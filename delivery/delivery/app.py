from flask import Flask, render_template  # noqa

from delivery.ext import config


def create_app():
    """
    Application factory
        Args:
            None
        Returns:
            The Flask application object
    """
    app = Flask(__name__)
    config.init_app(app)
    return app
