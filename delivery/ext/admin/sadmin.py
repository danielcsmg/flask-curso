from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from delivery.ext.auth.models import User
from delivery.ext.db import db
from flask import flash, Markup



#def format_user(self, request, user, *args):
#    return user.email.split('@')[0]


class UserAdmin(ModelView):
    column_formatters = {
        "email": lambda s, r, u, *a: Markup(f'<b>{u.email.split("@")[0]}</b>')
    }

    column_searchable_list = ["email"]

    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email,
            "dominio",
            options=(('gmail', 'Gmail'), ('uol', 'Uol'))
        )
        ]

    column_list = ['email','admin']

    '''can_edit = False
    can_delete = False
    can_create = False'''

    @action(
        'toggle_admin',
        'Toggle admin status',
        'Are you sure?'
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f'{len(users)} usuários alterados com sucesso!', 'success')