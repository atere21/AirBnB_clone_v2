#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage, State, Amenity

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """ After each request, it removes the current SQLAlchemy Session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def render_states_amenities():
    """ displays states and cities """
    States = storage.all(State).values()
    Amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", States=States, Amenities=Amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
