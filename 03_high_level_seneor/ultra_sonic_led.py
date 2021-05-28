import RPi.GPIO as gpio
import time

TRIGGER_PIN = 4
ECHO_PIN = 14
LED_PIN = 5
gpio.setmode(gpio.BCM)
gpio.setup(TRIGGER_PIN, gpio.OUT)
gpio.setup(LED_PIN, gpio.OUT)
gpio.setup(ECHO_PIN, gpio.IN)

try:
    while True:
        gpio.output(TRIGGER_PIN, 1)
        time.sleep(0.00001)
        gpio.output(TRIGGER_PIN, 0)

        while gpio.input(ECHO_PIN) == 0:
            pass
        start = time.time()

        while gpio.input(ECHO_PIN) == 1:
            pass
        stop = time.time()

        duration_time = stop - start
        distance = 17160 * duration_time
        print('distance: %.1fcm' %distance )
        if distance <= 20:
            gpio.output(LED_PIN,1)
            print('LED ON')
        else:
            gpio.output(LED_PIN,0)
            print('LED OFF')
        time.sleep(0.1)
finally:
    pwm.stop()
    gpio.cleanup()