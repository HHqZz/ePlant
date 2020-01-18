import RPi.GPIO as GPIO
import time

def turn_on(GPIO_NO):
	
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(GPIO_NO, GPIO.OUT)

	GPIO.output(GPIO_NO,True)


turn_on(23)
