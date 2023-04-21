#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import Flask


python_route = Flask(__name__)

@python_route.route("/", strict_slashes=False)
def hello():
    """
    Routes:
    /: Hello 
    """
    return "Hello HBNB!"

@python_route.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    /hbnb: 
    """
    return "HBNB"

@python_route.route("/c/<text>", strict_slashes=False)
def print_variable(text):
    """
    display C followed by the value of text variable
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

@python_route.route("/python/<text>", strict_slashes=False)
@python_route.route("/python/", strict_slashes=False)
def var_deafult_parameters(text="is_cool"):
    """
    set a variable to be displayed with a default value
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == "__main__":
    python_route.run(host='0.0.0.0', port=5000)
