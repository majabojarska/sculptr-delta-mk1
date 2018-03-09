This is a modified version of the generic Marlin-1.1.x firmware pulled from the original github repository.
It was set up to work with my build of Sculptr Delta MK1.
Might need a bit of tweaking to fully work with yours :) .

Hardware description:
- RAMPS 1.4 EFB
- RepRapDiscount FULL GRAPHIC Smart Controller
- 4xA4988 Stepper Drivers
- Normally closed (NC) endstops
- ATX PSU wired to power the hotend and heatbed from two separate channels
- E3Dv6 12V hotend
- MK6 220mm 12V circular heatbed with 4mm glass on top
- 100kOhm thermocouples
- Replaced heatbed MOSFET to IRLB3034 - more efficient, can handle higher loads easily with a small heatsink, generates much less heat
- OctoPrint hosted on Raspberry Pi 3 with a video stream
- 2x NeoPixel LEDs for print lighting
