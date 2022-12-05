#!/usr/bin/python3
"""Use variable with a routing"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Display web app homepage"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Display web app root hbnb page"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """Display web app root c and add text variable"""
    result = text.replace('_', ' ')
    return f"C {result}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
