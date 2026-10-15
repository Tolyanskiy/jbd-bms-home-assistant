# JBD BMS ESPHome Configurator

**Monitor and configure a JBD Smart BMS through ESPHome and Home Assistant.** Includes English and Ukrainian dashboards.

[Українська документація](README_UA.md) · [Installation](docs/INSTALL_EN.md) · [Hardware](docs/HARDWARE.md) · [Configuration](docs/CONFIGURATION.md)

## Features

- Live telemetry: pack/cell-group voltage, current, power, SOC, capacity, temperature and protection status.
- Discharge MOSFET control and state display.
- Read ten BMS EEPROM configuration registers without changing settings; compare EEPROM with DRAFT values.
- Protected EEPROM configuration: DRAFT validation, time-limited ARM, backup, APPLY and read-back verification.
- Built-in project preset and persistent custom profile; loading a profile only changes DRAFT.
- Six-view Home Assistant dashboards in English and Ukrainian; no custom Lovelace cards required.

## Compatibility

Tested by the maintainer with **JBD DP04S007-L4S 60A (4S, PCB V2.1)** and **ESP32-C3 Zero**. EEPROM APPLY and read-back have been exercised on this setup. Compatibility with other JBD models and PCB revisions is not established. This is a **beta release**; see [testing scope](docs/TESTING.md).

The tested setup also uses a **5 V DC-DC converter powered from the battery B+/B− terminals** and an optional external **ZNLD active balancer**. See [hardware wiring](docs/HARDWARE.md) before connecting your controller.

## Installation

1. Review [hardware compatibility and UART wiring](docs/HARDWARE.md). The sample uses ESP32 GPIO4 (TX) → JBD RX and GPIO5 (RX) ← JBD TX at **9600 8N1**.
2. Choose a firmware file: [`firmware/jbd-bms-en.yaml`](firmware/jbd-bms-en.yaml) or [`firmware/jbd-bms-ua.yaml`](firmware/jbd-bms-ua.yaml). Firmware variants share configuration logic and entity IDs but localize profile messages.
3. Set up local Wi-Fi/API secrets using [`secrets.yaml.example`](secrets.yaml.example). **Do not commit your real `secrets.yaml`.**
4. Validate and install the YAML through ESPHome Device Builder.
5. Add a Home Assistant dashboard using [`dashboards/jbd-dashboard-en.yaml`](dashboards/jbd-dashboard-en.yaml) or [`dashboards/jbd-dashboard-uk.yaml`](dashboards/jbd-dashboard-uk.yaml) in the **raw dashboard configuration editor**.
6. Verify telemetry and use **Read All 10 EEPROM Parameters** to obtain fresh stored values before comparing them with DRAFT.

Detailed instructions: [English](docs/INSTALL_EN.md) · [Українською](docs/INSTALL_UA.md).

## Configuration

**Project preset → Custom profile → DRAFT → EEPROM** are different layers. Profile changes do not write the BMS until the separate guarded APPLY operation. Project values are examples for the documented 4S pack, **not universal safety settings**. Read [configuration and register reference](docs/CONFIGURATION.md) before making changes.

The firmware uses `logger.level: WARN`, `jbd_bms.update_interval: 5s` and `jbd_bms.rx_timeout: 300ms`. These defaults were reported to improve UART reliability in the tested setup; results may vary by wiring and hardware.

## License and credits

The original materials in this repository are distributed under the [MIT License](LICENSE). This configuration depends on [syssi/esphome-jbd-bms](https://github.com/syssi/esphome-jbd-bms) (Apache-2.0); its source is not bundled. The upstream component is currently referenced at `@main`; pin a tested commit for reproducible deployments.

Bug reports and pull requests are welcome. See [Contributing](CONTRIBUTING.md).
