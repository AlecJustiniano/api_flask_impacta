from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from model.model_profs import DadoNaoEncontrado, lista_profs, prof_por_id, adiciona_prof, atualiza_prof, deleta_prof

professores_blueprint = Blueprint('professores', __name__)


@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    profs = lista_profs()
    return render_template("profs.html", profs=profs)


@professores_blueprint.route('/professores/adicionar', methods=['GET'])
def adicionar_prof_page():
    return render_template('criarProf.html')


@professores_blueprint.route('/professores', methods=['POST'])
def cria_professor():
    data = request.form
    adiciona_prof(data)
    profs = lista_profs()
    return render_template("profs.html", profs=profs)


@professores_blueprint.route('/professores/<int:id_prof>', methods=['GET'])
def get_professorPorId(id_prof):
    try:
        professor = prof_por_id(id_prof)
        return render_template("prof_id.html", professor=professor)
    except DadoNaoEncontrado:
        return jsonify({"erro": 'Professor nao encontrado'}), 404


@professores_blueprint.route('/professores/<int:id_prof>/editar', methods=['GET'])
def editar_prof_page(id_prof):
    try:
        prof = prof_por_id(id_prof)
        return render_template('prof_update.html', prof=prof)
    except DadoNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


@professores_blueprint.route('/professores/<int:id_prof>', methods=['PUT', "POST"])
def update_professor(id_prof):
    print("Dados recebidos no formulário:", request.form)
    try:
        prof = prof_por_id(id_prof)
        nome = request.form["nome"]
        materia = request.form["materia"]
        idade = request.form["idade"]
        observacao = request.form["observacao"]
        prof["nome"] = nome
        prof["materia"] = materia
        prof["idade"] = idade
        prof["observacao"] = observacao
        atualiza_prof(id_prof, prof)
        return redirect(url_for('professores.get_professores', id_prof=id_prof))
    except DadoNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


@professores_blueprint.route('/professores/delete/<int:id_prof>', methods=['POST', 'DELETE'])
def delete_professor(id_prof):
    try:
        deleta_prof(id_prof)
        return redirect(url_for("professores.get_professores"))
    except DadoNaoEncontrado:
        return jsonify({"erro": 'professor nao encontrado'}), 404
