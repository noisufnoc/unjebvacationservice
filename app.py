#!/usr/bin/env python
import random
from flask import Flask, jsonify

app = Flask(__name__)


facts = [
    'bananas are delicious',
    'i like turtles',
    'jeff is a pug'
]


@app.route('/')
def index():
    return jsonify({'fact': facts[random.randint(0, 2)]})


if __name__ == '__main__':
    app.run()
