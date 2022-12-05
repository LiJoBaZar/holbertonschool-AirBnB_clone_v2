#!/usr/bin/python3
"""Routing with other root"""
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
    """Display web app root c"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
