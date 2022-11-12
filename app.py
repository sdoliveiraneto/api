from flask import Flask, jsonify, request

app = Flask(__name__)

clientes = [
    {
        'id': 1,
        'Cliente': 'Cliente A',
        'Saldo': 'Saldo',
        'Investimento': 'Total',
        'Sugestão': 'Valor',
        'Variação': 'Porcentagem'
    },
    {
        'id': 2,
        'Cliente': 'Cliente B',
        'Saldo': 'Saldo',
        'Investimento': 'Total',
        'Sugestão': 'Valor',
        'Variação': 'Porcentagem'
    },
    {
        'id': 3,
        'Cliente': 'Cliente B',
        'Saldo': 'Saldo',
        'Investimento': 'Total',
        'Sugestão': 'Valor',
        'Variação': 'Porcentagem'
    },
]

# Consultar(todos)


@app.route('/clientes', methods=['GET'])
def obter_clientes():
    return jsonify(clientes)

# Consultar(id)


@app.route('/clientes/<int:id>', methods=['GET'])
def obter_id(id):
    for cliente in clientes:
        if cliente.get('id') == id:
            return jsonify(cliente)

# Editar


@app.route('/clientes/<int:id>', methods=['PUT'])
def editar_clientes(id):
    cliente_alterado = request.get_json()
    for indice, cliente in enumerate(clientes):
        if cliente.get('id') == id:
            clientes[indice].update(cliente_alterado)
            return jsonify(clientes[indice])

# Criar novo cliente


@app.route('/clientes', methods=['POST'])
def incluir_cliente():
    novo_cliente = request.get_json()
    clientes.append(novo_cliente)
    return jsonify(clientes)


app.run(port=5000, host='localhost', debug=True)
