# ENCAPSULAMENTO
# Encapsulamento é uma técnica que permite esconder detalhes internos de um objeto e expor apenas o que é necessário para o exterior.
# Componentes: Atributos e Método.

print('ENCAPSULAMENTO')

# Atributos Privados / Marcados como privados, de forma que não possam ser acessados diretamente de fora da classe.

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado

    def get_nome(self):
        return self.__nome  # Método público para acessar o nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome  # Método público para modificar o nome

# Criando um objeto da classe Pessoa
pessoa = Pessoa("Maria")
print(pessoa.get_nome())  # Acesso ao atributo através do método público

pessoa.set_nome("Ana")
print(pessoa.get_nome())  # Acesso ao atributo através do método público

# Métodos Públicos e Privados
# Usados para interagir com o estado do objeto. Forncem a interface pela qual o código externo acessar e modificar os atributos do objeto. 
# Métodos privados (prefixo duplo) são usados internamente dentro da classe e não devem ser chamados fora da classe.

class Calculadora:
    def __init__(self):
        self.__resultado = 0

    def somar(self, valor):
        self.__resultado += valor  # Método público para realizar uma operação
        return self.__resultado

    def __resetar(self):  # Método privado para resetar o resultado
        self.__resultado = 0

    def obter_resultado(self):
        return self.__resultado

# Criando um objeto da classe Calculadora
calc = Calculadora()
print(calc.somar(10))  # Usando o método público
# print(calc.__resetar())  # Isso causará um erro porque __resetar é privado


# Propriedades 
# --> As propriedades permitem que os atributos (ou campos) de uma classe sejam acessados e modificados de forma controlada, através de métodos
#  especiais conhecidos como getters e setters. Esses métodos permitem que você "encapsule" o acesso aos atributos, ou seja, controle como os
#  dados internos da classe são lidos ou modificados.
# --> Getter (Acesso): Um método que retorna o valor de um atributo. Permite que o código externo leia o valor do atributo, mas de uma maneira controlada.
# --> Setter (Modificação): Um método que define ou altera o valor de um atributo. Permite aplicar validações ou outras regras antes de modificar o valor do atributo.

# A visibilidade dos atributos --> Modificadores de acesso: public, protected( apenas dentro da classe e em subclasses) e private. 

class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo privado

    # Getter(acesso) para o atributo 'nome'
    @property
    def nome(self):
        return self._nome

    # Setter(modificação) para o atributo 'nome'
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome:
            self._nome = novo_nome
        else:
            raise ValueError("O nome não pode ser vazio")

# Exemplo de uso
pessoa = Pessoa("Fulano")
print(pessoa.nome)  # Saída: João

pessoa.nome = "Beutrano"
print(pessoa.nome)  # Saída: Carlos

