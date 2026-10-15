# Hardware and wiring

## Tested setup

| Component | Configuration |
|---|---|
| BMS | JBD DP04S007-L4S 60A, PCB V2.1 (4S) |
| Battery | 4S4P LiFePO₄, 60 Ah nominal |
| Controller | ESP32-C3 Zero, ESP-IDF |
| Power | Battery-side **B+ / B−** → DC-DC buck converter → regulated **5 V** to ESP32 |
| Active balancer | External **ZNLD DJ ETA 9000 Rev 2.0**, 2 A class (reported rating) |
| UART | 9600 baud, 8N1, ESP TX GPIO4 → JBD RX, ESP RX GPIO5 ← JBD TX |

## Power and UART connections

```text
Battery-side B+ ── suitably rated fuse ──> Buck VIN+
Battery-side B− ─────────────────────────> Buck VIN−
Buck 5 V  ───────────────────────────────> ESP32 designated 5 V input
Buck GND  ───────────────────────────────> ESP32 power GND

JBD UART TX ─────────────────────────────> ESP32 GPIO5 (RX)
JBD UART RX <──────────────────────────── ESP32 GPIO4 (TX)
JBD UART reference ────────────────────── ESP32 signal reference (verify pinout)
```

The ESP32 is powered from the **battery through the buck converter**, not from the JBD UART header or UPS output. Choose a converter suitable for the full pack-voltage range and ESP32 Wi-Fi current peaks. Measure its regulated 5 V output before connecting the board. Protect battery-side wiring against shorts.

**Electrical reference:** B− (battery-side negative) and P− (BMS-controlled output negative) are **not interchangeable**. Avoid unintended B−–P− bridges via the buck converter, UART ground, USB cable or other equipment. Verify the board's UART signal levels and reference; use level shifting or isolation where necessary. A header pin marked **VDD may carry full pack voltage** — never assume it is an ESP32-safe supply rail.

## External active balancer

The external **ZNLD DJ ETA 9000 Rev 2.0** performs active balancing independently of the JBD BMS and ESP32. The BMS also has built-in **passive balancing**. Home Assistant's **Balancing** indicators report JBD's passive-balancing state, **not** ZNLD activity. The external balancer is optional for using this ESPHome project. The reported 2 A specification has not been independently measured by this firmware.

## Current limits

Select BMS, wiring, fuses, connectors and UPS load within their actual current ratings. A 12 V, roughly 1 kW inverter may draw significantly more than 60 A from its battery under load. Telemetry alone does not validate protection hardware.
