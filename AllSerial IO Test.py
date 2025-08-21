import serial
import serial.tools.list_ports
import time
import threading

ports = serial.tools.list_ports.comports()
ser = serial.Serial()
ser.baudrate = 19200
ser.timeout = 0.1

class RxThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global ser
        try:
            cts = ser.cts
            dsr = ser.dsr
            ri = ser.ri
            dcd = ser.cd
            while True:
                rx = ser.read(255)
                if len(rx) > 0:
                    print(F"RX: {rx}")

                if (cts != ser.cts):
                    cts = not cts
                    print(F"CTS -> {cts}")

                if (dsr != ser.dsr):
                    dsr = not dsr
                    print(F"DSR -> {dsr}")

                if (ri != ser.ri):
                    ri = not ri
                    print(F"RING -> {ri}")

                if (dcd != ser.cd):
                    dcd = not dcd
                    print(F"DCD -> {dcd}")

        except Exception as e:
            print("RX:", e)
            return
        

class TxThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global ser
        i = 0
        print("Starting TX")
        while True:
            try:
                ser.write(b"ABCDEFGH\r\n")
                ser.rts = i == 1
                ser.dtr = i == 3
                i += 1
                if i == 4:
                    i = 0
            except Exception as e:
                print("TX:", e)
                del self
                return
            time.sleep(0.5)

while True:
    time.sleep(0.25)
    newports = serial.tools.list_ports.comports()
    if newports != ports:
        for newport in newports:
            if not newport in ports:
                print(F"Device new: {newport.device}")
                if not ser.is_open:
                    print(F"Opening {newport.device}")
                    ser.port = newport.device
                    ser.open()
                    txthread = TxThread()
                    txthread.start()
                    rxthread = RxThread()
                    rxthread.start()
                break

        for port in ports:
            if not port in newports:
                print("device left", port.device)
                if ser.is_open and ser.port == port.device:
                    print(F"Closing {ser.port}")
                    ser.close()

        ports = newports

ser.close()
rxthread.join()
txthread.join()
