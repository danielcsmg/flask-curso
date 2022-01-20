import click
from delivery.ext.db import db
from delivery.ext.db import models

def init_app(app):

    @app.cli.command()
    def create_db():
        db.create_all()


    @app.cli.command()
    def listar_pedidos():
        click.echo("lista de pedidos")
    
    