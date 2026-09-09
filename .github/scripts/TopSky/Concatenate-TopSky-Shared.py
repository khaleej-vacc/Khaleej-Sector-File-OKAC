import os
import shutil

# ============================================================
# OKAC TopSky Data File Compiler
# Compiles shared data files into each TopSky plugin variant
# ============================================================
#
# Three plugin variants share most of the same data:
#   - TopSky            : full compile, Realistic colours
#   - TopSky - Light     : full compile, Light colours
#   - TopSky Aerodrome  : maps only, built from its own separate
#                         Maps/Aerodrome/ dataset
#
# NOTE ON COLOURS:
# TopSky and TopSky - Light are identical except for the radar colour
# definitions. For this to work, the Maps/.Index entry that currently
# points at the colour file needs to use a {colour} placeholder, e.g.:
#
#     Radar/!Colours/{colour}.txt
#
# instead of a hardcoded "Radar/!Colours/Realistic.txt". This script
# fills in {colour} per-variant (Realistic / Light) when it reads the
# index. If you'd rather not touch the existing .Index, let me know and
# I can special-case the substitution instead.
#
# NOTE ON AERODROME:
# Currently assumed to only need the Maps step (built from
# Maps/Aerodrome/.Index rather than the normal Maps/.Index) plus the
# single-file ICAO data copies. Add step names to its 'steps' list
# below if it also needs Areas/Airspace/CPDLC/MSAW/Radars/SSRcodes/
# Settings.
# ============================================================

SHARED = '.data/TopSky Shared/'
INDEX  = '.Index'

# Each variant defines:
#   name          - label used in log output
#   output        - destination plugin folder
#   steps         - which compile steps to run for this variant
#   template_vars - dict used to fill in {placeholders} inside .Index
#                   entries (e.g. {colour} -> Radar/!Colours/{colour}.txt)
#   <step>_source - (optional) override the source folder used for that
#                   step, relative to SHARED. Defaults to the folder in
#                   STEP_SOURCE_FOLDERS below.
VARIANTS = [
    {
        'name': 'TopSky',
        'output': 'OKAC/Plugins/TopSky/',
        'steps': ['areas', 'airspace', 'cpdlc', 'maps', 'msaw', 'radars', 'ssr_codes', 'settings'],
        'template_vars': {'colour': 'Realistic'},
    },
    {
        'name': 'TopSky - Light',
        'output': 'OKAC/Plugins/TopSky - Light/',
        'steps': ['areas', 'airspace', 'cpdlc', 'maps', 'msaw', 'radars', 'ssr_codes', 'settings'],
        'template_vars': {'colour': 'Light'},
    },
    {
        'name': 'TopSky Aerodrome',
        'output': 'OKAC/Plugins/TopSky Aerodrome/',
        'steps': ['maps'],
        'maps_source': 'Maps/Aerodrome/',
    },
]

STEP_OUTPUT_NAMES = {
    'areas':     'TopSkyAreas.txt',
    'airspace':  'TopSkyAirspace.txt',
    'cpdlc':     'TopSkyCPDLC.txt',
    'maps':      'TopSkyMaps.txt',
    'msaw':      'TopSkyMSAW.txt',
    'radars':    'TopSkyRadars.txt',
    'ssr_codes': 'TopSkySSRcodes.txt',
    'settings':  'TopSkySettings.txt',
}

STEP_SOURCE_FOLDERS = {
    'areas':     'Areas/',
    'airspace':  'Airspace/',
    'cpdlc':     'CPDLC/',
    'maps':      'Maps/',
    'msaw':      'MSAW/',
    'radars':    'Radars/',
    'ssr_codes': 'SSRcodes/',
    'settings':  'Settings/',
}


def main():
    for variant in VARIANTS:
        print(f"\n=== Building {variant['name']} -> {variant['output']} ===")
        copy_single_files(variant)
        for step in variant['steps']:
            folder = variant.get(f'{step}_source', STEP_SOURCE_FOLDERS[step])
            build(variant, folder, STEP_OUTPUT_NAMES[step])


# ============================================================
# Single-file copies (no compilation needed)
# ============================================================

def copy_single_files(variant):
    singles = {
        'DataFiles/ICAO_Aircraft.json':  'ICAO_Aircraft.json',
        'DataFiles/ICAO_Aircraft.txt':   'ICAO_Aircraft.txt',
        'DataFiles/ICAO_Airlines.txt':   'ICAO_Airlines.txt',
        'DataFiles/ICAO_Airports.txt':   'ICAO_Airports.txt',
    }
    for src, dst in singles.items():
        copy_file(SHARED + src, variant['output'] + dst)


# ============================================================
# Core build logic
# ============================================================

