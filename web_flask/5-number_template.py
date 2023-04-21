#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import Flask, render_template
import os

template_route = Flask(__name__, template_folder=os.path.join(
    os.path.dirname(__file__), 'templates'))


@template_route.route("/", strict_slashes=False)
def hello():
    """
    Routes:
    /: Hello
    """
    return "Hello HBNB!"


@template_route.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    /hbnb:
    """
    return "HBNB"


@template_route.route("/c/<text>", strict_slashes=False)
def print_variable(text):
    """
    display C followed by the value of text variable
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@template_route.route("/python/<text>", strict_slashes=False)
@template_route.route("/python/", strict_slashes=False)
def var_deafult_parameters(text="is_cool"):
    """
    set a variable to be displayed with a default value
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@template_route.route("/number/<int:n>", strict_slashes=False)
def integer_num(n):
    """
    display n is number only if n is an integer
    """
    return "{} is a number".format(n)


@template_route.route("/number_template/<int:n>", strict_slashes=False)
def render_page(n):
    """
    display a html page only if n is an integer
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    template_route.run(host='0.0.0.0', port=5000)
