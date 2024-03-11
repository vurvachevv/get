import RPi.GPIO as GPIO
import time
leds_pins = [2, 3, 4, 17, 27, 22, 10,9]
aux_pins = [21, 20, 26, 16, 19, 25, 23, 24]

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(leds_pins, GPIO.OUT)
    GPIO.setup(aux_pins, GPIO.IN)

    while True:
        for i in range(len(leds_pins)):
            if GPIO.input(aux_pins[i]) == GPIO.LOW:
                GPIO.output(leds_pins[i], GPIO.LOW)
            else:
                GPIO.output(leds_pins[i], GPIO.HIGH)
        time.sleep(0.2)

finally:
    GPIO.output(leds_pins, GPIO.LOW)
    GPIO.cleanup()
            