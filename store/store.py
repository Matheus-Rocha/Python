from datetime import datetime, timedelta

# Produtos:
class Veiculo:

    def __init__(self):
        self.vendido = False

    def tem_na_loja(self):
        return False if self.vendido else True

    def valor_de_venda(self):
        return self.preco

    def valor_de_revenda(self):
        desvalorizacao = ((self.preco * 15) / 100)
        return self.preco - desvalorizacao

    def velocidade_media(self):
        if self.potencia:
            return self.velocidade_media * (self.potencia * 0.1)
        return self.velocidade_media * (self.cilindrada * 0.1)


class Carro(Veiculo):

    def __init__(self, preco, placa, cor, marca, velocidade_media, potencia, airbag):
        self.preco = preco
        self.placa = placa
        self.cor = cor
        self.marca = marca
        self.velocidade_media = velocidade_media
        self.potencia = potencia
        self.airbag = airbag


class Caminhao(Veiculo):

    def __init__(self, preco, placa, marca, velocidade_media, potencia, tamanho_do_bau):
        self.preco = preco
        self.placa = placa
        self.marca = marca
        self.velocidade_media = velocidade_media
        self.potencia = potencia
        self.tamanho_do_bau = tamanho_do_bau

    def quantidade_max_carga(self):
        return self.tamanho_do_bau


class Moto(Veiculo):

    def __init__(self, preco, placa, cor, marca, velocidade_media, cilindrada):
        self.preco = preco
        self.placa = placa
        self.cor = cor
        self.marca = marca
        self.velocidade_media = velocidade_media
        self.cilindrada = cilindrada


# Administradores:
class Funcionario:

    def tempo_de_empresa(self):
        time = datetime.now() - timedelta(days=self.dias_de_empresa)
        return time.isoformat()


class Gerente(Funcionario):

    def __init__(self, id, nome, dias_de_empresa):
        self.funcionario_id = id
        self.nome = nome
        self.dias_de_empresa = dias_de_empresa    

    def autorizar_desconto(self, forma_de_pagamento, parcelamento):
        if forma_de_pagamento in ['dinheiro', 'debito'] and parcelamento == 'a vista':
            return True
        
    def autorizar_compra(self, veiculo, preco_venda):
        preco_aceito_compra = veiculo.preco - (veiculo.preco * 0.2)
        if preco_venda >= preco_aceito_compra:
            return True 


class Vendedor(Funcionario):

    def __init__(self, id, nome, dias_de_empresa):
        self.funcionario_id = id
        self.nome = nome
        self.dias_de_empresa = dias_de_empresa 

    def vender_veiculo(self, cliente, veiculo):
        if cliente.carteira >= veiculo.preco:
            return True

    def comprar_veiculo(self, cliente, veiculo, gerente):
        if gerente.autorizar_compra:
            cliente.carteira += veiculo.preco
            return cliente.carteira


class Caixa(Funcionario):

    def __init__(self, id, nome, dias_de_empresa):
        self.funcionario_id = id
        self.nome = nome
        self.dias_de_empresa = dias_de_empresa 
        self.valor_em_caixa = 0

    def receber_pagamento(self, vendedor, cliente, veiculo):
        if vendedor.vender_veiculo():
            cliente.carteira -= veiculo.preco
            self.valor_em_caixa += veiculo.preco
            veiculo.vendido = True
            return f'Veiculo: {veiculo.marca} {veiculo.cor} {veiculo.placa} vendido por {veiculo.preco} vendido!'
    
    def fazer_pagamento(self, vendedor, cliente, veiculo, preco):
        if vendedor.comprar_veiculo():
            self.valor_em_caixa -= preco
            cliente.carteira += preco
            veiculo.vendido = True
            return f'Veiculo: {veiculo.marca} {veiculo.cor} {veiculo.placa} vendido por {veiculo.preco} vendido!'
            

class Cliente:

    def comprar_veiculo(self, marca, cor, preco, veiculo):
        preco = veiculo.preco - (veiculo.preco * self.porcentagem_desconto)
        if veiculo.marca == marca and veiculo.cor == cor and veiculo.preco <= preco:
            return True

    def vender_veiculo(self, veiculo, preco):
        if veiculo.preco <= preco:
            return True

class ClienteGold(Cliente):

    def __init__(self, carteira):
        self.carteira = carteira
        self.porcentagem_desconto = 0.10


class ClienteVip(Cliente):

    def __init__(self, carteira):
        self.carteira = carteira
        self.porcentagem_desconto = 0.15
