# Tuplas
# São coleções de itens que são imutáveis e ordenadas, permitem armazenar múltiplos valores em uma única variável.
# Não pode adicionar, remover ou alterar itens na tupla.

print('Tipo de tuplas')
numeros = (1, 2, 3, 4)
print(numeros)

mista = ( 1, True, 4.0, 'Text')
print(mista)

unica =  (20,)
print(unica)

vazia = ()
print(vazia)

print('--' * 10)
print('Acessando Itens')
num = (4, 6, 90)
primeiro_item = num[0]
ultimo_item = num[2]

print('Primeiro item {} / Último item {}'.format(primeiro_item, ultimo_item))

print('--' * 10)
print('Métodos')
frutas = ("maçã", "banana", "laranja", "maçã")

count_maca = frutas.count("maçã")  # Conta quantas vezes um item aparece na tupla.
print('Método count: {}'.format(count_maca))

index_banana = frutas.index("banana")  # Retorna o índice da primeira ocorrência de um item na tupla. Se o item não estiver presente, lança um erro.
print('Método index: {}'.format(index_banana))

# Desembalando Tuplas(ou "desempacotar") 
print('--' * 10)
print('Desembalando Tuplas')

#  Pode desembrulhar (ou "desempacotar") uma tupla para atribuir seus valores a variáveis individuais.
coordenadas = (10, 20)
x, y = coordenadas
print('Desempacotar Tuplas: {}, {}'.format(x, y))

# São úteis para armazenar dados que não devem ser alterados, como coordenadas ou registros fixos.
registro_pessoa = ("João", 30, "Engenheiro")
print('Registro de pessoa: {}'.format(registro_pessoa))

# Pode usá-las como chaves em dicionários, ao contrário das listas.
dicionario = {("A", 1): "Item 1", ("B", 2): "Item 2"}
print('Dicionário: {}'.format(dicionario))

# Funções podem retornar múltiplos valores agrupados em uma tupla.

def calcula_media(a, b):
    media = (a + b) / 2
    return media, media**2

# Receber múltiplos valores
media, media_quadrado = calcula_media(10, 20)

print("A média dos números é: {:.1f}".format(media))
print("O quadrado da média é: {:.1f}".format(media_quadrado))