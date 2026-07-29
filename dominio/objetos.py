# ======================================================
# 01 - Primeiro objeto de dominio do CRM. Guarda apenas os dados
# essenciais do contrato (id, cliente e valor), sem logica de
# negocio. O importante é como as interfaces serão consumidas
# por classes distintas
# ======================================================

from datetime import datetime

class Contrato:
    def __init__(self, id, cliente, valor):
        self.id = id
        self.cliente = cliente
        self.valor = valor

    def __repr__(self):
        """Define como o Contrato aparece em print() ou no terminal interativo."""
        return f"Contrato(id={self.id}, cliente={self.cliente!r}, valor={self.valor})"

class Log:
    def __init__(self, mensagem, criado_em=None):
        self.mensagem = mensagem
        # Se ninguém passou uma data/hora, usamos o momento atual.
        self.criado_em = criado_em if criado_em is not None else datetime.now()

    def __repr__(self):
        """Define como o Log aparece em print() ou no terminal interativo."""
        return f"Log(mensagem={self.mensagem!r}, criado_em={self.criado_em})"

class Notificacao:
    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def __repr__(self):
        """Define como a Notificacao aparece em print() ou no terminal interativo."""
        return f"Notificacao(destinatario={self.destinatario!r}, mensagem={self.mensagem!r})"