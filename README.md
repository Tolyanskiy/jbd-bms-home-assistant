# JBD BMS ESPHome Configurator

**UART monitoring, EEPROM read/write, protection-threshold profiles, and Home Assistant dashboards in English and Ukrainian.**

> **Status: v0.1.0-beta.** The project has been operated by its owner with a **JBD DP04S007-L4S 60A (4S, V2.1)** and **ESP32-C3 Zero**. The owner reports successful EEPROM APPLY and read-back verification on this hardware. This GitHub distribution has undergone static audits, **not** independent hardware qualification, exhaustive BMS-protection testing, or a local ESPHome compiler run. Do not infer compatibility with other JBD revisions.

## UART settings used in the published beta

The project maintainer reports that occasional UART parser warnings stopped after changing the following settings on their ESP32-C3 test device:

```yaml
logger:
  level: WARN
  hardware_uart: USB_SERIAL_JTAG

jbd_bms:
  id: bms0
  uart_id: jbd_uart
  update_interval: 5s
  rx_timeout: 300ms
```

These settings are applied to **both** firmware language variants. They reduce log output and polling frequency. The observed improvement does not independently establish the original cause of dropped UART frames. The RX observer used for EEPROM responses remains enabled.

## Features

- BMS telemetry: pack and cell-group voltages, current, power, capacity, temperature, protection flags, history counters.
- Discharge MOSFET control and status display.
- Independent **10-register EEPROM read** without writing parameters, and DRAFT vs EEPROM comparison (10/10).
- Protected configuration workflow: edit DRAFT → validate → review/ARM → APPLY → backup and read-back verification.
- Project preset and persistent custom profile; loading a profile changes **DRAFT only**.
- Two complete Home Assistant dashboards: **English** and **Українська**, six views each.

## Files

| File | Purpose |
|---|---|
| [`firmware/jbd-bms-ua.yaml`](firmware/jbd-bms-ua.yaml) | ESPHome firmware with Ukrainian runtime profile messages |
| [`firmware/jbd-bms-en.yaml`](firmware/jbd-bms-en.yaml) | Identical configuration logic with English runtime profile messages |
| [`dashboards/jbd-dashboard-en.yaml`](dashboards/jbd-dashboard-en.yaml) | English Home Assistant dashboard |
| [`dashboards/jbd-dashboard-uk.yaml`](dashboards/jbd-dashboard-uk.yaml) | Ukrainian Home Assistant dashboard |
| [`docs/INSTALL_EN.md`](docs/INSTALL_EN.md) | Setup walkthrough |
| [`docs/HARDWARE.md`](docs/HARDWARE.md) | UART pinout and electrical considerations |
| [`docs/CONFIGURATION.md`](docs/CONFIGURATION.md) | Parameters, profiles, EEPROM and status semantics |
| [`docs/COMPATIBILITY.md`](docs/COMPATIBILITY.md) | Versions and scope of verification |
| [`docs/TESTING.md`](docs/TESTING.md) | What is and is not validated |

## Quick start

1. Install Home Assistant + ESPHome Device Builder and ensure the external component can be downloaded.
2. Check **hardware compatibility** and UART electrical levels before wiring (see [HARDWARE](docs/HARDWARE.md)).
3. Copy one firmware YAML into the ESPHome configuration directory. **Copy `secrets.yaml.example` to `secrets.yaml` locally, supply Wi-Fi/API secrets, and never commit `secrets.yaml`.** ESPHome also supports existing shared secrets.
4. Validate and install the firmware with ESPHome. UART configuration in the example uses GPIO4 (ESP TX) and GPIO5 (ESP RX) at 9600 8N1.
5. Import one dashboard as a **complete raw Home Assistant dashboard configuration**. Both dashboard variants use identical entity IDs and may be switched without changing firmware.
6. Verify telemetry and press **Read All 10 EEPROM Parameters** in the EEPROM tab. After a restart, re-read before trusting the comparison.

> Language support: English and Ukrainian Home Assistant dashboards are available. Matching firmware variants provide localized status messages. Both variants use identical entity IDs and functionality.

### Secrets example

```yaml
wifi_ssid: "YOUR_SSID"
wifi_password: "YOUR_WIFI_PASSWORD"
jbd_bms__encryption_key: "YOUR_ESPHOME_API_ENCRYPTION_KEY"
```

Generate a proper ESPHome API encryption key locally or use your existing ESPHome-generated one. Never use these example placeholders as real credentials.

## Hardware compatibility

This example was built for **4S** JBD DP04S007-L4S 60A and a separate **ESP32-C3 Zero**. It is *not* a generic configuration for all JBD BMS devices, all UART headers, battery chemistries or pack sizes. UART header supply pins may have **battery-pack voltage**, not regulated 3.3 V or 5 V. Read [HARDWARE.md](docs/HARDWARE.md) before connecting anything.

The example project preset describes one pack; **the values are illustrative and must be checked against the actual cells, charger, UPS, current limits and BMS model**. See [CONFIGURATION.md](docs/CONFIGURATION.md).

## Third-party component and licensing

This project **uses but does not bundle** [`syssi/esphome-jbd-bms`](https://github.com/syssi/esphome-jbd-bms), which is provided under **Apache License 2.0**. Credit belongs to that project and its contributors. This repository's original configuration and dashboard materials are under the [MIT License](LICENSE). All upstream licensing remains intact.

The ESPHome `external_components` reference currently uses `@main`, which can change over time. For reproducibility, **pin the last verified upstream commit after testing it**; don't assume a future `main` revision will behave identically.

## Security and change control

- Never upload `secrets.yaml`, copied API keys, production Wi-Fi credentials, BMS serial identifiers or private Home Assistant backups to GitHub.
- Do not treat reported MOSFET states, BMS telemetry, or a successful EEPROM read-back as substitute for independent hardware protection verification.
- EEPROM APPLY is an explicit action, guarded by unlocking and a time-limited ARM operation. Neither dashboard switches nor profile buttons bypass this procedure.
- EEPROM writes can reset event counters on some protocol implementations. Save their values before reconfiguring.
- Configuration backups shown in the UI are diagnostic readings, not a durable off-device archive.

## Support the project

If this open-source project is useful, optional donations are appreciated. See [SUPPORT.md](SUPPORT.md) for current setup instructions. **No payment URL or crypto address is published until the maintainer provides and verifies it.** The prepared `.github/FUNDING.yml.example` is a template only; rename it to `.github/FUNDING.yml` after replacing sample entries with real URLs.

## Screenshots

See [`screenshots/README.md`](screenshots/README.md). Images are intentionally not included yet: take screenshots after installing the language-specific dashboard, and redact identifiers/network information before committing them.

## Contributing

Issues and pull requests are welcome. Include the BMS model and board revision, ESPHome version, platform, symptoms, and **redacted** logs. See [`CONTRIBUTING.md`](CONTRIBUTING.md). Detailed first-time GitHub publication instructions in Ukrainian are in [`docs/PUBLISH_STEP_BY_STEP_UA.md`](docs/PUBLISH_STEP_BY_STEP_UA.md).
