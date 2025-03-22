
from flask import Blueprint, current_app, render_template, request, url_for, redirect 
from sistema_mvc.models.produto import Produto
from models.produto import produto 

produto_bp = Blueprint('Produto, __name')

@produto_bp.route('/')
def index():
    produtos = Produto.listar(current_app.mysql)
    return render_template('index.html', produtos=produtos)

@produto_bp.route('/criar', methods=['GET, POST'])
def criar():
    if request.method == 'POST':
    # deseja criar um produto
        nome = request.form['nome']
        preco = request.form['preco']
        Produto.salvar(Produto(None, nome, preco), current_app.mysql) # Salvar no banco
        return redirect(url_for('criar.html'))
    return render_template('criar.html') # pagina de fora 


@produto_bp.route('/editar/<int:id>', methods={'GET', 'POST'})
def editar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        Produto.atualizar(Produto(id, nome, preco), current_app.mysql)
        return redirect(url_for('produto.index'))
    prod = Produto.buscar_por_id(current_app.mysql, id)
    return render_template('editar.html', produto=prod)

@produto_bp.route('/deletar/<int:id>')
def deletar(id):
    Produto.deletar(current_app.mysql, id)
    return redirect(url_for('produto.index'))

    