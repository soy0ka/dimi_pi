import RPi.GPIO as gpio
import time

buzzerPin = 4
gpio.setmode(gpio.BCM)
gpio.setup(buzzerPin, gpio.OUT)

pwm = gpio.PWM(buzzerPin,262)
pwm.start(10)

melody = [262,294,330,349,392,440,494,523]
do = melody[0]
rae = melody[1]
mi = melody[2]
fa = melody[3]
sol = melody[4]
la = melody[5]
ti = melody[6]
do_h = melody[7]

def buzzer (melody,wait):
    pwm.ChangeFrequency(melody)
    time.sleep(wait)
    pwm.ChangeFrequency(1)
    time.sleep(0.05)
try:
    buzzer(sol,0.45)
    buzzer(sol,0.45)
    buzzer(la,0.45)
    buzzer(la,0.45)    
    buzzer(sol,0.45)
    buzzer(sol,0.45)
    buzzer(mi,1)
    buzzer(sol,0.45)
    buzzer(sol,0.45)
    buzzer(mi,0.45)
    buzzer(mi,0.45)
    buzzer(rae,1)

    buzzer(sol,0.45)
    buzzer(sol,0.45)
    buzzer(la,0.45)
    buzzer(la,0.45)    
    buzzer(sol,0.45)
    buzzer(sol,0.45)
    buzzer(mi,1)

    buzzer(sol,0.45)
    buzzer(mi,0.45)
    buzzer(rae,0.45)
    buzzer(mi,0.45)
    buzzer(do,1)



finally:
    pwm.stop()
    gpio.cleanup()