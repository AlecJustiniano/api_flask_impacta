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
        turma = turma_por_id(id_turma)
        return render_template("turmas_id.html", turma=turma)
    except DadoNaoEncontrado:
        return ({"erro": 'turma não encontrada'}, 400)


@turmas_blueprint.route('/turmas/adicionar', methods=['GET'])
def adicionar_turma_page():
    return render_template('criarTurma.html')


@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    try:
        descricao = request.form.get('descricao')
        professor_id = request.form.get('prof_id')
        ativo = request.form.get('ativo')

        turma_data = {
            'descricao': descricao,
            'prof_id': professor_id,
            'ativo': ativo
        }

        adicionar_turma(turma_data)
        return redirect(url_for('turmas.get_turmas'))
    except DadoNaoEncontrado:
        redirect(url_for('turmas.create_turma'))


@turmas_blueprint.route("/turmas/editar/<int:id_turma>", methods=["GET"])
def editar_turma_page(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return render_template("turmas_update.html", turma=turma)
    except DadoNaoEncontrado:
        return jsonify({'message': 'Turma não encontrado'}), 404


@turmas_blueprint.route('/turmas/<int:id_turma>', methods=['PUT', 'POST'])
def update_turma(id_turma):
    print("Dados recebidos no formulário:", request.form)
    try:
        turma = turma_por_id(id_turma)
        descricao = request.form["descricao"]
        professor = request.form["prof_id"]
        ativo = request.form["ativo"]
        turma["descricao"] = descricao
        turma["professor"] = professor
        turma["ativo"] = ativo
        atualiza_tudo(id_turma, turma)
        return redirect(url_for('turmas.get_turmas', id_turma=id_turma))
    except DadoNaoEncontrado:
        return jsonify({'message': 'Turma não encontrada'}), 404


@turmas_blueprint.route('/turmas/delete/<int:turma_id>', methods=['POST', 'DELETE'])
def excluir_turma(turma_id):
    try:
        delete_turma(turma_id)
        return redirect(url_for('turmas.get_turmas'))
    except DadoNaoEncontrado:
        return jsonify({"erro": 'turma não encontrada'}), 404
