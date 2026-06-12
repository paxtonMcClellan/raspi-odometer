import serial
import pynmea2
import time

class GPS:
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port, 9600, timeout=1)

        self.lat = 0.0
        self.lon = 0.0
        self.speed_mph = 0.0
        self.sats = 0
        self.fix = "NO DATA"

    def update(self):
        try:
            line = self.ser.readline().decode(errors='ignore')

            if line.startswith('$GPGGA') or line.startswith('$GPRMC'):
                msg = pynmea2.parse(line)

                if hasattr(msg, 'latitude') and msg.latitude:
                    self.lat = msg.latitude
                    self.lon = msg.longitude

                if hasattr(msg, 'num_sats'):
                    self.sats = int(msg.num_sats)

                if hasattr(msg, 'spd_over_grnd'):
                    self.speed_mph = float(msg.spd_over_grnd) * 1.15078

                if hasattr(msg, 'gps_qual'):
                    if msg.gps_qual == 0:
                        self.fix = "NO FIX"
                    elif msg.gps_qual == 1:
                        self.fix = "2D FIX"
                    else:
                        self.fix = "3D FIX"

        except Exception:
            self.fix = "NO DATA"