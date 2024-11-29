# [U.A.E FIR] AIRAC 2412
@U.A.E FIR Operations The Operations Department has been updating the **U.A.E FIR [OMAE]** sector file. Controllers must perform a clean installation of the sector file, as significant changes have been made to the folder structure and files throughout the entire sector. These modifications are essential for the proper functioning of the system, and installing the new sector file over the old one could lead to errors or misconfigurations. To ensure everything works as intended and to avoid any potential issues, it is crucial to fully uninstall the previous version and follow the clean installation process.

This release now allows us to fully utilize the capabilities of TopSky and GRplugin. Please review the changelog below for the details of the changes.

## Sector File Changelog:
### Discord Euroscope
- The position data in the config file has been updated.

### DelHel
- The DelHel "DEL" item in the departure list has been deactivated for all profiles as it was causing issues for airports with more than two departures runways with initial climbs on each SID. Initial climbs should now be set using the TopSky "Cleared Flight Level (CFL)" menu by left-clicking in the "CFL" column.

### TopSky Plugin
Several updates have been made to the TopSky maps after testing them on the Dubai TMA. Everything is now drawn dynamically by TopSky, and there is no need to adjust display settings anymore—it is now configured in a "plug and play" format.

- [AERODROME-MAKTOUM] Maktoum dataset has been created due to symbology differences with Dubai.
- [AERODROME-NORTH] Dubai dataset has been revised to better match its real-world counterpart. The Minhad restricted zone has been updated, and OMR96 + OMR62 have been reactivated on the display. Dynamic frequencies have been added to the displays.
- [AERODROME-SOUTH] A basic Sheikh Zayed dataset has been implemented for daily operations while awaiting more real-world references. Dynamic frequencies have been added to the displays.
- [CTA] A general dataset has been created for Ras Al Khaimah and Fujairah.
- [CTA Abu Dhabi] Abu Dhabi has received updates to better align with its real-world counterpart. Several restricted zones have been reactivated to match real-world displays. Dynamic frequencies have been added to the displays.
- [CTA Dubai] Runway configuration numbers have been added in accordance with the real-world display. Dynamic frequencies have been added to the displays.
- [CTA Military] A general dataset has been created for military aerodromes, such as Minhad and Al-Dhafra.
- [Enroute] Automatic sector ownership displays have been added (still experimental, but functional for now as we refine them). Proper terminal maneuvering areas and control zone maps have been added. Zoom parameters have been included to show both upper and terminal displays, with basic TMA FIX points and extended centerlines in a cleaner format. Lower quality coastline (SPORTS MODE!) has been reactivated to save frames.
- [PLUGIN] Updated to version 2.5 beta 15.

### Ground Radar Plugin
The entire U.A.E FIR has been redrawn on QGIS using accurate satellite imagery and fully leveraging the Ground Radar Plugin, as some of the ground layouts hadn't been updated since 2018. The following SMGCS ASRs are now available: Al-Ain, Al-Bateen, Al-Dhafra, Al-Maktoum, Arzanah, Das Island, Delma, Dubai, Fujairah, Minhad, Qarnayn, Ras Al Khaimah, Sharjah, Sheikh Zayed, Sir Bani Yas, and Zirku. Each airport’s configuration has also been set, including maximum aircraft category per runway and low visibility procedure buffers.

Observers & Controllers can adjust their SMGCS displays by navigating to the top menu and selecting: FUNCTIONS -> MAPS -> [NAME SMGCS], where they can enable or disable the desired maps for display.

- [SMGCS] The Sheikh Zayed SMGCS has been redrawn, with updated colors to better reflect real-world displays. Ongoing adjustments are being made to address the color vibrancy differences between real-world screens and Euroscope. Intermediate Holding Points are disabled by default to reduce screen clutter; however, they can be enabled by navigating to FUNCTIONS -> MAPS -> Sheikh Zayed SMGCS. Code F restriction safety nets have been added, along with closed taxiway nets. The stand assignment dataset is now complete, and the stand auto-assign feature is fully functional.
- [SMGCS] Al-Bateen has been redrawn and implemented.
- [SMGCS] Al-Ain has been redrawn and implemented.
- [SMGCS] Al-Dhafra has been created and implemented.
- [SMGCS] Qarnayn has been created and implemented.
- [SMGCS] Arzanah has been created and implemented.
- [SMGCS] Das Island has been created and implemented.
- [SMGCS] Zirku has been created and implemented.
- [SMGCS] Sir Bani Yas Island has been redrawn and implemented.
- [SMGCS] Dubai's colors have been updated to reflect real-world displays, as the previous color set was for Abu Dhabi. Code F restriction safety nets have been added.
- [SMGCS] Delma has been created and implemented.
- [SMGCS] Minhad has been created and implemented.
- [SMGCS] Al-Maktoum has been redrawn and implemented. Stand assignment dataset is complete, and stand auto-assign now functions.
- [SMGCS] Fujairah has been redrawn and implemented. Runway 11L/29R is closed, and safety nets have been added.
- [SMGCS] Ras Al Khaimah has been redrawn and implemented.
- [SMGCS] Sharjah has been redrawn and implemented. Code F restriction safety nets have been added, and closed taxiway nets are included. Stand assignment dataset is complete, and stand auto-assign now functions.
- [APPROACH WINDOW] Extended runway centerlines, control zones, and terminal maneuvering areas have been added.
- [SETTINGS] Departure timer window is now enabled by default. Airports using multiple runways for departure will have their timers stacked. Please drag the top one to reveal the one below!
- [SETTINGS] Filter has been refined to hide aircraft with their transponder set to standby.
- [SETTINGS] Ground status has been changed back to their full wording.

