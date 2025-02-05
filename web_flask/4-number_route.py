#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import Flask


number_route = Flask(__name__)


@number_route.route("/", strict_slashes=False)
def hello():
    """
    Routes:
    /: Hello
    """
    return "Hello HBNB!"


@number_route.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    /hbnb:
    """
    return "HBNB"


@number_route.route("/c/<text>", strict_slashes=False)
def print_variable(text):
    """
    display C followed by the value of text variable
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@number_route.route("/python/<text>", strict_slashes=False)
@number_route.route("/python/", strict_slashes=False)
def var_deafult_parameters(text="is_cool"):
    """
    set a variable to be displayed with a default value
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@number_route.route("/number/<int:n>", strict_slashes=False)
def integer_num(n):
    """
    display n is number only if n is an integer
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    number_route.run(host='0.0.0.0', port=5000)
