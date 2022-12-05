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
    """display the second url page"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
