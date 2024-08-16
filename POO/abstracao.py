# Abstração
# É como pegar um problema grande e complexo e dividi-lo em partes menores e mais simples.
print('--'* 10)
print('ABSTRAÇÃO')

#Exemplo de uso seguindo o menu número abaixo
# [1] IDENTIFICAR O PROBLEMA PRINCIPAL = Objetivo.
# Criando um sistema de gerenciamento de biblioteca. O objetivo é gerenciar livros, usuários e empréstimos.

# [2] DIVIDIR O PROBLEMA EM PEDAÇOS = Resolver individualmente.
# As partes principais são:
# 1. Gerenciar informações sobre livros.
# 2. Gerenciar informações sobre usuários.
# 3. Controlar o processo de empréstimo de livros.

# [3] DEFINIR O QUE CADA PARTE FAZ = Defina o que ela precisa fazer.

class Livro:
    def __init__(self, titulo, autor):  # [3] Inicializa um livro com título e autor.
        self.titulo = titulo
        self.autor = autor

    def exibir_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"  # [3] Retorna uma string com informações do livro.

class Usuario:
    def __init__(self, nome):  # [3] Inicializa um usuário com nome.
        self.nome = nome

    def exibir_info(self):  # [3] Retorna uma string com o nome do usuário.
        return f"Nome: {self.nome}"

class Emprestimo:
    def __init__(self, livro, usuario):  # [3] Inicializa o empréstimo com um livro e um usuário.
        self.livro = livro
        self.usuario = usuario

    def realizar_emprestimo(self):  # [3] Retorna uma string indicando que o usuário emprestou o livro.
        return f"{self.usuario.nome} emprestou '{self.livro.titulo}'"

# [4] CRIA REPRESENTAÇÕES SIMPLES = Use classes, métodos e interfaces para representar cada parte do problema.

# Criando objetos
livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")  # [4] Cria um objeto Livro com título e autor.
usuario = Usuario("João Silva")  # [4] Cria um objeto Usuario com nome.

# Realizando um empréstimo
emprestimo = Emprestimo(livro, usuario)  # [4] Cria um objeto Emprestimo com um livro e um usuário.

# Exibindo informações e realizando o empréstimo
print(livro.exibir_info())       # [4] Exibe informações do livro.
print(usuario.exibir_info())      # [4] Exibe informações do usuário.
print(emprestimo.realizar_emprestimo())  # [4] Exibe a mensagem de que o usuário emprestou o livro.

# Classes abstratas / Métodos abstratos.

print('--'* 10)
print('Classes Abstratas e Métodos abstratos')
#  Classes Abstratas: É uma classe que não pode ser instanciada diretamente e serve como um modelo para outras classes. Ela pode conter
#  métodos abstratos (que precisam ser implementados pelas subclasses) e métodos concretos *anotações
# (com uma implementação já definida). São usadas para definir uma interface comum para um grupo de classes relacionadas, 
# garantindo que todas as subclasses implementem certos métodos e atributos.

# Métodos abstratos: É um método que é declarado em uma classe abstrata, mas não possui uma implementação. As subclasses que herdam a classe 
# abstrata são obrigadas a fornecer uma implementação para o método abstrato.
# definem um contrato para as subclasses, obrigando-as a implementar esses métodos. Isso garante que todas as subclasses 
# terão um comportamento consistente para esses métodos.

from abc import ABC, abstractmethod

# A classe Veiculo herda de ABC (Abstract Base Class), tornando-a uma classe abstrata.
class Veiculo(ABC):
    # Método construtor que define o atributo 'modelo'.
    def __init__(self, modelo):
        self.modelo = modelo

    # Método abstrato 'mover' que deve ser implementado pelas subclasses.
    @abstractmethod
    def mover(self):
        pass

    # Método concreto 'exibir_modelo' que retorna o modelo do veículo.
    def exibir_modelo(self):
        return f"Modelo: {self.modelo}"

# A classe Carro e Bicicleta herdam de Veiculo e é obrigada a implementar o método abstrato 'mover'.
class Carro(Veiculo):
    def mover(self):
        return "O carro está se movendo."

class Bicicleta(Veiculo):
    def mover(self):
        return "A bicicleta está se movendo."

# Criando um objeto da classe Carro com o modelo 'Fusca' e Bicicleta com o modelo 'Caloi'
carro = Carro("Fusca")
bicicleta = Bicicleta("Caloi")

# Exibindo o modelo do carro e bicicleta e chamando o método 'mover'.
print(carro.exibir_modelo())
print(carro.mover())           
print(bicicleta.exibir_modelo())
print(bicicleta.mover())          
        

print('Métodos Abstratos')
# É um método que é declarado em uma classe abstrata, mas não possui uma implementação. As subclasses que herdam a classe 
# abstrata são obrigadas a fornecer uma implementação para o método abstrato.
# definem um contrato para as subclasses, obrigando-as a implementar esses métodos. Isso garante que todas as subclasses 
# terão um comportamento consistente para esses métodos.


