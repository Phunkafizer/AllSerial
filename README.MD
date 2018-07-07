# AllSerial
An universal USB-serial converter

## Features
- Isolated
- Reset button
- Status LEDs

# Modules
## 1 Mainboard FT232
![Alt text](./Housing/1_Main.svg)
<img src="./Housing/1_Main.svg">
* Isolated between controller and daughterboards
* pin header for connecting logicanalyer

## 2 RS422/RS485
* Jumper for termination
* Second doublepait for RS422 with handshake lines

## 3 RS232
* Full connection: TXD, RXD, CTS, RTS, DTR, DSR, DCD, RI
* 9 pin Sub-D male connector

## 4 TTL
* Full connection: TXD, RXD, CTS, RTS, DTR, DSR, DCD, RI
* Selectable voltage 5 V, 3.3 V, external

## 5 Current loop (TTY)
* Jumper for mode (2/3/4-wire, passiv/active)
* Jumper for currentselection (20 mA / 40 mA)

## 6 LIN
* Jumper for master

# Device notes
Profilgehäuse Fischer AKG 71 24 100 ME
leds Mentor 1296.1004 Lichtleiter für 0805










Daughterboards:
- TTL mit 10 pol Stecker, 4 pol mit GND, 3,3, 5 und 12
- RS232 10 pol mit 8 Daten, GND, 5 V, oder auch 4 pol?
- RS422 / 485, Term schaltbar, Handshake wählbar
- Current Loop, 5 pol Stecker, an Front jumperbar?