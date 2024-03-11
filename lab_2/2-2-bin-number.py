import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac_pins = [8, 11, 7, 1, 0, 5, 12, 6]
number_pins = len(dac_pins)
number = bin(0)[2:].zfill(number_pins)

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac_pins, GPIO.OUT)
    for i in range(number_pins):
        GPIO.output(dac_pins[i], int(number[i]))
    
    time.sleep(10)

finally:
    GPIO.output(dac_pins, GPIO.LOW)

    GPIO.cleanup()
