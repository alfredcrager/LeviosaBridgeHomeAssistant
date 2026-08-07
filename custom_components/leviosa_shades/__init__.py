"""The Leviosa shades Zone integration."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import service

from .const import DOMAIN, SERVICE_NEXT_DOWN_POS, SERVICE_NEXT_UP_POS

PLATFORMS = [Platform.COVER]


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Leviosa shades Zone component."""
    service.async_register_platform_entity_service(
        hass,
        DOMAIN,
        SERVICE_NEXT_DOWN_POS,
        entity_domain=Platform.COVER,
        func="next_down_pos",
        schema={},
    )
    service.async_register_platform_entity_service(
        hass,
        DOMAIN,
        SERVICE_NEXT_UP_POS,
        entity_domain=Platform.COVER,
        func="next_up_pos",
        schema={},
    )
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Leviosa shades Zone from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
