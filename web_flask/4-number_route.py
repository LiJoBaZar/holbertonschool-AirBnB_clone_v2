#!/usr/bin/python3
"""using flask Framework for routing"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """display the homepage"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """display the 2nd url page"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """display custom 3rd url page"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python(text):
    """display custom 4th url page"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    """display custom 5th url page"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
