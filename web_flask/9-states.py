#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ After each request, it removes the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
def render_states():
    """ displays all states """
    States = storage.all(State).values()
    return render_template("9-states.html", States=States, one=None)


@app.route('/states/<string:id>', strict_slashes=False)
def render_one_state(id):
    """ displays one state if it exists """
    key = "State." + id
    one = None
    if key in storage.all(State):
        one = storage.all(State)[key]
    return render_template("9-states.html", States=None, one=one)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

