import time
from gps import GPS
from display import Display
from power import Power
from storage import load_mileage, save_mileage
from config import *

gps = GPS(GPS_PORT)
lcd = Display(LCD_ADDR)
power = Power(IGNITION_PIN)

miles = load_mileage()

last_lat = None
last_lon = None
last_saved = miles

screen = 0
last_switch = time.time()

def fake_distance(lat1, lon1, lat2, lon2):
    # simple approximation (good enough for MVP)
    return abs(lat1 - lat2) + abs(lon1 - lon2)

while True:

    gps.update()

    ign = power.ignition_on()

    # -------------------
    # STANDBY MODE
    # -------------------
    if not ign:
        lcd.set_backlight(False)

        if miles != last_saved:
            save_mileage(miles)
            last_saved = miles

        time.sleep(1)
        continue

    # -------------------
    # ACTIVE MODE
    # -------------------
    lcd.set_backlight(True)

    # distance calc (only if moving)
    if gps.speed_mph > MIN_SPEED_MPH:

        if last_lat is not None:
            d = fake_distance(last_lat, last_lon, gps.lat, gps.lon)

            if d > 0.01:  # filter GPS drift
                miles += d

    last_lat = gps.lat
    last_lon = gps.lon

    # save every 0.1 mile
    if miles - last_saved >= SAVE_INTERVAL_MILES:
        save_mileage(miles)
        last_saved = miles

    # -------------------
    # SCREEN SWITCHING
    # -------------------
    now = time.time()

    if now - last_switch > SCREEN_TIME:
        screen = (screen + 1) % 2
        last_switch = now

    # -------------------
    # DISPLAY LOGIC
    # -------------------
    if gps.fix == "NO DATA":
        lcd.screen_odometer(miles, "NO GPS")

    else:
        if screen == 0:
            lcd.screen_odometer(miles, gps.fix)

        else:
            lcd.screen_gps(
                gps.lat,
                gps.lon,
                gps.sats,
                gps.fix
            )