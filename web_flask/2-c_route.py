#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import Flask


c_route = Flask(__name__)

@c_route.route("/", strict_slashes=False)
def hello():
    """
    Routes:
    /: Hello 
    """
    return "Hello HBNB!"

@c_route.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    /hbnb: 
    """
    return "HBNB"

@c_route.route("/c/<text>", strict_slashes=False)
def print_variable(text):
    """
    display C followed by the value of text variable
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    c_route.run(host='0.0.0.0', port=5000)
