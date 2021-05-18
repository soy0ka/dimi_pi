import RPi.GPIO as GPIO
import time

LED_PIN_ONE = 4
LED_PIN_TWO = 5
LED_PIN_THREE = 6
SWITCH_PIN_ONE = 9
SWITCH_PIN_TWO = 10
SWITCH_PIN_THREE = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN_ONE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_TWO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_THREE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN_ONE, GPIO.OUT)
GPIO.setup(LED_PIN_TWO, GPIO.OUT)
GPIO.setup(LED_PIN_THREE, GPIO.OUT)

try:
    while True:
        val1 = GPIO.input(SWITCH_PIN_ONE)
        val2 = GPIO.input(SWITCH_PIN_TWO)
        val3 = GPIO.input(SWITCH_PIN_THREE)
        GPIO.output(LED_PIN_ONE,val1)
        GPIO.output(LED_PIN_TWO,val2)
        GPIO.output(LED_PIN_THREE,val3)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')
