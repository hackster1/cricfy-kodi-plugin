# Cricfy Plugin for Kodi

![Cricfy Plugin for Kodi](plugin.video.cricfy/icon.png)

Cricfy Plugin for Kodi is an unofficial Kodi add-on that lets you stream Cricfy content directly from your Kodi media center. The plugin aggregates streams and providers to give a convenient viewing experience from within Kodi.

## Features

- Browse and play Cricfy streams from within Kodi
- Aggregates multiple providers through Cricfy for higher availability

## Building the Plugin

### Automated Build (GitHub Actions)

The plugin is automatically built and packaged when code is pushed to the repository or when a new version tag is created. The GitHub Actions workflow (`.github/workflows/build.yml`) handles:

1. **Build Job**: Runs `main.py` to populate configuration files, then creates an artifact with the plugin directory
2. **Release Job** (on version tags): Creates a ZIP file and publishes it as a GitHub Release
3. **Pre-release Job** (on regular commits): Creates a ZIP file and publishes it as a pre-release

The workflow produces `plugin.video.cricfy-{version}.zip` files ready for installation in Kodi.

### Manual Build (Local)

To build the plugin locally and create a ZIP file:

1. **Prerequisites**: Python 3.12

2. **Run the build script**:
   ```bash
   python build.py
   ```

   This creates `plugin.video.cricfy.zip` in the current directory.

3. **Optional: Specify output directory**:
   ```bash
   python build.py -o dist
   ```

   This creates the ZIP file in the `dist/` directory.

4. **View all options**:
   ```bash
   python build.py --help
   ```

**Note**: The `build.py` script packages the plugin directory as-is. For a fully functional plugin, you may need to run `main.py` first to populate configuration files from environment variables (this is done automatically in the GitHub Actions workflow). The packaged plugin will work without this step, but may require configuration at runtime.

### How the Packaging Works

The `build.py` script:
- Locates the `plugin.video.cricfy` directory
- Creates a ZIP archive containing all files from the plugin directory
- Maintains the directory structure required by Kodi (plugin files must be inside a `plugin.video.cricfy/` folder within the ZIP)
- Outputs a `plugin.video.cricfy.zip` file ready for installation in Kodi

The resulting ZIP file contains:
- `addon.xml` - Plugin metadata and dependencies
- `main.py` - Main plugin entry point
- `service.py` - Background service
- `icon.png` - Plugin icon
- `lib/` - Python modules and libraries
- `resources/` - Configuration and resource files

## Installation

1. Download the latest plugin ZIP file from [Releases](https://github.com/itsyourap/cricfy-kodi-plugin/releases) to a location accessible from the device where Kodi is installed. Alternatively, build the plugin manually using the instructions above.
2. Open Kodi.
3. (Optional) Enable installation from unknown sources if required:
    - Go to Settings -> System -> Add-ons and enable "Unknown sources".
4. Install the add-on from the ZIP file:
    - From Kodi's home screen, go to Add-ons.
    - Open the Add-on browser (the open box icon in the top-left).
    - Choose "Install from zip file".
    - Navigate to and select the downloaded `plugin.video.cricfy.zip` file.
    - Wait for the "Add-on enabled" (or similar) notification.
5. Launch the plugin:
    - From the home screen go to Add-ons -> Video add-ons and open "Cricfy".

Notes:

- The exact menu labels may vary slightly between Kodi versions, but the "Install from zip file" method is common to all modern Kodi releases.

## Usage

- After installation open the add-on from Video Add-ons.
- Browse available providers, then select a provider to view their channels.

## Troubleshooting

- If the add-on fails to install, double-check that you selected the correct ZIP file and that "Unknown sources" is enabled (if applicable).
- If streams fail to play, check your internet connection and try another provider/stream in the add-on.
- For persistent issues, check Kodi's log (enable debug logging in Settings -> System -> Logging) and review the log file for errors.

## Credits

Some portions of the code were inspired by the following repository:

<https://github.com/NivinCNC/CNCVerse-Cloud-Stream-Extension/tree/master/CricifyProvider>

Please see that project for reference and additional context.

## Contributing

If you'd like to contribute improvements or fixes, fork the repository and submit a pull request with a clear description of your changes.

## License

[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)

You can use, study, share and modify it at your will. They can be redistributed and/or modified under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) version 3 or later published by the Free Software Foundation.

## Support

[![Buy Me a Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://buymeacoffee.com/itsyourap)

If you find this project helpful and would like to support its development, consider buying me a coffee! Your support helps keep the project alive and allows me to dedicate more time to improvements and new features. Thank you for your generosity!

## Disclaimer

This is an unofficial plugin. Use at your own risk. The plugin is not affiliated with Cricfy or Kodi.

## DMCA

We hereby issue this notice to inform you that this add-on just functions like an ordinary browser (like your browser) that fetches video files from internet, and do not violate the provisions of the Digital Millennium Copyright Act (DMCA). The Content this add-on may access is not hosted by us or the Kodi application but the websites it is browsing in their autonomous mode. It is sole responsibility of the user and his/her countries' or states' law. If you think it is violating any intellectual property then please contact the actual file hosts not the owners of this repository or the Kodi application.
