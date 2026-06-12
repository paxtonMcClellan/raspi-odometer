class Health:
    def __init__(self):
        self.gps = "NO DATA"
        self.display = "OK"
        self.storage = "OK"
        self.power = "UNKNOWN"

    def gps_status(self, gps):
        if gps.fix == "NO DATA":
            return "NO GPS"
        return gps.fix
    