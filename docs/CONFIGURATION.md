# Configuration, DRAFT, profiles and EEPROM

## Ten thresholds / registers

| Register | Function | Unit | Project example (V) |
|---|---|---|---:|
| `0x20` | Pack overvoltage (OVP) | 0.01 V/raw | 14.60 |
| `0x21` | Pack OVP recovery | 0.01 V/raw | 14.00 |
| `0x22` | Pack undervoltage (UVP) | 0.01 V/raw | 10.50 |
| `0x23` | Pack UVP recovery | 0.01 V/raw | 11.50 |
| `0x24` | Cell overvoltage | 0.001 V/raw | 3.650 |
| `0x25` | Cell OVP recovery | 0.001 V/raw | 3.500 |
| `0x26` | Cell undervoltage | 0.001 V/raw | 2.550 |
| `0x27` | Cell UVP recovery | 0.001 V/raw | 3.000 |
| `0x2A` | Passive balance start | 0.001 V/raw | 3.300 |
| `0x2B` | Passive balance delta | 0.001 V/raw | 0.015 |

**Example only:** These are project preset constants, not factory defaults or safety recommendations for other BMS, cells, charging profiles or UPSes. The owner later read back a **Pack UVP of 10.20 V** on this actual BMS, which may **not** match the `10.50 V` project preset. The EEPROM readout is the source of actual stored values.

The single source for *project preset* parameters is the `substitutions:` section near the top of the firmware file. Changing it requires ESPHome build and flashing; it does not directly change BMS EEPROM. Existing saved user/DRAFT profiles in ESP32 flash may persist after a firmware update.

## Four parameter layers

- **Project preset**: fixed firmware example defaults.
- **Custom profile**: editable values saved in ESP32 preferences only after Save Custom Profile.
- **DRAFT**: working values used to prepare an eventual EEPROM operation; can be loaded from either profile. Not written to BMS merely by editing.
- **EEPROM**: independently read BMS configuration registers (ten-register reader). Read after restart to obtain fresh values; comparisons require a successful current-session read.

## APPLY sequence (owner-tested on this hardware)

1. Unlock configuration editing.
2. Enter and validate DRAFT.
3. Review / ARM (expires after 60 seconds).
4. Press APPLY while conditions required by the firmware are met.
5. Transaction obtains ten original values as a diagnostic backup, writes changed registers, issues a commit, opens another factory-mode session, and checks all ten values.
6. Read all ten EEPROM registers independently afterwards to verify. The on-screen diagnostic backup is not a persisted remote archive.

The operation is deliberately not triggered by profile actions, HA startup, or an EEPROM read button. Power/temperature/current protections of the BMS require independent hardware verification.

## EEPROM read status

`Read 10/10; exit confirmed; NO WRITE` means ten expected register read responses were received and the device acknowledged exit without parameter changes. It is not a verification of actual hardware cutoff behavior. `unknown` indicates a value is not available yet, commonly after ESP32 restart and before reading.

### Error counters

Some JBD protocol commit procedures can clear historical protection counters. Track them separately if event history matters. Reading them uses the **Read Error Counters** button.
