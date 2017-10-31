from flask import request, jsonify
from .. import app, controllers


@app.route('/validar_usuario_authenticator', methods=["POST"])
def validar_usuario_authenticator():
    conteudo = request.get_json(silent=True)
    user_id = conteudo.get('userId')
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
    user_id = conteudo.get('userId')
    lab_id = conteudo.get('labId')
    validacao = controllers.registrar_entrada_authenticator(user_id, lab_id)
    resposta = jsonify(validacao)

    if 'erro' in validacao:
        resposta.status_code = 500
        return resposta

    return resposta


@app.route('/registrar_saida_authenticator', methods=["POST"])
def registrar_saida_authenticator():
    conteudo = request.get_json(silent=True)
    user_id = conteudo.get('userId')
    lab_id = conteudo.get('labId')
    validacao = controllers.registrar_saida_authenticator(user_id, lab_id)
    resposta = jsonify(validacao)

    if 'erro' in validacao:
        resposta.status_code = 500
        return resposta

    return resposta
