# Testing and verification

## Tested on the reference hardware

The maintainer reports successful operation with JBD DP04S007-L4S 60A (4S, PCB V2.1) and ESP32-C3 Zero:

- UART telemetry in Home Assistant.
- Discharge MOSFET control via the dashboard.
- Independent read and comparison of ten EEPROM configuration registers.
- EEPROM APPLY and read-back of the changed configuration.
- Custom-profile editing, persistence and DRAFT loading.
- Improved UART reliability using WARN logging, 5-second polling and 300 ms receive timeout.

## Automated checks

`python tools/static_audit.py` checks YAML parsing, language-variant structure, entity references and common accidental secret inclusion. CI runs this static check on pushes and pull requests when the included GitHub Actions workflow is enabled.

## Not covered by this test scope

- A full ESPHome compile or deployment from a clean machine for every supported version.
- Compatibility with other JBD models, board revisions or UART voltage levels.
- Independent validation of protection cutoffs, hardware fault tolerance or interrupted EEPROM transactions.

The release is marked **beta**. Contributors can report reproducible compatibility results using the issue template.
