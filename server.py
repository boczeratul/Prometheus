from flask import Flask
from flask import render_template
from multiprocessing import Pool

# import alarm
import light
import danboard
import common
import logging

app = Flask(__name__)
pool = Pool()

state = 'rest'

@app.route("/alarm")
def alarm_page():
    common.play_mp3('./assets/warning_1.mp3')
    light.start_alarm()
    logging.warning('Alarm!')
    return "Alarm sent!"

@app.route("/portal")
def r2d2():
    common.play_mp3('./assets/portal.wav')
    light.start_speak()
    return "R2D2"

@app.route("/")
def index_page():
    logging.warning('Index!')
    return render_template('index.html')

if __name__ == "__main__":
    pool.apply_async(danboard.danboard, [])
    app.run(host='0.0.0.0')