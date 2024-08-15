# LISTAS
print('--' * 10)
print('LISTAS')
print('--' * 10)

numeros = [1, 2, 3, 4]
print('Lista números: {}'.format(numeros))

mista = [ 1, 'text', True, 2.9]
print('Lista mista: {}'.format(mista))

print('--' * 10)

# MÉTODOS
print('Métodos')

# Criando uma lista inicial
frutas = ['maçã', 'banana', 'laranja']

print("Lista original:", frutas)

# Adicionando um item ao final
frutas.append('manga')
print("Após append:", frutas)

# Adicionando todos os itens de outra lista
outras_frutas = ['kiwi', 'morango']
frutas.extend(outras_frutas)
print("Após extend:", frutas)

# Inserindo um item na posição 2
frutas.insert(2, 'cabeludo')
print("Após insert:", frutas)

# Removendo um item (primeira ocorrência de 'banana')
frutas.remove('banana')
print("Após remove:", frutas)

# Removendo e retornando o item na posição 3
item_removido = frutas.pop(3)
print("Item removido:", item_removido)
print("Após pop:", frutas)

# Ordenando a lista
frutas.sort()
print("Após sort:", frutas)

# Invertendo a lista
frutas.reverse()
print("Após reverse:", frutas)

print('--' * 10)

# COMPREENSÃO DE LISTAS / forma compacta de criar listas a partir de outras listas ou iteráveis.
#  Elas permitem gerar novas listas aplicando uma expressão a cada item de um iterável, como uma lista, tupla ou range.
print('COMPREENSÃO DE LISTAS')
numeros = [0, 1, 2, 3, 4] # Criando uma lista com os números de 0 a 4
dobrados = [x * 2 for x in numeros] # Usando compreensão de listas para criar uma nova lista com cada número multiplicado por 2

print(dobrados)