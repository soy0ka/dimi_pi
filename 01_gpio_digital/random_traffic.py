import RPi.GPIO as gpio
import time
import random

red = 4
yellow = 17
green = 27
gpio.setmode(gpio.BCM)
gpio.setup(red, gpio.OUT)
gpio.setup(yellow, gpio.OUT)
gpio.setup(green, gpio.OUT)

for i in range(100000):
    gpio.output(red, 1)
    print("red on")
    time.sleep(random.randrange(1,300)/1500)
    gpio.output(red, 0)
    print("red off\nyellow on")
    gpio.output(yellow, 1)
    time.sleep(random.randrange(1,300)/1500)
    gpio.output(yellow, 0)
    print("yellow off\ngreen on")
    gpio.output(green, 1)
    time.sleep(random.randrange(1,300)/1500)
    print("green off")
    gpio.output(green,0)
