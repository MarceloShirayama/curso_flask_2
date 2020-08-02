from flask import Flask, render_template
from delivery.ext import site, toolbar, config, db, cli


def create_app():
    """Factory principal"""
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
