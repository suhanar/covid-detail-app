from flask import Flask,request,render_template,jsonify
import requests
import json
app = Flask(__name__)

import requests

url = "https://covid-193.p.rapidapi.com/countries"

headers = {
    'x-rapidapi-host': "HOST",
    'x-rapidapi-key': "KEY"
    }

response = requests.request("GET", url, headers=headers)








@app.route('/')
def home():
    if response.status_code == 200:
        res1 = json.loads(response.content.decode('utf-8'))



        return res1
    else:
        return 'none'




if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)
