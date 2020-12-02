import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        issue = request.form['issue']
        print(issue)
        return 'POST'


    return 'Hello Worlkd!'

if __name__ == '__main__':
    app.run()
