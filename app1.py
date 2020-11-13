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

    result = request.form
    #result1 = result['country']
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        res=json.loads(response.content.decode('utf-8'))
        #res1=res['response'][1]['continent']
        res2=res['response']
        length = len(res['response'])
        print(length) #227
        j = 0
        while j <= length:
            for i in res2:
                j = j + 1


            #ret= res['response'][i]['continent']
           #print(ret)
            #lst.append(ret)
                print(i)

                return(i)


            '''if result1 in ret:
                return('success')
            else:
                return('no')'''







            #return "man"



    else:
        return None
@app.route('/none')
def covid_home2():
    gett_value = home_country()
    for i in gett_value:
        return(i)














@app.route('/covid')
def postt_covid():
    response = requests.request("GET", url, headers=headers)

    return (response.text)



if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)

