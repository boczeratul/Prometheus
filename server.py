from flask import Flask
from multiprocessing import Pool

import alarm
import light
import logging

app = Flask(__name__)
pool = Pool()

@app.route("/alarm")
def hello():
    pool.apply_async(alarm.alarm, [])
    pool.apply_async(light.light, [])
    logging.warning('Alarm!')
    return "Alarm sent!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')