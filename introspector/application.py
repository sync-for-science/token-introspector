# pylint: disable=missing-docstring
""" Holds the create_app() Flask application factory.
"""
import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['API_SERVER'] = os.getenv('API_SERVER')

    from introspector.views.api.views import BP as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
