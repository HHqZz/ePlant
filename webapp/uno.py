
import constants as const

def handle_signals():
    check_water()
    check_temperature()
    check_humidity()

def check_water():
    water_level = READUNO()
    if water_level<const.WATER_TH:
        en_pump()



def check_temperature():
    light_level = READUNO()
    if light_level<const.LIGHT_TH:
        en_fan()


def check_humidity():
    humidity_level=READUNO()

