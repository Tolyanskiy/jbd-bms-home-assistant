# Audit and testing notes

## Checks included in this release

- YAML parsed for both ESPHome variants (including `!secret`) and both Home Assistant dashboards.
- The English and Ukrainian dashboards were compared structurally: **same six views, same entity identifiers, same actions**.
- Original firmware and optional English firmware compared after replacing localized **profile-status string literals**; no commands, GPIO definitions, register constants, or algorithmic control flow were intentionally modified.
- No literal Wi-Fi/API secrets, personal identifiers, or external component source copies included.
- All code comments in shipped firmware checked for Ukrainian characters; dashboard language localized separately.

## Hardware tests reported by the owner (not reproduced in this release build)

- UART telemetry and discharge MOSFET interface were in use.
- Independent 10/10 EEPROM read displayed valid returned threshold values.
- APPLY configuration and read-back were reported working on the owner’s device.
- Custom profile edit/save and comparison were exercised in Home Assistant.

## Still to test before marking stable

- Actual ESPHome validation and compilation on the current installed version.
- Fresh install on a second/clean Home Assistant system, including entity-ID mapping.
- Verification of setup instructions, pinout and electrical levels for each supported BMS board revision.
- Negative-path handling: timeouts, interrupted UART, interrupted BMS power, interrupted transaction, malformed response.
- Dedicated bench tests of hardware cutoff/recovery behavior where relevant, rather than assuming readings alone establish it.

**Release classification:** `v0.1.0-beta`, not a universal verified hardware controller.


## UART reliability observation

The maintainer reports UART errors stopped after changing logging to WARN, polling to 5s, and RX timeout to 300ms. This is field observation, not a measured error-rate certification; longer-term testing under different charger/load modes is welcome.
