#!/usr/bin/env python

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    print request.args
    return 'Thanks for filling out our form!'

if __name__ == "__main__":
    app.run()
