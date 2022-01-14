from flask import render_template, request
from flask import Blueprint

bp = Blueprint("site", __name__)

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/sobre')
def about():
    return render_template("about.html")

@bp.route('/restaurantes')
def restaurantes():
    nome = request.user_agent
    print(nome)
    return render_template("restaurantes.html")