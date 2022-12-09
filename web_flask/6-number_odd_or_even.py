#!/usr/bin/python3
"""using flask Framework for routing""""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """show the homepage"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """show the 2nd url page"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """show custom 3rd url page"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python(text):
    """show custom 4th url page"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    """show custom 5th url page"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_templete(n):
    """show custom 6th url page"""
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """show custom integer 7th url page"""
    if (n % 2) != 0:
        """is odd"""
        n = "{} is odd".format(n)
        return render_template('6-number_odd_or_even.html', number=n)
    """Is even"""
    n = "{} is even".format(n)
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
