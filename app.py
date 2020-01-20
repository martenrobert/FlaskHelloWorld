from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__=="__main__":
    app.run()

@app.route('/SayHello')
def sayHell():
    greeting = {
        "greeting":"Hi!"
    }
    return jsonify(greeting)