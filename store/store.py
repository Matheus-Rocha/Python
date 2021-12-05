from datetime import datetime, timedelta

# Produtos:
class Veiculo:

    def __init__(self, preco, placa, cor, marca, n_rodas, velocidade_media):
        self.preco = preco
        self.placa = placa
        self.cor = cor
        self.marca = marca
        self.numero_de_rodas = n_rodas
        self.velocidade_media = velocidade_media

    def valor_de_venda(self):
        return self.preco

    def valor_de_revenda(self):
        desvalorizacao = ((self.preco * 15) / 100)
        return self.preco - desvalorizacao

    def velocidade_media(self):
        return self.velocidade_media



class Carro(Veiculo):

    def __init__(self, potencia, airbag):
        self.potencia = potencia
        self.airbag = airbag

    def velocidade_media(self):
        return self.velocidade_media * (self.potencia * 0.05)


class Caminhao(Veiculo):

    def __init__(self, potencia):
        self.potencia = potencia
        self.carga
        self.tamanho_do_bau
    
    def velocidade_media(self):
        pass

    def quantidade_max_carga(self):
        pass


class Moto(Veiculo):

    def __init__(self, cilindrada):
        self.cilindrada = cilindrada
    
    def velocidade_media(self):
        pass


# Administradores:
class Funcionario:
    
    def __init__(self):
        self.funcionario_id
        self.nome
        self.dias_de_empresa

    def tempo_de_empresa(self):
        time = datetime.now() - timedelta(days=self.dias_de_empresa)


class Gerente(Funcionario):
    
    def __init__(self):
        pass

    def autorizar_desconto(self):
        pass

    def autorizar_compra(self):
        pass


class Vendedor(Funcionario):

    def __init__(self):
        pass

    def vender_veiculo(self):
        pass

    def comprar_veiculo(self):
        pass


class Caixa(Funcionario):

    def __init__(self):
        pass

    def receber_pagamento(self):
        pass

    def dar_troco(self):
        pass


class Cliente:

    def __init__(self):
        self.carteira
        self.tipo

    def beneficios(self):
        pass

    def comprar_veiculo(self):
        pass

    def vender_veiculo(self):
        pass


class ClienteGold(Cliente):

    def __init__(self):
        self.porcentagem_desconto = 0.10

    def beneficios_gold(self):
        pass


class ClienteVip(Cliente):

    def __init__(self):
        self.porcentagem_desconto = 0.15

    def beneficios_vip(self):
        pass


def venda_de_veiculo():
    pass

def compra_de_veiculo():
    pass