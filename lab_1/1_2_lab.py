import RPi.GPIO as GPIO
import time as tm
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
for i in range(100):
    if i % 2 == 0:
        GPIO.output(19, 1)
    else:
        GPIO.output(19, 0)
    tm.sleep(0.5)
