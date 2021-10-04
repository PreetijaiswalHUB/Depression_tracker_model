from flask import Flask, json,jsonify, render_template, request
import pickle
import requests
# change the filename before executing
clf = pickle.load(
    open(r'/Users/Pramod/Downloads/Depression-Check-main/Model/model.pkl', 'rb'))

# change the filename before executing
tfidf = pickle.load(
    open(r'/Users/Pramod/Downloads/Depression-Check-main/Model/vect.pkl', 'rb'))

def estimate(x):
    vec = tfidf.transform([x])
    rs = clf.predict(vec)
    return rs[0]


app = Flask(__name__)

rs=""
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        print ("POST")
        print ("get_json: ", request.get_json())
        #print ("data: ", request.data)        
        data = json.loads(request.data)
        print(data['tweetData'])
        global rs
        rs = estimate(data['tweetData'])
        print(str(rs))
        return str(rs)
        #return 'POST'
    else:
        return "GET"


# @app.route('/getresult', methods=['GET', 'POST'])
# def getresult():
    
#     if request.method == 'POST':
#         text = request.form['text']
#         print(text)
#         global rs
#         rs = estimate(text)
#         return str(rs)
    

@app.route('/flask', methods=['GET'])
def ind():
        global rs
        return str(rs)


if __name__ == '__main__':
    app.run(debug=True)
