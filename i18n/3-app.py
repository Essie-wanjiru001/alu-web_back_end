#!/usr/bin/env python3
''' Flask application with Babel
Parameterize templates '''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' app Config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    ''' Determine best match with supported languages '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world() -> str:
    ''' Output templates '''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
