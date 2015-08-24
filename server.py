from flask import Flask
from flask import render_template
from multiprocessing import Pool

import alarm
import light
import danboard
import logging

app = Flask(__name__)
pool = Pool()

@app.route("/alarm")
def alarm_page():
    #pool.apply_async(alarm.alarm_mp3, [])
    #pool.apply_async(light.light, [])
    alarm.alarm_mp3_with_light('./assets/warning_1.mp3')
    logging.warning('Alarm!')
    return "Alarm sent!"

@app.route("/r2d2")
def alarm_page():
    alarm.alarm_mp3_with_light('./assets/r2d2_01.mp3')
    return "R2D2"

@app.route("/")
def index_page():
    logging.warning('Index!')
    return render_template('index.html')

if __name__ == "__main__":
    pool.apply_async(danboard.danboard, [])
    app.run(host='0.0.0.0')