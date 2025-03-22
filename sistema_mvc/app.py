
from flask import Flask
from flask_mysqldb import MySQL # biblioteca mysql flask
from controllers.produto_controller import produto_bp 
import config

app = Flask(__name__) # Instanciar o Flask
app.config.from_object(config) # Configurando Variedades


mysql = MySQL(app)

# passando a conexão para os controllers 
app.mysql

# registrar o controller
app.register_blueprint(produto_bp)

# rodar o app
if __name__ == '__main__':
    app.run(debug=True)