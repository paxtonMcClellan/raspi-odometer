from RPLCD.i2c import CharLCD

class Display:
    def __init__(self, addr):
        self.lcd = CharLCD('PCF8574', addr)
        self.backlight = True

    def clear(self):
        self.lcd.clear()

    def set_backlight(self, state):
        self.backlight = state
        if state:
            self.lcd.backlight_on()
        else:
            self.lcd.backlight_off()

    def screen_odometer(self, miles, fix):
        self.lcd.clear()
        self.lcd.write_string(f"{miles:.1f} MI")
        self.lcd.cursor_pos = (1, 0)
        self.lcd.write_string(f"GPS:{fix}")

    def screen_gps(self, lat, lon, sats, fix):
        self.lcd.clear()
        self.lcd.write_string(f"S{sats} {fix}")
        self.lcd.cursor_pos = (1, 0)
        self.lcd.write_string(f"{lat:.4f} {lon:.4f}")