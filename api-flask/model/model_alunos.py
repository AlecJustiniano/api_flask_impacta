from config import db  # Certifique-se de que o caminho está correto
from datetime import datetime
from model.model_turma import Turma


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id', ondelete="SET NULL"), nullable=True)
    turma = db.relationship('Turma', backref='alunos')
    dataNasc = db.Column(db.Date)
    nota_S1 = db.Column(db.Float)
    nota_S2 = db.Column(db.Float)
    media_F = db.Column(db.Float)

    def __init__(self, nome, turma, dataNasc, nota_S1, nota_S2):
        self.nome = nome
        self.turma = turma
        self.dataNasc = dataNasc
        self.nota_S1 = nota_S1
        self.nota_S2 = nota_S2
        self.media_F = self.calcula_media()  # Calcula a média automaticamente

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

    def calcula_media(self):
        return (float(self.nota_S1) + float(self.nota_S2)) / 2



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
    turma_id = aluno_data.get('turma')
    turma = Turma.query.get(turma_id)

    if not turma:
        raise ValueError(f'Turma com id {turma_id} não encontrada')

    novo_aluno = Aluno(
        nome=aluno_data['nome'],
        turma=turma,
        dataNasc=datetime.strptime(aluno_data['dataNasc'], '%Y-%m-%d'),
        nota_S1=aluno_data['nota_S1'],
        nota_S2=aluno_data['nota_S2']
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

    # Recalcula a média automaticamente
    aluno.media_F = aluno.calcula_media()
    
    db.session.commit()