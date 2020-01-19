import RPi.GPIO as GPIO
import time
import constants as const
import context as context

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def turn_on(GPIO_NO):
	if(GPIO_NO == const.GPIO_FAN):
		context.fan = True
	if(GPIO_NO == const.GPIO_LIGHT):
		context.light = True
	if(GPIO_NO == const.GPIO_PUMP):
		context.pump = True
	GPIO.setup(GPIO_NO, GPIO.OUT)
	GPIO.output(GPIO_NO,True)

def turn_off(GPIO_NO):
	if(GPIO_NO == const.GPIO_FAN):
		context.fan = False
	if(GPIO_NO == const.GPIO_LIGHT):
		context.light = False
	if(GPIO_NO == const.GPIO_PUMP):
		context.pump = False
	GPIO.setup(GPIO_NO, GPIO.OUT)
	GPIO.output(GPIO_NO,False)
