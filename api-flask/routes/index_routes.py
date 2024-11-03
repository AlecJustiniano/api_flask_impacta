from flask import Blueprint, request, jsonify, render_template

index_blueprint = Blueprint('/', __name__)


@index_blueprint.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html")
