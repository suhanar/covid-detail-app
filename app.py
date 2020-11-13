
from flask import Flask,request,render_template,jsonify
import requests
import json
app = Flask(__name__)

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "HOST",
    'x-rapidapi-key': "KEY"
    }
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/result',methods=['POST','GET'])
def home_country():
    lst=[]
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        res=json.loads(response.content.decode('utf-8'))
        return(res)


        #return(res['response'][1]['continent'])
    else:
        return None









    '''if request.method == 'POST':
        result = request.form
        cou = result['country']





        return render_template('result.html',cou=cou,res=res)'''




@app.route('/covid')
def postt_covid():
    response = requests.request("GET", url, headers=headers)

    return (response.text)



if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)

