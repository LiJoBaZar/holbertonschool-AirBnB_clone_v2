#!/usr/bin/python3
"""add a c routing with add value in text"""
from flask import Flask
from markupsafe import escape

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
    return f"c {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
