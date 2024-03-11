import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(19, GPIO.IN)
GPIO.output(25, GPIO.input(19))


