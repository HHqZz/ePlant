import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_NO, GPIO.OUT)

def turn_on(GPIO_NO):

	GPIO.output(GPIO_NO,True)

def turn_off(GPIO_NO):

	GPIO.output(GPIO_NO,False)

turn_on(23)
sleep(1)
turn_off(23)