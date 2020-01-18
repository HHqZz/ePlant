from flask import Flask, render_template
from led import blinkLed

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led')
def led():
    blinkLed()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')