from flask import Flask, render_template, request, redirect, url_for
from configuracao import configura_tudo
from database.models.produto import Produto

app = Flask(__name__)

configura_tudo(app)


@app.route('/')
def form():
    return render_template('index_form.html')


@app.route('/listagem/')
def listagem():
    produtos = Produto.select().order_by(Produto.valor)
    return render_template('listagem.html', produtos=produtos)


@app.route('/', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    descricao = request.form.get('descricao', '')
    valor = float(request.form['valor'])
    disp = request.form['disp'] == 'Sim'

    Produto.create(nome=nome, descricao=descricao, valor=valor, disp=disp)
    return redirect(url_for('listagem'))


@app.route('/<int:produto_id>')
def detalhe(produto_id):
    produto = Produto.get_by_id(produto_id)         
    return render_template('detalhe_produto.html', produto=produto)


@app.route('/<int:produto_id>/edit', methods=['GET', 'POST'])
def editar(produto_id):
    produto = Produto.get_by_id(produto_id)
    
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.descricao = request.form.get('descricao', '')
        produto.valor = float(request.form['valor'])
        produto.disp = request.form['disp'] == 'Sim'
        produto.save()
        return redirect(url_for('listagem'))
        
    return render_template('editar.html', produto=produto)


@app.route('/<int:produto_id>/update', methods=['PUT'])
def atualizar(produto_id):
    data = request.json  

    produto_editado = Produto.get_by_id(produto_id)

    produto_editado.nome = data['nome']
    produto_editado.descricao = data['descricao']
    produto_editado.valor = data['valor']
    produto_editado.disp = data['disp']

    produto_editado.save()
    redirect(url_for('listagem'))   


@app.route('/<int:produto_id>/delete', methods=['DELETE'])
def deletar(produto_id):
    produto = Produto.get_by_id(produto_id)
    produto.delete_instance()
    return 'deleted'