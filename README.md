# Leviosa WiFi Zone Bridge Integration for Home Assistant

This integration uses [Leviosa's](https://leviosashades.com)
original Home Assistant [custom component implementation](https://leviosashades.com/pages/beta-testing-for-home-assistant) 
to make Leviosa's WiFi Zone bridge and associated shades available for use 
with Home Assistant.

## Installation

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