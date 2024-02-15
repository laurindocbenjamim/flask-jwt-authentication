from flask import Flask, jsonify, request, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask("Flask with JWT Authentication")
app.config['SECRET_KEY'] = '608433bf0b1a4d319ce2c6efa2982c3d'


""" This is for home page"""
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Logged in currently!'

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request/args.get('token')
        if not token:
            return jsonify({'Alert!': 'Token is missing!'})
        
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Alert!': 'Invalid token!'})
    return decorated

""" For public person """
@app.route('/public')
def public():
    return 'Fo public person'

""" For authenticated persons"""
@app.route('/auth')
@token_required
def dashboard():
    return "JWT Verified! Welcome to the Dashboard"

""" For the login page """
@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True
        date = timedelta(seconds=120)
        token = jwt.encode({
            'user': request.form['username'],
            
        },
            app.config['SECRET_KEY']
        )
        return jsonify({'token': token})
    
    else:
        return make_response('Unable to verify', 403, 
                             {'WWW-Authenticate' : 'Basic realm: "Autehentication Failed!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)