# AllSerial
An universal USB-serial converter

## Features
- Isolated
- Reset button
- Status LEDs

# Modules
## 1 Mainboard FT232
![PCB](./1_MAIN/PCB.png)
![Front panel](./1_Main/FRONT.svg)
* Isolated between controller and daughterboards
* pin header for connecting logicanalyer

## 2 RS422/RS485
![PCB](./2_RS485_RS422/PCB.png)
![Front panel](./2_RS422_485/FRONT.svg)
* Jumper for termination
* Second doublepait for RS422 with handshake lines

## 3 RS232
![PCB](./3_RS232/PCB.png)
![Front panel](./3_RS232/FRONT..svg)
* Full connection: TXD, RXD, CTS, RTS, DTR, DSR, DCD, RI
* 9 pin Sub-D male connector

## 4 TTL
![PCB](./4_TTL/PCB.png)
![Front panel](./4_TTL/FRONT.svg)
* Full connection: TXD, RXD, CTS, RTS, DTR, DSR, DCD, RI
* Selectable voltage 5 V, 3.3 V, external

## 5 Current loop (TTY)
![PCB](./PCB/5_TTY.png)
![Front panel](./5_TTY/FRONT.svg)
* Jumper for mode (2/3/4-wire, passiv/active)
* Jumper for currentselection (20 mA / 40 mA)

## 6 LIN
![PCB](./PCB/6_LIN.png)
![Front panel](./6_LIN/FRONT.svg)
* Jumper for master

# Device notes
Housing: Fischer AKG 71 24 100 ME
Mainboard LEDs Mentor 1296.1004
