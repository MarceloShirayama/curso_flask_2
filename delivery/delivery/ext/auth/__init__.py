from delivery.ext.auth import  models
from delivery.ext.auth.commands \
    import add_user, list_users

from delivery.ext.db import db
from delivery.ext.auth.admin import UserAdmin   # este import tem que vir antes
from delivery.ext.admin import admin    # este import tem que vir depois
from delivery.ext.auth.models import User


def init_app(app):
    """TODO: Incializa o Flask Simple Login + JWT"""
    app.cli.command()(list_users)
    app.cli.command()(add_user)

    admin.add_view(UserAdmin(User, db.session))
