from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from model.model_turma import DadoNaoEncontrado, lista_turmas, turma_por_id, adicionar_turma, atualiza_tudo, delete_turma

turmas_blueprint = Blueprint('turmas', __name__)


@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = lista_turmas()
    return render_template("turmas.html", turmas=turmas)


@turmas_blueprint.route("/turmas/<int:id_turma>", methods=["GET"])
def get_turmas_por_id(id_turma):
    try:
        return turma_por_id(id_turma)
    except DadoNaoEncontrado:
        return ({"erro": 'turma não encontrada'}, 400)


@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    dict = request.json
    adicionar_turma(dict)
    return lista_turmas()


@turmas_blueprint.route("/turmas/<int:turma_id>", methods=["PUT"])
def update_turma(turma_id):
    data = request.json
    try:
        atualiza_tudo(turma_id, data)
        return jsonify(turma_por_id(turma_id))
    except DadoNaoEncontrado:
        return jsonify({"erro": 'Turma nao encontrado'}), 404


@turmas_blueprint.route('/turmas/<int:turma_id>', methods=['DELETE'])
def excluir_aluno(turma_id):
    try:
        delete_turma(turma_id)
        return "", 204
    except DadoNaoEncontrado:
        return jsonify({"erro": 'turma não encontrada'}), 404
