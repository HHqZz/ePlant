
import constants as const
import gpio as gpio
import time
import serial    


def handle_signals():
    check_water()
    check_temperature()

def check_water():
    water_level = read_uno()
    if water_level<const.WATER_TH:
        en_gpio(3,const.GPIO_PUMP) #Should be calculated depending on the uno value

def check_temperature():
    temperature_level = READUNO()
    if temperature_level<const.TEMPERATURE_TH:
        en_gpio(3,const.GPIO_FAN) #Should be calculated depending on the uno value

def en_gpio(t, gpio_port):
    gpio.turn_on(gpio_port)
    time.sleep(t)
    gpio.turn_off(gpio_port)

def read_uno():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5) # open serial port with 5s timeout
    while(1):
        msg = ser.readline().decode('utf-8')
        array = (msg.rstrip()).split(":") # retire la nouvelle ligne puis sépare l'identifiant de la valeur
    if array[0] == "TEMP":
        print(array[1] + "°C")
    elif array[0] == "HUMI":
        print(array[1] + "%")
    elif array[0] == "MOIS":
        print(array[1] + " (sans unitée)")

    ser.close()    
