#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import Flask


hbnb_route = Flask(__name__)

@hbnb_route.route("/", strict_slashes=False)
def hello():
    """
    Routes:
    /: Hello 
    """
    return "Hello HBNB!"

@hbnb_route.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    /hbnb: 
    """
    return "HBNB"


if __name__ == "__main__":
    hbnb_route.run(host='0.0.0.0', port=5000)
