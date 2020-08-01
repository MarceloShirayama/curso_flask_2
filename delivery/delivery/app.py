from flask import Flask, render_template
from delivery.ext import site


def create_app():
    """Factory principal"""
    app = Flask(__name__)
    site.init_app(app)
    return app
