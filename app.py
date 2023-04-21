#!/usr/bin/env python3
from flask import Flask;

#very basic flask application

app = Flask(__name__) #references this file

# creating an index route to avoid a 404, in brackets is the url
# the define the function for that route
@app.route("/")
def index():
    return "hello, world!"

if __name__ == "__main__":
    app.run(debug=True) # any errors will pop up in the web
