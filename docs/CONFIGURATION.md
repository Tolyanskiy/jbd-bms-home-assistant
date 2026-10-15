# Configuration, profiles and EEPROM

## EEPROM registers

| Register | Parameter | Raw unit | Project preset |
|---|---|---|---:|
| `0x20` | Pack overvoltage | 0.01 V | 14.60 V |
| `0x21` | Pack OVP recovery | 0.01 V | 14.00 V |
| `0x22` | Pack undervoltage | 0.01 V | 10.50 V |
| `0x23` | Pack UVP recovery | 0.01 V | 11.50 V |
| `0x24` | Cell overvoltage | 0.001 V | 3.650 V |
| `0x25` | Cell OVP recovery | 0.001 V | 3.500 V |
| `0x26` | Cell undervoltage | 0.001 V | 2.550 V |
| `0x27` | Cell UVP recovery | 0.001 V | 3.000 V |
| `0x2A` | Passive balance start | 0.001 V | 3.300 V |
| `0x2B` | Passive balance voltage delta | 0.001 V | 0.015 V |

These are **project presets**, not manufacturer defaults or universal LiFePO₄ recommendations. Actual EEPROM values can differ: **always read the BMS** to determine what it has stored. Preset constants are defined in the firmware's `substitutions:` block.

## Parameter layers

- **Project preset:** read-only reference values built into the firmware.
- **Custom profile:** user-defined values saved in ESP32 flash after an explicit save.
- **DRAFT:** working values prepared for comparison and optional EEPROM programming.
- **EEPROM:** parameters stored by the JBD BMS, retrieved by the independent reader.

Loading profiles into DRAFT does **not** write to the BMS.

## EEPROM operations

**Read All 10 Parameters** opens a read-only factory-mode session, retrieves ten settings and exits without saving. A message of `Read 10/10; exit confirmed; NO WRITE` indicates a successful response and acknowledged exit, not a physical protection-cutoff test.

**APPLY** is a separate action requiring the configuration unlock and 60-second ARM gate. It obtains original register values, sends changed parameters, commits, and reads back the settings. Re-read all ten registers independently after programming. The displayed raw backup is diagnostic information, **not** an off-device archival copy.

Some protocol commit operations may reset historical BMS protection counters. Retrieve and retain those counters separately if event history matters.

**Recovery thresholds** apply when protection has tripped; exact MOSFET recovery behavior depends on the BMS model and firmware. Do not assume preset thresholds match another battery pack or charger.
