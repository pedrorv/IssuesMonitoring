from flask import request, jsonify
from .. import app, controllers


@app.route('/validar_usuario_authenticator', methods=["POST"])
def validar_usuario_authenticator():
    conteudo = request.get_json(silent=True)
    login = conteudo.get('login')
    senha = conteudo.get('senha')
    validacao = controllers.validar_usuario_authenticator(login, senha)
    resposta = jsonify(validacao)

    if 'erro' in validacao:
        resposta.status_code = 401
        return resposta

    return resposta
