from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Flask!"


@app.route("/hello")
def hello():
    return "Hello, World!"
