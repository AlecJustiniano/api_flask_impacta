from config import db  # Certifique-se de que o caminho está correto
from datetime import datetime
from model.model_turma import Turma


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id', ondelete="SET NULL"), nullable=True)
    turma = db.relationship('Turma', backref='alunos')
    dataNasc = db.Column(db.Date)
    nota_S1 = db.Column(db.Integer)
    nota_S2 = db.Column(db.Integer)
    media_F = db.Column(db.Integer)

    def __init__(self, nome, turma, dataNasc, nota_S1, nota_S2, media_F):
        self.nome = nome
        self.turma = turma
        self.dataNasc = dataNasc
        self.nota_S1 = nota_S1
        self.nota_S2 = nota_S2
        self.media_F = media_F

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "turma": self.turma.descricao if self.turma is not None else "Sem Turma",
            "dataNasc": self.dataNasc,
            "nota_S1": self.nota_S1,
            "nota_S2": self.nota_S2,
            "media_F": self.media_F,
        }


class AlunoNaoEncontrado(Exception):
    pass


def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno.to_dict()


def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]


def adiciona_aluno(aluno_data):
    # Busca a turma pelo ID enviado no JSON
    turma_id = aluno_data.get('turma')
    turma = Turma.query.get(turma_id)

    if not turma:
        raise ValueError(f'Turma com id {turma_id} não encontrada')

    # Cria o novo aluno com a instância da turma associada
    novo_aluno = Aluno(
        nome=aluno_data['nome'],
        turma=turma,  # Atribui a instância de Turma, não o ID
        dataNasc=datetime.strptime(aluno_data['dataNasc'], '%Y-%m-%d'),  # Corrige o formato da data
        nota_S1=aluno_data['nota_S1'],
        nota_S2=aluno_data['nota_S2'],
        media_F=aluno_data['media_F']
    )

    # Adiciona e comita no banco de dados
    db.session.add(novo_aluno)
    db.session.commit()


def deletar_aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()


def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    turma_id = novos_dados.get('turma')
    turma = Turma.query.get(turma_id)

    if not turma:
        raise ValueError(f'Turma com id {turma_id} não encontrada')

    data_formatada = datetime.strptime(novos_dados["dataNasc"], '%Y-%m-%d')
    aluno.nome = novos_dados["nome"]
    aluno.turma = turma
    aluno.dataNasc = data_formatada
    aluno.nota_S1 = novos_dados["nota_S1"]
    aluno.nota_S2 = novos_dados["nota_S2"]
    aluno.media_F = novos_dados["media_F"]
    db.session.commit()
