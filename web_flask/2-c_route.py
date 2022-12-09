#!/usr/bin/python3
"""using flask Framework for routing""""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """show the homepage"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """show the second url page"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """display custom third url page"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
