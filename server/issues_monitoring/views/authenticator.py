from flask import request, jsonify
from .. import app, controllers


@app.route('/validar_usuario_authenticator', methods=["POST"])
def validar_usuario_authenticator():
    conteudo = request.get_json(silent=True)
    user_id = conteudo.get('user_id')
    email = conteudo.get('email')
    validacao = controllers.validar_usuario_authenticator(user_id, email)
    resposta = jsonify(validacao)

    if 'erro' in validacao:
        resposta.status_code = 401
        return resposta

    return resposta


@app.route('/registrar_entrada_authenticator', methods=["POST"])
def registrar_entrada_authenticator():
    conteudo = request.get_json(silent=True)
    user_id = conteudo.get('user_id')
    lab_id = conteudo.get('lab_id')
    validacao = controllers.registrar_entrada_authenticator(user_id, lab_id)
    resposta = jsonify(validacao)

    if 'erro' in validacao:
        resposta.status_code = 500
        return resposta

    return resposta
