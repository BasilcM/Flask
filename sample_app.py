from flask import Flask
app = Flask(__name__)

@app.route('/sample')
def running():
    return 'Flask is running!'

@app.route('/sample/next')
def runnings():
    return 'Hey It is the next Page'

@app.route('/example')
def runningr():
    return 'Working perfectly!'