from config import db


class Professor(db.Model):
    __tablename__ = 'professores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(30))
    observacao = db.Column(db.String(30))

    def __init__(self, nome, idade, materia, observacao):
        self.nome = nome
        self.materia = materia
        self.idade = idade
        self.observacao = observacao

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "materia": self.materia,
            "idade": self.idade,
            "observacao": self.observacao,
        }


class DadoNaoEncontrado(Exception):
    pass


def prof_por_id(id_prof):
    professor = Professor.query.get(id_prof)
    if not professor:
        raise DadoNaoEncontrado
    return professor.to_dict()


def adiciona_prof(prof_data):
    novo_prof = Professor(
        nome=prof_data["nome"],
        materia=prof_data["materia"],
        idade=prof_data["idade"],
        observacao=prof_data["observacao"]
    )
    db.session.add(novo_prof)
    db.session.commit()


def lista_profs():
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]


def deleta_prof(id_prof):
    professor = Professor.query.get(id_prof)
    if not professor:
        raise DadoNaoEncontrado

    # Atualiza o campo 'ativo' para 'não' em todas as turmas associadas ao professor
    for turma in professor.turmas:
        turma.ativo = "não"

    # Se realmente quiser deletar o professor depois de atualizar as turmas:
    db.session.delete(professor)
    
    db.session.commit()


def atualiza_prof(id_prof, novos_dados):
    professor = Professor.query.get(id_prof)
    if not professor:
        raise DadoNaoEncontrado
    professor.nome = novos_dados["nome"]
    professor.materia = novos_dados["materia"]
    professor.idade = novos_dados["idade"]
    professor.observacao = novos_dados["observacao"]
    db.session.commit()