### VACDM
- Configuration added to the server backend for Dubai.

### vATIS
- The U.A.E FIR vATIS profile has been updated to include "V-ACDM IN USE. SET YOUR TOBT AT VACDM.VATSIM.ME" in the ARPT CONDITIONS tab for Sheikh Zayed and Dubai. The .json file is available in OMAE/Plugins/vATIS.

### Changes
- [NAVDATA] AIRAC 2412 has been applied.
- [ASR] Previous ASRs have been revised.
- [SETTINGS-PROFILES] All profiles within the U.A.E FIR have been updated to include vatglasses.uk for sector information and vats.im/arb/airports for pilot briefings (still under development). The feedback link has been updated. DCLs have been removed for airports that do not support them in the real world.
- [SETTINGS-PROFILES] Each profile will now only display the relevant positions in the dropdown.
- [SETTINGS-VOICE] Each profile will now only display the relevant frequencies in the window.
- [SETTINGS-VCCS] The VCCS panel has been updated for Dubai and Abu Dhabi.
- [SETTINGS-SYMBOLOGY] Symbology for Abu Dhabi CTA has been updated.
- [SETTINGS-SYMBOLOGY] Symbology for Minhad CTA has been created.
- [SETTINGS-TAGS] Tags have been renamed to remove underscores.
- [SOUNDS] The startup sound has been updated for Dubai Aerodrome, Dubai CTA, and U.A.E Enroute.
- [ALIAS] Dubai vacate aliases have been revised.
- [ALIAS] "CLEAR DIRECTIONS" has been added to the vacate alias.
- [ALIAS] Capital letters have been removed from the start of each message, as Euroscope automatically adds the selected aircraft callsign followed by a comma.
- [ALIAS] Holding alias has been refined, including where to find the "published" hold information.
- [ALIAS] .invalfl has been changed to .ifl, and the message has been refined. Added .msg so it sends a private message directly.
- [ALIAS] .routefull has been changed to .rtef to comply with the new SimBrief method, and .msg has been added to send a private message directly.
- [ALIAS] .deg/itr/ors/pas/pat/res/sod/tap/tom have been refined, and .msg has been added to send a private message directly.

### Additions
- [PROFILES] New profiles have been implemented for Das Island, Delma, Fujairah, Minhad, Ras Al Khaimah, Sir Bani Yas Island, and Zirku.
- [ASR] New ASRs have been implemented for Al-Dhafra, Das Island, Delma, Fujairah, Minhad, Ras Al Khaimah, Sir Bani Yas Island, and Zirku.
- [ALIAS] .loudmic has been added for pilots with poorly calibrated microphones that are set to an incorrect level.
- [ALIAS] .tatl has been added for pilots who do not distinguish between altitude and flight levels.
- [ALIAS] Abu Dhabi vacate aliases have been added.
- [ALIAS] ALNEV holding information has been added.
- [ALIAS] Aliases for 160kts till 4 DME (.160), 190kts till 10 DME (.190), and the combined instruction (.169) have been added.
- [ALIAS] .ctor has been added for RRSM take-off clearance.
- [ALIAS] .ctlr has been added for RRSM landing clearance.
- [ALIAS] .route has been changed to .rte, removing the need to add a new route. Instead, it instructs pilots to select our purple user-defined routes on SimBrief upon first contact.
- [ALIAS] .gm, .gaf, and .ge good morning/afternoon/evening aliases have been re-added.

### Removals
- [ALIAS] Removed vATIS subscription commands as with the latest version of Euroscope you can see the identifier for both the departure & arrival ATIS'.

[U.A.E FIR AeroNav Download](https://files.aero-nav.com/OMAE)

## Notice Confirmation
Controllers are required to acknowledge this operations update by clicking the :greentick: to confirm receipt. Please ensure that your sector file is updated accordingly. We have implemented several checks that allow us to easily identify if your sector file is not up to date!

## Interested in Contributing? Contribute now on GitHub!
In an effort to encourage contributions from everyone, the Sector File configuration files are now available on the **Arabian vACC GitHub Organization.**

Anyone can contribute or report issues by opening an issue to highlight a problem or suggest improvements. Members interested in contributing should fork the repository to their own account and submit a pull request for review and inclusion in the next AIRAC cycle.

[U.A.E FIR GitHub Repository](https://github.com/Arabian-vACC/OMAE-U.A.E-FIR-Controller-Pack)