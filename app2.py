from flask import Flask,request,render_template,jsonify
import requests
import json
from countries import countries

app = Flask(__name__)



url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "HOST",
    'x-rapidapi-key': "KEY"
    }
@app.route('/')
def home():
    lst=[]
    for key in countries.keys():
        lst.append(key)
        country=sorted(lst)


    return render_template('home.html',country=country)
@app.route('/result',methods=['POST','GET'])
def home_country():

    if request.method=='POST':
        result = request.form
        #resu = result['country']
        res = result['country']

        #return res
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            res1 = json.loads(response.content.decode('utf-8'))
            for key,value in countries.items():

                if res == key:
                    ret=countries[res]
                    data=res1['response'][ret]
                    continent = data['continent']
                    day = data["day"]
                    recovered=data['cases']['recovered']
                    total = data['cases']['total']
                    active = data['cases']['active']
                    deaths = data['deaths']['total']
                    print(recovered)
                    return render_template('result.html',recovered=recovered,total=total,res=res,continent=continent,active=active,day=day,deaths=deaths)


        else:
            return('none')















@app.route('/covid')
def postt_covid():
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        res = json.loads(response.content.decode('utf-8'))

        return (res)
    else:
        return 'None'
@app.route('/covidlist')
def postt_covid1():
    lst =[]
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        res = json.loads(response.content.decode('utf-8'))
        length = len(res['response'])
        print (length)


       # for i in range(len(res)):
        #    return str(i)








        #return (res)
    else:
        return 'None'



if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)


