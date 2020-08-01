from flask import Flask


def create_app():
    """Factory principal"""
    app = Flask(__name__)
    return app
