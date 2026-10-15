# Hardware and wiring

## Verified example setup (owner-reported)

| Item | Tested setup |
|---|---|
| BMS | JBD DP04S007-L4S 60A; board revision V2.1 |
| Pack | 4S4P LiFePO₄, 4 series groups, 60 Ah nominal |
| MCU | ESP32-C3 Zero, ESP-IDF framework |
| UART | 9600 baud, 8 data bits, no parity, 1 stop bit |
| ESP TX | GPIO4 → BMS RX |
| ESP RX | GPIO5 ← BMS TX |
| GND | Reference connected only after checking manufacturer pinout and electrical design |
| Supply | A separate correctly regulated supply for ESP32 |

**Important:** A UART/header connector on a BMS may expose **full pack voltage** on a pin labeled VDD. Never connect a BMS header's VDD directly to ESP32 3.3 V or 5 V. Confirm the exact pin function, voltage, common reference and UART voltage levels with suitable instruments and manufacturer documents for your board revision. Use an appropriate level shifter or isolation if required.

ESPHome GPIO pins are **ESP-side pins**, not labels on the BMS connector. Two BMS board revisions may use different connector arrangements even with similar names. The connector voltage and pin order are not guaranteed by this repository.

## System power/current sizing

The BMS current rating and wire/contact/connector ratings must match the actual charge and discharge current. For example, a 12 V UPS inverter of roughly 1 kW may demand well over 60 A on its DC side once losses and battery voltage under load are considered. Select hardware and protection to match the true operating envelope.

This repository does not provide a battery pack construction guide or hardware-protection validation. Do not assume a normal HA telemetry value proves that a cutoff or MOSFET is electrically safe.
