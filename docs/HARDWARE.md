# Hardware and wiring

## Verified example setup (owner-reported)

| Item | Tested setup |
|---|---|
| BMS | JBD DP04S007-L4S 60A; board revision V2.1 |
| Pack | 4S4P LiFePO₄, 4 series groups, 60 Ah nominal |
| External active balancer | ZNLD DJ ETA 9000 Rev 2.0 (2 A class, owner-reported), used independently of the JBD BMS |
| MCU | ESP32-C3 Zero, ESP-IDF framework |
| UART | 9600 baud, 8 data bits, no parity, 1 stop bit |
| ESP TX | GPIO4 → BMS RX |
| ESP RX | GPIO5 ← BMS TX |
| ESP32 power source | Battery-side **B+** and **B−** → DC-DC buck converter → regulated 5 V ESP32 supply input |
| UART ground | Verify the UART header's signal reference and its relation to B− before connection |

## ESP32 power supply

The tested ESP32-C3 Zero is powered from the battery's **B+ and B− terminals via a DC-DC step-down (buck) converter**. The ESP32 does **not** take its supply voltage from the BMS UART VDD pin or from the UPS output.

```text
Battery / BMS battery-side terminals:
  B+ ── appropriately rated fuse ──> DC-DC buck VIN+
  B− ─────────────────────────────> DC-DC buck VIN−

Regulated DC-DC output:
  +5 V ──> ESP32-C3 Zero designated 5 V power input
  GND  ──> ESP32-C3 Zero power GND

JBD UART (ESP32-side GPIO labels):
  BMS TX ──> ESP32 GPIO5 (RX)
  BMS RX <── ESP32 GPIO4 (TX)
  BMS UART GND ──> appropriate signal reference after verification
```

Choose a DC-DC converter rated for the entire 4S LiFePO₄ voltage range, including the maximum charge voltage, and with enough output current for ESP32-C3 Wi-Fi peaks. Confirm the converter's regulated 5 V output using a multimeter before connecting the ESP32. Protect and insulate the battery-side converter wiring; these conductors can stay live even when the BMS discharge MOSFET is off.

**Important grounding distinction:** B− is the battery-side negative terminal; P− (if provided) is the BMS-controlled negative terminal for external equipment. Do not unintentionally bridge B− to P− through the buck converter, UART signal ground, USB cable, computer, or any other connected device. Verify the BMS UART signal reference, ESP32 power arrangement, and any USB connection; use appropriate galvanic isolation where required.

## UART connector and logic levels

A UART/header connector on a BMS may expose **full pack voltage** on a pin labeled VDD. Never connect a BMS header's VDD directly to ESP32 3.3 V or 5 V. Confirm the exact pin function, voltage, signal reference, and UART voltage levels with suitable instruments and manufacturer documentation for your board revision. Use an appropriate level shifter or isolation where required.

ESPHome GPIO pins are **ESP-side pins**, not labels on the BMS connector. Two BMS board revisions may use different connector arrangements even with similar names. The connector voltage and pin order are not guaranteed by this repository.

## External active cell balancer

The tested battery assembly also includes an **external ZNLD DJ ETA 9000 Rev 2.0 active balancer** (described by the owner as a **2 A** model). It is a separate device connected to the battery's four series cell groups; it is **not controlled or configured by this ESPHome project**.

- The JBD BMS provides cell monitoring, protection, and its own built-in **passive** balancing function.
- The ZNLD unit performs **active** cell-group balancing independently of the JBD BMS and ESP32.
- The Home Assistant **Balancing / Balancing Cells** indicators reflect **JBD-reported passive balancing**, **not** the ZNLD unit's activity.
- The external active balancer is **optional** for running the JBD ESPHome configurator. A compatible 4S balancer must be wired according to its own pinout and documentation, with appropriately protected balance leads.

The exact balancing current and supported operating voltage should be confirmed against the specific ZNLD hardware documentation; the 2 A figure above is the installation's reported rating, not a value measured by ESPHome.

## System power/current sizing

The BMS current rating and wire/contact/connector ratings must match the actual charge and discharge current. For example, a 12 V UPS inverter of roughly 1 kW may demand well over 60 A on its DC side once losses and battery voltage under load are considered. Select hardware and protection to match the true operating envelope.

This repository does not provide a battery pack construction guide or hardware-protection validation. Do not assume a normal HA telemetry value proves that a cutoff or MOSFET is electrically safe.
