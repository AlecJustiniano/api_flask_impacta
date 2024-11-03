from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from model.model_alunos import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adiciona_aluno, atualizar_aluno, deletar_aluno_por_id


alunos_blueprint = Blueprint('alunos', __name__)


@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = listar_alunos()
    return render_template("alunos.html", alunos=alunos)


@alunos_blueprint.route("/alunos/<int:id_aluno>", methods=["GET"])
def get_alunoPorId(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template("aluno_id.html", aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({"erro": 'aluno nao encontrado'}), 404


@alunos_blueprint.route('/alunos/adicionar', methods=['GET'])
def adicionar_aluno_page():
    return render_template('criarAlunos.html')


@alunos_blueprint.route("/alunos", methods=["POST"])
def cria_aluno():
    data = request.form
    adiciona_aluno(data)
    alunos = listar_alunos()
    return render_template("alunos.html", alunos=alunos)


@alunos_blueprint.route('/alunos/<int:id_aluno>/editar', methods=['GET'])
def editar_aluno_page(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template('alunos_update.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404


@alunos_blueprint.route("/alunos/<int:aluno_id>", methods=["PUT", "POST"])
def update_aluno(aluno_id):
    print("Dados recebidos no formulário:", request.form)
    try:
        aluno = aluno_por_id(aluno_id)
        nome = request.form['nome']
        turma = request.form["turma"]
        dataN = request.form["dataNasc"]
        nota_S1 = request.form["nota_S1"]
        nota_S2 = request.form["nota_S2"]
        aluno['nome'] = nome
        aluno["turma"] = turma
        aluno["dataNasc"] = dataN
        aluno["nota_S1"] = nota_S1
        aluno["nota_S2"] = nota_S2
        atualizar_aluno(aluno_id, aluno)
        return redirect(url_for('alunos.get_alunos', id_aluno=aluno_id))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404


@alunos_blueprint.route('/alunos/delete/<int:id_aluno>', methods=['POST', 'DELETE'])
def excluir_aluno(id_aluno):
    try:
        deletar_aluno_por_id(id_aluno)  
        return redirect(url_for('alunos.get_alunos'))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
