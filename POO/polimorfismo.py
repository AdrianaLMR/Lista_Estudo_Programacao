#Polimorfismo
# É é a capacidade de diferentes classes responderem ao mesmo método de maneiras diferentes, pode chamar o mesmo método em objetos de 
# diferentes classes e cada classe pode fazer algo diferente com esse método. 
# Existe duas formas de polimorfismo:Métodos Sobrescritos e Interfaces.

print('POLIMORFISMO')

# Classe base pagamento
class Pagamento:
    def processar(self):
        pass

# Subclasses tipos de pagmento

# Pagamento cartão de crédito
class CartaoCredito(Pagamento): # Pagamento está em maiúsculas, o que segue a convenção de nomenclatura de classes em Python.
    def __init__(self, numero_cartao, nome_titular):
        self.numero_cartao = numero_cartao
        self.nome_titular = nome_titular

    def processar(self):
        return 'Processando pagamento com cartão de crédito: {} - {} '.format(self.numero_cartao, self.nome_titular)

# Pagamento em dinheiro
class Dinheiro(Pagamento):
    def __init__(self, valor):
        self.valor = valor 

    def processar(self): # Pagamento está em minúsculas, conforme a convenção para nomes de variáveis e parâmetros em func
        return 'Processando pagamento em dinheiro: R${:.2f}'.format((self.valor))
    
def finalizar_pagamento(pagamento): # Pagamento está em minúsculas, conforme a convenção para nomes de variáveis e parâmetros
    print(pagamento.processar())

#Criando objs
pagamento_cartao = CartaoCredito("1234-5678-9101-1121", "Fulano de Tal")
pagamento_dinheiro = Dinheiro(150.00)

# Chama a mesma func com objs diferentes
finalizar_pagamento(pagamento_cartao)
finalizar_pagamento(pagamento_dinheiro)

print('--'* 10)
print('FORMAS DE POLIMORFISMO')

# Métodos Sobrescritos
# Ou "overriding" ocorre quando uma subclasse fornece uma nova implementação para um método que já foi definido na sua classe base (superclasse).
# Isso significa que, quando você chama o método no objeto da subclasse, a nova implementação é usada, não a da classe base.
print('Métodos Sobrescritos')
class CardapioBase:
    def fazer_pedido(self):
        # Método da classe base
        return "Escolha uma opção"

class Bebida(CardapioBase):
    def fazer_pedido(self):  # Sobrescrita do método
        return "Refrigerante."

class Comida(CardapioBase):
    def fazer_pedido(self):  # Sobrescrita do método
        return "Pizza."

# Criando objetos
bebida = Bebida()
comida = Comida()

# Chamando o método sobrescrito
print(bebida.fazer_pedido())  # Saída: Você escolheu refrigerante.
print(comida.fazer_pedido())  # Saída: Você escolheu pizza.


# Interfaces
# Uma interface é um "manual" que define quais métodos uma classe deve ter, mas não como esses métodos devem ser implementados. Seu objetivo é garantir que diferentes classes 
# sigam o mesmo "contrato", implementando os mesmos métodos com comportamentos específicos.

print('Interfaces')
from abc import ABC, abstractmethod

# Interface que define o contrato para notificações
class Notificacao(ABC):
    @abstractmethod
    def enviar(self):
        pass

# Implementação da interface para Notificação por E-mail
class NotificacaoEmail(Notificacao):
    def __init__(self, endereco_email, mensagem):
        self.endereco_email = endereco_email
        self.mensagem = mensagem

    def enviar(self):
        return f"Enviando e-mail para {self.endereco_email}: {self.mensagem}"

# Implementação da interface para Notificação por SMS
class NotificacaoSMS(Notificacao):
    def __init__(self, numero_telefone, mensagem):
        self.numero_telefone = numero_telefone
        self.mensagem = mensagem

    def enviar(self):
        return f"Enviando SMS para {self.numero_telefone}: {self.mensagem}"

# Função que usa polimorfismo para enviar notificações
def enviar_notificacao(notificacao: Notificacao):
    print(notificacao.enviar())

# Criando objetos
notificacao_email = NotificacaoEmail("exemplo@dominio.com", "Sua conta foi criada.")
notificacao_sms = NotificacaoSMS("+551199999999", "Sua conta foi criada.")

# Enviando notificações
enviar_notificacao(notificacao_email)  # Saída: Enviando e-mail para exemplo@dominio.com: Sua conta foi criada.
enviar_notificacao(notificacao_sms)    # Saída: Enviando SMS para +551199999999: Sua conta foi criada.
