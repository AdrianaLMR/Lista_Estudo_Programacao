#Funções
# Definição: Bloco de código que realiza uma tarefa específica.

# Argumentos: Dados passados para a função.

# Retorno: Valor que a função devolve.

# Escopo de Variáveis: Variáveis definidas dentro de uma função são locais a ela; fora da função, são globais.

def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)  # Saída: 5

# O texto e a string dentro da função verificar_cor são parte de uma docstring, que é uma forma de documentar o propósito e o uso da função. 
# A docstring é escrita dentro de aspas triplas e fica logo após a definição da função.

#Definição da função
def calcular_desconto(valor_compra: float, estudante: bool) -> float: # Anotação de tipo que indica o tipo de valor que a função irá retornar.
    """
    Calcula o valor do desconto com base no valor da compra e na condição de ser estudante.
    
    :param valor_compra: O valor total da compra.
    :param estudante: Indica se a pessoa é estudante (True ou False).
    :return: O valor do desconto.
    """

    # Taxa de desconto para estudantes
    desconto_estudante = 0.10  # 10% de desconto para estudantes

    # Taxa de desconto para compras acima de 100
    desconto_compra = 0.05  # 5% de desconto para compras acima de R$100

    # Calcula o desconto baseado nas condições 
    if estudante:
        desconto = valor_compra * desconto_estudante
    elif valor_compra > 100:
        desconto = valor_compra * desconto_compra
    else:
        desconto = 0
    
    return desconto # retorna o valor do desconto calculado

# Testando a função
valor_compra = 150
estudante = True

valor_desconto = calcular_desconto(valor_compra, estudante)
print("O valor do desconto é: R${:.2f}".format(valor_desconto))
