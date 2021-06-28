from logging import debug
from flask import Flask,jsonify,request,make_response
import jwt
import datetime
from auth import auth
from controller.login import login
from functools import wraps
from controller.signup import signup


app = Flask(__name__)



@app.post('/signup')
def signingup():
    return signup(request.get_json())

@app.post('/login')
def loging():
    return login(request.get_json())




@app.route('/admin')
def admin():
    if auth(request,'USER'):
        return jsonify({'message':'admin'})
    return 'unauthorized',401
    


@app.route('/owner')
def owner():
    if auth(request,'USER'):
        return jsonify({'message':'owner'})
    return 'unauthorized',401
    


@app.route('/user')
def user():
    if auth(request,'USER'):
        return jsonify({'message':'user'})
    return 'unauthorized',401

if __name__ == "__main__":
    
	app.run(debug=True)