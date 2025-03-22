from flask import Flask, jsonify, request, render_template


# Criando aplicação em Flask !
app = Flask(__name__)

@app.route('/')
def home():
      return render_template('index.html')
1
# GET - > uscar algo
@app.route('/helloword', methods=['GET'])
def helloworld():
    return jsonify({
        "msg": "Ola mundo como estao voces"
    })
''
#Lista de tarefas
tarefas = [
      {"id": 1, " titulo":"Estudar Python", "feito": False},
      {"id": 2, "titulo": "Ler a doc", "feito": True }
]

"""
JavaScript (front) = fetch
reactJS (front) = axios 
insomsina (aplicativo) = simular um front

back-end - > modelo de API - > FULL REST
Full = arquitetura MVC (model, view, controller)
"""

@app.route('/tarefas', methods=['GET'])
def get_tarefas():
      return jsonify(tarefas)

# Post - Criar uma nova tarefa
@app.route('/tarefas', methods=['POST'])
def add_tarefas():
      nova_tarefa = request.json # pegar a infomaçao do body
      nova_tarefa['id'] = len(tarefas) + 1 # adicionando novo id
      tarefas.append(nova_tarefa) # adicionando nova tarefa na lista
      return jsonify(nova_tarefa), 201 # 201 -> created -> criado com sucesso 

# Iniciar o servidor 
if __name__ == '__main__':
        app.run(debug=True)

# http://localhost:5000/helloworld


