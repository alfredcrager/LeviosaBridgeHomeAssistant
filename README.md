# Leviosa WiFi Zone Bridge Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=alfredcrager&repository=LeviosaBridgeHomeAssistant&category=integration)

This integration uses [Leviosa's](https://leviosashades.com)
original Home Assistant [custom component implementation](https://leviosashades.com/pages/beta-testing-for-home-assistant) 
to make Leviosa's WiFi Zone bridge and associated shades available for use 
with Home Assistant.

## Installation

### Option 1: Install via HACS (Recommended)

1. Make sure you have [HACS](https://hacs.xyz/) installed
2. Click the button below to add this repository to HACS:

   [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=alfredcrager&repository=LeviosaBridgeHomeAssistant&category=integration)
   
   Or manually add it:
   - In HACS, click on "Integrations"
   - Click the three dots menu in the top right corner
   - Select "Custom repositories"
   - Add `https://github.com/alfredcrager/LeviosaBridgeHomeAssistant` as an Integration
   - Click "Add"

3. Search for "Leviosa Motor Shades" in HACS and install it
4. Restart Home Assistant
5. Add the Leviosa integration through "Devices & services" under "Settings"

### Option 2: Manual Installation

This component is an _integration_, which is different from an _add on_.
Integrations are managed through the "Devices & Services" configuration menu
rather than through "Add-ons, Backups & Supervisor".

Install this integration manually by cloning this repository and copying the 
integration files to the proper location in your HA config directory.

Clone this repository and copy the `custom_components/leviosa_shades` folder into your
`<config>/custom_components/` directory (so you end up with
`<config>/custom_components/leviosa_shades`).

Restart Home Assistant after installation.

Add the Leviosa integration through "Devices & services" under "Settings" in 
Home Assistant

## Development

### Version Management

When creating a new release:

1. Update the version in `custom_components/leviosa_shades/manifest.json`
2. Commit the version change: `git commit -am "Bump version to X.Y.Z"`
3. Create a git tag matching the version: `git tag vX.Y.Z`
4. Push the changes and tag: `git push && git push --tags`

The GitHub Actions workflow will automatically create a release when a version tag is pushed. 
HACS uses GitHub releases to notify users of updates, so it's important that:
- The version in `manifest.json` matches the git tag
- Releases follow semantic versioning (X.Y.Z format)
- Pre-release versions can include suffixes like `-beta` or `-rc`