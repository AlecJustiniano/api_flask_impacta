📋 Pré-requisitos
Antes de começar, certifique-se de ter instalado:

Python 3.x

Pip (gerenciador de pacotes do Python)

Git (opcional, para clonar o repositório)

🔧 Instalação
Clone o repositório (ou baixe o código-fonte):

bash
Copy
git clone https://github.com/AlecJustiniano/api_flask_impacta.git
cd api-flask
Crie um ambiente virtual (recomendado):

bash
Copy
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
Instale as dependências:

bash
Copy
pip install flask

bash
Copy
pip install sqlalchemy

bash
Copy
pip install requests

Configure o banco de dados:

O projeto usa SQLite como banco de dados. O arquivo app.db será criado automaticamente quando você rodar a aplicação pela primeira vez.

Execute a aplicação:

bash
Copy
python app.py
A aplicação estará disponível em http://0.0.0.0:8000.

🛠️ Estrutura do Projeto
app.py: Ponto de entrada da aplicação. Registra os blueprints e inicializa o banco de dados.

config.py: Configurações da aplicação, como host, porta e conexão com o banco de dados.

routes/: Contém os blueprints para as rotas de alunos, professores e turmas.

models/: Define os modelos do banco de dados (alunos, professores, turmas).

🧩 Funcionalidades
Alunos: CRUD para gerenciar alunos.

Professores: CRUD para gerenciar professores.

Turmas: CRUD para gerenciar turmas.

Banco de dados SQLite: Armazena os dados localmente.

📚 Rotas da API
Aqui estão alguns exemplos de rotas disponíveis:

Alunos:

GET /alunos: Lista todos os alunos.

POST /alunos: Cria um novo aluno.

GET /alunos/<id>: Retorna os detalhes de um aluno específico.

PUT /alunos/<id>: Atualiza um aluno existente.

DELETE /alunos/<id>: Remove um aluno.

Professores:

GET /professores: Lista todos os professores.

POST /professores: Cria um novo professor.

GET /professores/<id>: Retorna os detalhes de um professor específico.

PUT /professores/<id>: Atualiza um professor existente.

DELETE /professores/<id>: Remove um professor.

Turmas:

GET /turmas: Lista todas as turmas.

POST /turmas: Cria uma nova turma.

GET /turmas/<id>: Retorna os detalhes de uma turma específica.

PUT /turmas/<id>: Atualiza uma turma existente.

DELETE /turmas/<id>: Remove uma turma.

🛠️ Construído com
Flask: Framework web leve para Python.

SQLAlchemy: ORM para interagir com o banco de dados.

SQLite: Banco de dados leve e embutido.

🤝 Como Contribuir
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do projeto.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Commit suas mudanças (git commit -m 'Adiciona nova feature').

Push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🎁 Agradecimentos
Agradeço à comunidade Flask por fornecer uma documentação incrível.

Inspirado por projetos de gerenciamento escolar.

📝 Notas Adicionais
Se você precisar de ajuda, abra uma issue no repositório.

Para melhorar o desempenho em produção, considere usar um banco de dados mais robusto, como PostgreSQL ou MySQL.
