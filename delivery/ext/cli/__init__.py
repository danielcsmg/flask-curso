import email
from email.policy import default
from gc import is_finalized
import click
from delivery.ext.db import db
from delivery.ext.site import models

def init_app(app):

    @app.cli.command()
    def create_db():
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f'Usuário {email} criado com sucesso.')

    @app.cli.command()
    def listar_pedidos():
        click.echo("lista de pedidos")
    
    @app.cli.command()
    def listar_usuarios():
        click.echo("lista de usuários")

    