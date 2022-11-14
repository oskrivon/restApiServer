from flask import Flask
import json
import pandas as pd
from datetime import datetime
import random


app = Flask(__name__)

@app.route("/servertime", methods=['GET'])
def index():
    time = {"server_time": str(datetime.utcnow())}
    return json.dumps(time)


@app.route("/screening", methods=['GET'])
def index2():
    screenings = []
    with open('ex.json') as f:
        screenings.append(json.load(f))
    with open('ex2.json') as f:
        screenings.append(json.load(f))
    #hash = random.getrandbits(128)
    random_index = random.randint(0, len(screenings) - 1)
    #screening["hash"] = hash
    return json.dumps(screenings[random_index])


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="85.193.94.150", port=1212)
    #serve(app, host="127.0.0.1", port=1212)