from flask import Flask
from flask import request
import datetime
app = Flask(__name__)

logs = []

@app.route("/send")
def send():
    global logs
    cur_time = datetime.datetime.now()
    logs.append(cur_time)
    return "sent"

@app.route("/")
def read():
    global logs
    ret = '[*] Motion Detection Log'
    for time in logs:
        ret += str(time)
        ret += "\n"
    return ret