from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}!'
