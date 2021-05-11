import RPi.GPIO as gpio
import time

ledPin = 4
gpio.setmode(gpio.BCM)
gpio.setup(ledPin, gpio.OUT)

for i in range(100000):
    gpio.output(ledPin, 1)
    print("led on")
    time.sleep(0.02)
    gpio.output(ledPin, 0)
    print("led off")
    time.sleep(0.02)
