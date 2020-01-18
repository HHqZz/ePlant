
import constants as const
import gpio as gpio
import time
from readSerial import read    


def handle_signals():
    check_water()
    check_temperature()

def check_water():
    water_level = 200
    if water_level<const.WATER_TH:
        en_gpio(3,const.GPIO_PUMP) #Should be calculated depending on the uno value

def check_temperature():
    temperature_level = 200
    if temperature_level<const.TEMPERATURE_TH:
        en_gpio(3,const.GPIO_FAN) #Should be calculated depending on the uno value

def en_gpio(t, gpio_port):
    gpio.turn_on(gpio_port)
    time.sleep(t)
    gpio.turn_off(gpio_port)

#def read_uno():
   # serial.read()
