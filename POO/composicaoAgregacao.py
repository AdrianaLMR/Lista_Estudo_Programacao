# Composição e Agregação
# Ambos representam a ideia de que uma classe pode ser composta de outras classes, mas diferem na maneira como essa relação
#  é estabelecida e mantida.
print('Composição')
# A composição é um tipo de relacionamento onde uma classe (a “classe pai” ou “todo”) é composta por outras classes 
# (as “classes filhas” ou “partes”). A ideia é que as partes só existem enquanto o todo existir. Se o objeto “todo” for destruído, os
#  objetos “parte” também serão destruídos.

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor("V8")  # Composição: O carro contém um motor

    def exibir_info(self):
        return f"Carro: {self.modelo}, Motor: {self.motor.tipo}"

# Criando um objeto Carro
carro = Carro("Fusca")

# Exibindo as informações do carro
print(carro.exibir_info())


print('Agregação')
# É um relacionamento mais fraco onde uma classe (o todo) pode conter
#  outras classes (as partes), mas essas partes podem existir independentemente do todo.

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor  # Agregação: O carro tem um motor, mas o motor pode existir fora do carro

    def exibir_info(self):
        return f"Carro: {self.modelo}, Motor: {self.motor.tipo}"

# Motor pode existir separadamente
motor_v8 = Motor("V8")
carro = Carro("Mustang", motor_v8)
