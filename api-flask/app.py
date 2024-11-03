import os
from config import app, db
from routes.alunos_routes import alunos_blueprint
from routes.profs_routes import professores_blueprint
from routes.turmas_routes import turmas_blueprint
from routes.index_routes import index_blueprint


app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)
app.register_blueprint(turmas_blueprint)
app.register_blueprint(index_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
 
