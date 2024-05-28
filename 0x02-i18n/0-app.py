#!/usr/bin/env python3
"""
0-app module: A basic Flask app
"""
from flask import Flask, render_template

app: Flask = Flask(__name__)


def index() -> str:
    """
    Index route: Renders index.html template
    """
    return render_template(
        '0-index.html',
        title="Welcome to Holberton",
        header="Hello world")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
