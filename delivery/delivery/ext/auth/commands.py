import click
from delivery.ext.db import db
from delivery.ext.auth.models import User



@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """
    Desc:
        Add new user
    args:
        --email, -e 
        --passwd, -p
        --admin, -a (default=True)
    """
    user = User(
        email=email,
        passwd=passwd,
        admin=admin
    )
    db.session.add(user)
    db.session.commit()

    click.echo(f"Usuário {email} criado com sucesso!")



def list_users():
    """
    Desc:
        List users
    """
    users = User.query.all()
    click.echo("Lista de usuários:")
    for user in users:
        click.echo(user)
