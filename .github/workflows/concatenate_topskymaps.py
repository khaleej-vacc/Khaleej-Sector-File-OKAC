import os

def concatenate_files(source_directory, output_file):
    with open(output_file, 'w') as outfile:
        for filename in sorted(os.listdir(source_directory)):
            file_path = os.path.join(source_directory, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as infile:
                    for line in infile:
                        stripped_line = line.strip()
                        if stripped_line:
                            if stripped_line.startswith('//&preserve'):
                                # Remove the //&preserve prefix but keep the // and the rest of the line
                                stripped_line = '//' + stripped_line[len('//&preserve'):].strip()
                            elif stripped_line.startswith('//'):
                                # Skip lines starting with // that don't start with //&preserve
                                continue
                            outfile.write(stripped_line + '\n')  # Write the cleaned line

def main():
    base_dir = '.data/TopSkyMaps'
    targets = [
        ('TopSky', 'OKAC/Plugins/TopSky/TopSkyMaps.txt'),
        ('TopSky Aerodrome', 'OKAC/Plugins/TopSky Aerodrome/TopSkyMaps.txt'),
    ]

    for source_subdir, target_file in targets:
        source_directory = os.path.join(base_dir, source_subdir)
        print(f'Building {target_file} from {source_directory}')
        concatenate_files(source_directory, target_file)
        print(f'{target_file} built successfully.')

if __name__ == '__main__':
    main()
