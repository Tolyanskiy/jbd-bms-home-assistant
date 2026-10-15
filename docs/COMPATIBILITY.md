# Compatibility and dependencies

**Owner-tested hardware:** JBD DP04S007-L4S 60A (4S, PCB revision V2.1) + ESP32-C3 Zero + TTL UART GPIO4/5, 9600 8N1. Other JBD models and firmware revisions **may not implement the same EEPROM register behavior**, even if basic telemetry works.

**Firmware framework:** ESPHome with ESP-IDF on ESP32-C3. The shipped source declares `min_version: 2026.4.0`. This package was not compiled by the authoring environment; use your current ESPHome Validate and compile workflows before deployment.

**External component:** [`syssi/esphome-jbd-bms`](https://github.com/syssi/esphome-jbd-bms), Apache-2.0 licensed. The configuration currently references `github://syssi/esphome-jbd-bms@main`. Upstream may change at any moment: record and pin a **verified Git commit** for repeatable builds, rather than assuming `main` is permanent.

**Home Assistant:** The dashboard uses built-in Lovelace `sections`, `entities`, `tile`, `grid`, `markdown`, `statistics-graph`, and `conditional` cards and does not need HACS custom cards. Sections view and Markdown templating must be supported by the installed Home Assistant version. The device name `jbd-bms` is used to derive dashboard entity IDs.

**Localization:** The panels can be switched independently of firmware. Firmware language determines ESPHome-generated profile status text; both firmware variants otherwise share configuration logic.


## Published UART defaults

ESP32-C3 UART uses 9600 8N1, `update_interval: 5s`, `rx_timeout: 300ms`, and `logger.level: WARN` for the maintained public beta.
