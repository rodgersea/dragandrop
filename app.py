from flask import Flask
import sys
import os

print(sys.prefix)

app = Flask(__name__)  # create object "app", which belongs to the Flask class


@app.route("/")  # calls function "index" when requested
def index():  # view function "index" is linked to the main route using the app.route() decorator
    return "Hello World!"
