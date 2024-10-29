from flask import Blueprint, request, jsonify

index_blueprint = Blueprint('/', __name__)


@index_blueprint.route("/", methods=["GET"])
def pagina_inicial():
    return jsonify({"msg": "Bem vindo a pagina inicial"})
