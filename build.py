#!/usr/bin/env python3
"""
Build script for Cricfy Kodi Plugin.

This script packages the plugin.video.cricfy directory into a deployable ZIP file
that can be installed in Kodi.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional
from zipfile import ZIP_DEFLATED, ZipFile


def build_plugin(output_dir: Optional[Path] = None, plugin_name: str = "plugin.video.cricfy") -> Path:
    """
    Package the Kodi plugin directory into a ZIP file.
    
    Args:
        output_dir: Directory where the ZIP file will be created. Defaults to current directory.
        plugin_name: Name of the plugin directory to package. Defaults to "plugin.video.cricfy".
    
    Returns:
        Path to the created ZIP file.
    
    Raises:
        FileNotFoundError: If the plugin directory doesn't exist.
        ValueError: If the plugin path exists but is not a directory.
        IOError: If packaging fails.
    """
    current_dir = Path(__file__).resolve().parent
    plugin_dir = current_dir / plugin_name
    
    # Validate plugin directory exists
    if not plugin_dir.exists():
        raise FileNotFoundError(f"Plugin directory not found: {plugin_dir}")
    
    if not plugin_dir.is_dir():
        raise ValueError(f"Path exists but is not a directory: {plugin_dir}")
    
    # Set output directory
    if output_dir is None:
        output_dir = current_dir
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create ZIP file
    zip_filename = f"{plugin_name}.zip"
    zip_path = output_dir / zip_filename
    
    print(f"Packaging plugin from: {plugin_dir}")
    print(f"Creating ZIP file: {zip_path}")
    
    try:
        with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zipf:
            # Walk through the plugin directory and add all files
            for file_path in plugin_dir.rglob('*'):
                if file_path.is_file():
                    # Calculate the archive name (relative path from parent of plugin_dir)
                    arcname = file_path.relative_to(current_dir)
                    zipf.write(file_path, arcname)
                    print(f"  Adding: {arcname}")
    except Exception as e:
        # Clean up partial ZIP file if creation failed
        if zip_path.exists():
            zip_path.unlink()
        raise IOError(f"Failed to create ZIP file: {e}") from e
    
    print(f"\n✓ Successfully created: {zip_path}")
    print(f"  Size: {zip_path.stat().st_size / 1024:.2f} KB")
    return zip_path


def main():
    """Main entry point for the build script."""
    parser = argparse.ArgumentParser(
        description="Build and package the Cricfy Kodi plugin into a ZIP file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build.py                    # Create plugin.video.cricfy.zip in current directory
  python build.py -o dist            # Create ZIP in dist/ directory
  python build.py --output-dir dist  # Same as above
        """
    )
    
    parser.add_argument(
        '-o', '--output-dir',
        type=str,
        default=None,
        help='Directory where the ZIP file will be created (default: current directory)'
    )
    
    parser.add_argument(
        '--plugin-name',
        type=str,
        default='plugin.video.cricfy',
        help='Name of the plugin directory to package (default: plugin.video.cricfy)'
    )
    
    args = parser.parse_args()
    
    try:
        build_plugin(
            output_dir=Path(args.output_dir) if args.output_dir else None,
            plugin_name=args.plugin_name
        )
        return 0
    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
