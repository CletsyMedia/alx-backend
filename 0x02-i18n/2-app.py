#!/usr/bin/env python3
"""
2-app module: Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale() -> str:
    """
    Get locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Index route: Renders 2-index.html template
    """
    return render_template(
        '2-index.html',
        title="Welcome to Holberton",
        header="Hello world")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
