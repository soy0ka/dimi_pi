# PIR (인체감지) 센서
import RPi.GPIO as gpio
import time

PIR_PIN = 4
gpio.setmode(gpio.BCM)
gpio.setup(PIR_PIN, gpio.IN)

time.sleep(5)
print("PIR Ready...")
try:
    while True:
        val gpio.input(PIR_PIN)
        if(val == 1):
            print("움직임 감지")
        else:
            print("움직임 없음")
        time.sleep(0.1)
finally:
    pwm.stop()
    gpio.cleanup()