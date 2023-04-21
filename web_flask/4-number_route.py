#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """ displays c + text """
    return "C %s" % text.replace('_', ' ')


@app.route("/python/", defaults={"text": "is cool"})
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text):
    """ displays Python + text """
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ displays: n is a number """
    return "%d is a number" % n

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
