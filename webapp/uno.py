
import constants as const
import gpio as gpio
import time
from readSerial import read    
from _thread import start_new_thread


def start():
	start_new_thread(anepasrefairechezvous,())

def handle_signals():
	start_new_thread(check_water,())
	start_new_thread(check_temperature,())

def check_water():
    f = open("water.txt", "r")
    water_level = float(f.read())
    print(water_level)
    if water_level<const.WATER_TH:
        en_gpio(3,const.GPIO_PUMP) #Should be calculated depending on the uno value

def check_temperature():
    f = open("temperature.txt", "r")
    temperature_level = float(f.read())
    print(temperature_level)
    if temperature_level<const.TEMPERATURE_TH:
        en_gpio(3,const.GPIO_FAN) #Should be calculated depending on the uno value

def en_gpio(t, gpio_port):
    gpio.turn_on(gpio_port)
    time.sleep(t)
    gpio.turn_off(gpio_port)
    
def anepasrefairechezvous():
	while(1):
		handle_signals()
		time.sleep(10)

#def read_uno():
   # serial.read()
