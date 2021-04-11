from typing import List


class Destinatario:
    def __init__(self, nome, endereco, cidade, uf):
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.uf = uf


class Item:
    def __init__(self, qt_volume, descricao):
        self.qt_volume = qt_volume
        self.descricao = descricao


class Transportador:
    def __init__(self, empresa, nome_motorista, placa):
        self.empresa = empresa
        self.nome_motorista = nome_motorista
        self.placa = placa


class Update:
    def __init__(self, data_hora, descricao):
        self.data_hora = data_hora
        self.descricao = descricao


class Romaneio:
    def __init__(self, numero, data_hora_carga, destinatario: Destinatario, transportador: Transportador,
                 itens: List[Item], updates: List[Update]):
        self.numero = numero
        self.data_hora_carga = data_hora_carga
        self.destinatario = destinatario
        self.transportador = transportador
        self.itens = itens
        self.updates = updates



