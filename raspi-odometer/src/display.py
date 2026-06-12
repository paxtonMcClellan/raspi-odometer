from RPLCD.i2c import CharLCD

class Display:
    def __init__(self, addr):
        self.lcd = CharLCD('PCF8574', addr)
        self.backlight = True
        # cache for last-written lines to avoid flicker
        self.rows = getattr(self.lcd, 'rows', 2)
        self.cols = getattr(self.lcd, 'cols', 20)
        self.last_lines = [""] * self.rows

    def clear(self):
        self.lcd.clear()
        self.last_lines = [""] * self.rows

    def set_backlight(self, state):
        self.backlight = state
        if state:
            self.lcd.backlight_enabled = True
        else:
            self.lcd.backlight_enabled = False

    def screen_odometer(self, miles, fix):
        line0 = f"{miles:.1f} MI"
        line1 = f"GPS:{fix}"
        self._write_line(0, line0)
        self._write_line(1, line1)

    def screen_gps(self, lat, lon, sats, fix):
        line0 = f"S{sats} {fix}"
        line1 = f"{lat:.4f} {lon:.4f}"
        self._write_line(0, line0)
        self._write_line(1, line1)

    def _write_line(self, row, text):
        # pad/truncate to overwrite previous content and avoid leftover chars
        padded = text.ljust(self.cols)[:self.cols]
        if self.last_lines[row] != padded:
            self.lcd.cursor_pos = (row, 0)
            self.lcd.write_string(padded)
            self.last_lines[row] = padded