def build(variant, folder, output_name):
    """
    Compiles all .txt files in a shared folder into a single output
    file for this variant.
    """
    src_folder = SHARED + folder
    template_vars = variant.get('template_vars', {})

    files = get_file_list(src_folder, template_vars)
    if not files:
        print(f'[SKIP] No files found for {output_name} ({folder})')
        return

    dst = variant['output'] + output_name
    os.makedirs(variant['output'], exist_ok=True)

    with open(dst, 'wb') as out:
        for relative_path in files:
            full_path = src_folder + relative_path
            if not os.path.exists(full_path):
                print(f'[WARN] Missing: {full_path}')
                continue
            with open(full_path, 'rb') as f:
                shutil.copyfileobj(f, out)
                out.write(b'\n\n')

    print(f'[OK]   Built {dst} from {len(files)} file(s)')


# ============================================================
# File ordering
#
# Same logic as the ORBB compiler (.Index at any depth is honored,
# with alphabetical auto-discovery filling in anything not listed),
# plus {placeholder} substitution on each .Index line so one shared
# index can serve multiple variants (e.g. colour swapping).
# ============================================================

def get_file_list(folder_path, template_vars):
    return collect_txt_files(folder_path, prefix='', template_vars=template_vars)


def collect_txt_files(folder_path, prefix='', template_vars=None):
    template_vars = template_vars or {}
    index_path = os.path.join(folder_path, INDEX)

    if os.path.exists(index_path):
        return read_index_with_remainder(folder_path, prefix, index_path, template_vars)

    return auto_discover(folder_path, prefix=prefix, template_vars=template_vars)


def read_index_with_remainder(folder_path, prefix, index_path, template_vars):
    files = []
    covered = set()
    label = prefix.rstrip('/') or '(root)'

    with open(index_path, 'r') as f:
        for raw_line in f:
            line = raw_line.split('//')[0].strip()
            if not line:
                continue

            try:
                line = line.format(**template_vars)
            except KeyError as e:
                print(f'[WARN] Unresolved placeholder {e} in "{line}" ({index_path})')
                continue

            if line.endswith('/'):
                sub_name = line.rstrip('/')
                sub_path = os.path.join(folder_path, sub_name)
                if not os.path.exists(sub_path):
                    print(f'[WARN] Subfolder not found: {sub_path}')
                    continue
                sub_files = collect_txt_files(sub_path, prefix=prefix + sub_name + '/', template_vars=template_vars)
                files.extend(sub_files)
                covered.add(sub_name)
                print(f'[INFO] {prefix}{line} expanded to {len(sub_files)} file(s)')

            elif '.' in line:
                files.append(prefix + line)
                top = line.split('/')[0]
                covered.add(top)

            else:
                print(f'[WARN] Skipped index entry (no extension or /): "{line}" in {index_path}')

    print(f'[INFO] {label} index supplied {len(files)} entry/entries')

    remainder = collect_remainder(folder_path, covered, prefix, template_vars)
    if remainder:
        print(f'[INFO] {label} appending {len(remainder)} unlisted file(s) alphabetically')
        files.extend(remainder)

    print(f'[INFO] {label} total: {len(files)} file(s)')
    return files


def collect_remainder(folder_path, covered, prefix, template_vars):
    files = []
    try:
        entries = sorted(os.scandir(folder_path), key=lambda e: e.name)
    except FileNotFoundError:
        return files

    for entry in entries:
        if entry.is_dir() and not entry.name.startswith('.'):
            if entry.name not in covered:
                sub_files = collect_txt_files(entry.path, prefix=prefix + entry.name + '/', template_vars=template_vars)
                files.extend(sub_files)

    for entry in entries:
        if entry.is_file() and entry.name.endswith('.txt') and not entry.name.startswith('.'):
            if entry.name not in covered:
                files.append(prefix + entry.name)

    return files


def auto_discover(folder_path, prefix='', template_vars=None):
    template_vars = template_vars or {}
    files = []
    try:
        entries = sorted(os.scandir(folder_path), key=lambda e: e.name)
    except FileNotFoundError:
        print(f'[WARN] Folder not found: {folder_path}')
        return files

    for entry in entries:
        if entry.is_dir() and not entry.name.startswith('.'):
            files.extend(collect_txt_files(entry.path, prefix=prefix + entry.name + '/', template_vars=template_vars))

    for entry in entries:
        if entry.is_file() and entry.name.endswith('.txt') and not entry.name.startswith('.'):
            files.append(prefix + entry.name)

    return files


# ============================================================
# File utilities
# ============================================================

def copy_file(src, dst):
    if not os.path.exists(src):
        print(f'[WARN] Missing source: {src}')
        return
    parent = os.path.dirname(dst)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copy(src, dst)
    print(f'[OK]   Copied {src} -> {dst}')


if __name__ == '__main__':
    main()