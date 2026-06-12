import RPi.GPIO as GPIO
import time

class Power:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)

    def ignition_on(self):
        return GPIO.input(self.pin) == 1