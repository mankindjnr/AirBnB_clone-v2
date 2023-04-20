#!/usr/bin/python3
from flask import Flask

#very basic flask application

hello_route = Flask(__name__) #references this file

# creating an index route to avoid a 404, in brackets is the url
# the define the function for that route
@app.route("/", strict_slashes=False)
def index():
    return "hello, mankind!"

if __name__ == "__main__":
    hello_route.run(host='0.0.0.0', port=5000) # any errors will pop up in the web
