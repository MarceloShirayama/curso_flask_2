import click
from delivery.ext.db import db, models  # noqa


def init_app(app):
    
    @app.cli.command()
    def create_db():
        """
        Desc:
            Create db
        """
        db.create_all()


    @app.cli.command()        
    def list_orders():
        """
        Desc: 
            List orders
        """
        click.echo("list orders")
   