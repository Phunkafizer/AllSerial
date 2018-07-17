# AllSerial
An universal open source USB-serial converter for RS232, RS485, RS232, TTL, TTY current loop, mBus

## Features
- Isolated
- Reset button for reenumerating device on the USB
- Status LEDs
- modular, just exchange daughterboard for different interfaces

# Modules
## 1A Mainboard FT232
![PCB](./1_MAIN/1_MAIN_SCHEM.png)
![PCB](./1_MAIN/1_MAIN_BOARD.png)
![Front panel](./1_MAIN/FRONT.svg)
* Isolated between controller and daughterboards
* pin header for connecting logicanalyer

## 2 RS422/RS485
![PCB](./2_RS485_RS422/2_RS485_RS422_SCHEM.png)
![PCB](./2_RS485_RS422/2_RS485_RS422_BOARD.png)
![Front panel](./2_RS485_RS422/FRONT.svg)
* Jumper for termination
* Second doublepait for RS422 with handshake lines

## 3 RS232
![PCB](./3_RS232/PCB.png)
![Front panel](./3_RS232/FRONT.svg)
* Full connection: TXD, RXD, CTS, RTS, DTR, DSR, DCD, RI
* 9 pin Sub-D male connector

## 4 TTL
![PCB](./4_TTL/PCB.png)
![Front panel](./4_TTL/FRONT.svg)
* Full connection: TXD, RXD, CTS, RTS, DTR, DSR, DCD, RI
* Selectable voltage 5 V, 3.3 V, external

## 5 Current loop (TTY)
![PCB](./5_TTY/PCB.png)
![Front panel](./5_TTY/FRONT.svg)
* Jumper for mode (2/3/4-wire, passiv/active)
* Jumper for currentselection (20 mA / 40 mA)

## 6 LIN
![PCB](./6_LIN/PCB.png)
![Front panel](./6_LIN/FRONT.svg)
* Jumper for master

## 7 mBus master

# Device notes
Housing: Fischer AKG 71 24 100 ME
Mainboard LEDs Mentor 1296.1004
