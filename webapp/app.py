from flask import Flask, render_template, jsonify
# from led import blinkLed
import constants as const
from uno import start
from _thread import start_new_thread
from readSerial import read
import gpio as gpio
import json
import context
import uno
 


start_new_thread(read,())
start()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/light')
def light():
    if context.light:
        gpio.turn_off(const.GPIO_LIGHT)
    else:
        gpio.turn_on(const.GPIO_LIGHT)
    return render_template('index.html')


@app.route('/info')
def infos():
    f = open("humidite.txt", "r")
    context.humidity = float(f.read())
    #json qui renvoie les infos sur light fan humidite ground wet
    return  jsonify({'fan':context.fan,'pump':context.pump,'light':context.light,'humidity':context.humidity})

#fan switch
@app.route('/fan')
def fan():
    if context.fan:
        gpio.turn_off(const.GPIO_FAN)
    else:
        gpio.turn_on(const.GPIO_FAN)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
 
