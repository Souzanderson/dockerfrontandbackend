from flask import Flask 
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__) 

@app.route("/") 
def home(): 
    return "API - V.1.0.0 "

if __name__ == '__main__':
    app.run()