# Compatibility

| Item | Verified project configuration |
|---|---|
| BMS | JBD DP04S007-L4S 60A, 4S, PCB V2.1 |
| Controller | ESP32-C3 Zero, ESP-IDF framework |
| UART | ESP GPIO4 TX, GPIO5 RX, 9600 8N1 |
| ESPHome | Configuration declares minimum version `2026.4.0` |
| UART defaults | `logger.level: WARN`, `update_interval: 5s`, `rx_timeout: 300ms` |

The firmware uses [syssi/esphome-jbd-bms](https://github.com/syssi/esphome-jbd-bms) as an external ESPHome component. Its source is not included here. The configuration currently references the moving `@main` branch; pin a tested upstream revision for reproducible builds.

The Home Assistant dashboards use built-in cards, including **Sections**, **Entities**, **Tile**, **Grid**, **Markdown**, **Statistics graph**, and **Conditional**. Ensure your Home Assistant version supports these features and the device's entity IDs match the sample.

**Scope:** Monitoring may work on other JBD models, but EEPROM registers, control commands and electrical pinouts are **not verified** for other boards. See [TESTING.md](TESTING.md).
