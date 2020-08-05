from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from delivery.ext.auth.models import User
from delivery.ext.db import db
from flask import flash, Markup


# def format_user(self, request, user, *args):
#     return user.email.split("@")[0]

# TODO: configurar os outros models

class UserAdmin(ModelView):
    """Interface admin of the user"""

    # column_formatters = {"email": format_user}
    # ou
    column_formatters = {
        "email": lambda s, r, u, *a: Markup(f'<b>{u.email.split("@")[0]}</b>')
    }

    column_list = ["email", "admin"]

    column_searchable_list = ["email"]

    column_filters = [
        "email", 
        "admin",
        filters.FilterLike(
            User.email,
            "domíno",
            options=(("gmail", "Gmail"), ("uol", "Uol"))
        )
    ]
    
    can_edit = False
    can_create = True
    can_delete = True


    @action(
        'Toggle_admin',
        'Toggle admin status of selected users ',
        'Are you sure?'
    )
    def toggle_admin_status(self, ids):
        """ 
        Altera o status de administrador do usuário
            args: 
                self, ids
            return: altera o status  de administrador do usuário.
        """
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f"{len(users)} Usuário(s) alterado(s) com sucesso!", "success")
        # flash(f"{len(users)} Usuário(s) alterado(s) com erro!", "error")
        # flash(f"{len(users)} Usuário(s) alterado(s) com perigo!", "danger")


    @action(
        'Send email',
        'Send email to selected users',
        'Are you sure?'
    )
    def send_email(self, ids):
        """ 
        Envia email aos usuários
            args:
                self, ids
            return: envio de emails.
        """
        users = User.query.filter(User.id.in_(ids)).all()
        # 1) redirect para um form para escrever a mensagem de email
        # 2) enviar email
        db.session.commit()
        flash(f"{len(users)} email(s) enviado(s) com sucesso!", "success")
        # flash(f"{len(users)} Usuário(s) alterado(s) com erro!", "error")
        # flash(f"{len(users)} Usuário(s) alterado(s) com perigo!", "danger")




