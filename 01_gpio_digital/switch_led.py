import RPi.GPIO as GPIO
import time

LED_PIN = 4
SWITCH_PIN = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN,val)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')
