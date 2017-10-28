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
