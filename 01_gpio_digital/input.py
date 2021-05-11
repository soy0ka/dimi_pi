import RPi.GPIO as gpio
import time

ledPin = 4
gpio.setmode(gpio.BCM)
gpio.setup(ledPin, gpio.OUT)

try:
    while 1:
        print("0 : off 1 : on 9 : exit")
        a = input()
        if a == '0':
            gpio.output(ledPin, 0)
            print("Led off")
        elif a=='1':
            gpio.output(ledPin, 1)
            print("Led on")
        elif a=='9':
            gpio.cleanup()
            exit()
        else:
            print("지원하지 않는 숫자입니다")
finally:
    gpio.cleanup()
