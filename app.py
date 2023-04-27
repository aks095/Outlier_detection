from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
import pandas as pd
from time import time
import random
from flask import Flask, render_template, make_response
app = Flask(__name__)

data=pd.read_json("http://www.qts.iitkgp.ac.in/last/1/100")
column=['Board_id','Humidity','Mac_id','Reading_id','Temperature','Time','co2ppm','ethylene1']
df=pd.DataFrame(data,columns=column)
temp_df = df["Temperature"].tolist()
humid_df = df["Humidity"].tolist()

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
#for x1 in range(100):
def data():
    # Data Format
    # [TIME, Temperature, Humidity]
    x1 = random.randint(0,99)

    Temperature = temp_df[x1]

    Humidity = humid_df[x1]

    out_temp = 28
    out_hum = (20 * 100) // Temperature
    data = [time() * 1000, Temperature, Humidity, out_temp, out_hum]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response

# data()
if __name__ == "__main__":
    app.run(debug=True)

