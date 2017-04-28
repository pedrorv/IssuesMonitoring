from datetime import datetime
from .usuario_sistema import UsuarioSistema
from . import db

def AdministradorSistema(UsuarioSistema):
    admin = True

    def autorizar_usuario_lab(user_id):
        data_aprovacao = int(datetime.now().timestamp())
        db.execute("""
            UPDATE User_Lab
            SET data_aprov = ?
            WHERE user_id = ?;""", (data_aprovacao, user_id))
