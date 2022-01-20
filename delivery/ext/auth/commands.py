import click
from delivery.ext.auth.models import User
from delivery.ext.db import db


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    user = User(
        email=email,
        passwd=passwd,
        admin=admin
    )
    db.session.add(user)
    db.session.commit()

    if admin == True:
        click.echo(f'Usuário admin {email} criado com sucesso.')
    else:
        click.echo(f'Usuário {email} criado com sucesso.')


def list_users():
    users = User.query.all()
    click.echo(f"lista de usuários {users}")
