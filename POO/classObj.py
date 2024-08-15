#POO
# Programação Orientada a Objetos (POO) é um paradigma de programação que utiliza "objetos" e "classes" para organizar e estruturar o código
#  de forma que simule o comportamento do mundo real. A ideia principal é modelar o sistema em termos de objetos que interagem entre si.

print('Classes e Objetos')

# Objetos: São uma instância de uma classe. Quando você cria um objeto, está instanciando a classe com valores específicos para seus atributos.
# Classes: São como os projetos ou moldes para criar objetos. Elas definem as características e comportamentos que os objetos/ PascalCase
# Self é um nome convencionalmente utilizado em métodos de uma classe para referenciar o objeto que está executando o método. 
    #  É um parâmetro que não precisa ser explicitamente passado quando você chama um método em um objeto;

# Definindo a classe Carro
class Carro:
    """
    Representa um carro com informações básicas e um método para descrever o carro.

    Atributos:
    - marca (str): A marca do carro.
    - modelo (str): O modelo do carro.
    - ano (int): O ano de fabricação do carro.

    Métodos:
    - __init__: Inicializa um novo objeto da classe Carro.
    - descrever: Retorna uma descrição do carro no formato 'marca modelo (ano)'.
    """
    def __init__(self, marca, modelo, ano):
        """
        Inicializa um novo objeto da classe Carro.
        
        :param marca: A marca do carro (string).
        :param modelo: O modelo do carro (string).
        :param ano: O ano de fabricação do carro (inteiro).
        """
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descrever(self):
        """
        Retorna uma descrição do carro.
        
        :return: Uma string que descreve o carro no formato 'marca modelo (ano)'.
        """
        return f"{self.marca} {self.modelo} ({self.ano})"


# Criando objetos da classe Carro
carro1 = Carro("Ford", "Mustang", 2022)
carro2 = Carro("Chevrolet", "Camaro", 2021)

# Exibindo a descrição dos carros
print(carro1.descrever())  # Saída: Ford Mustang (2022)
print(carro2.descrever())  # Saída: Chevrolet Camaro (2021)

# Atributos de Classe e Instância
print('--' * 10)
print('Atributos de Classe e Instância')

# Atributos de Instância: São atributos específicos de um objeto. São definidos no método construtor (__init__) usando self.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

# Atributos de Classe: São atributos que são compartilhados por todas as instâncias de uma classe. Eles são definidos diretamente na classe, fora de qualquer método.
class Animal:
    especie = "Desconhecida"  # Atributo de classe

    def __init__(self, nome):
        self.nome = nome  # Atributo de instância

# Criando instâncias
animal1 = Animal("Leão")
animal2 = Animal("Tigre")

# Atributo de classe acessível por qualquer instância
print(animal1.especie)  # Saída: Desconhecida
print(animal2.especie)  # Saída: Desconhecida

# MÉTODOS
# São funções definidas dentro de uma classe que operam sobre os atributos da instância. Eles definem o comportamento dos objetos.
print('MÉTODOS')

class Nome:
    nome = 'Siclano'

    #Método __init__  Inicializa um novo objeto da classe Carro.
    def __init__(self, sobrenome: str):
        self.sobrenome = sobrenome

    def descrever(self) -> str:
        return "Nome completo: {} {}".format(self.nome, self.sobrenome)

pessoa = Nome('De Tal')

# Usando o método descrever
print(pessoa.descrever())