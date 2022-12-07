#!/usr/bin/python3
"""use flask with storage and db storage"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def state_list():
    """display list of states"""
    state_list = storage.all(State)
    return render_template("7-states_list.html")


@app.teardown_appcontext
def teardown():
    """close storage"""
    return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
