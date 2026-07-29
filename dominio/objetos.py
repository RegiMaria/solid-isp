# ======================================================
# 01 - Primeiro objeto de dominio do CRM. Guarda apenas os dados
# essenciais do contrato (id, cliente e valor), sem logica de
# negocio
# ======================================================

from datetime import datetime

class Contrato:
    def __init__(self, id, cliente, valor):
        self.id = id
        self.cliente = cliente
        self.valor = valor

    def __repr__(self):
        return f"Contrato(id={self.id}, cliente={self.cliente!r}, valor={self.valor})"

