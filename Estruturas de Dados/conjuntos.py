# CONJUNTOS são estruturas de dados que armazenam coleções de elementos únicos.

# Um conjunto é uma coleção de elementos onde:
# Não há duplicatas: Um conjunto não pode conter elementos repetidos. Se você tentar adicionar um elemento que já existe, ele não será adicionado novamente.
# Ordem não é garantida: Os elementos em um conjunto não têm uma ordem específica. Portanto, você não pode acessar elementos por índice.
# Mutabilidade: Em Python, os conjuntos são mutáveis, o que significa que você pode adicionar e remover elementos depois de criar o conjunto.

print('--' * 10)
print('CONJUNTOS')
meu_conjunto = {1, 2, 3, 4}
meu_conjunto.add(5) #Adiciona elemento

print('Conjunto usando chaves: {}'.format(meu_conjunto))

print('--' * 10)
conjunto = {1, 2, 3, 4}

 # Remove um elemento específico do conjunto. Se o elemento não estiver presente no conjunto, o método não faz nada e não levanta uma exceção.
conjunto.discard(2)

# Verificar Membro:
membro_4 = 4 in conjunto  # Deve retornar True
membro_5 = 5 in conjunto  # Deve retornar False

print('Conjunto usando função set(): {}'.format(conjunto))
print('O número 4 está no conjunto? {}'.format(membro_4))
print('O número 5 está no conjunto? {}'.format(membro_5))

print('--' * 10)
# A função set() também pode ser usada para converter outras coleções, como listas ou tuplas, em conjuntos.
conjunto_float = set([1.8, 3.6, 5.6, 7.8])

#  Remove um elemento específico do conjunto. Se o elemento não estiver presente no conjunto, o método levanta uma exceção KeyError.
conjunto_float.remove(3.6)
# conjunto_float.remove(2) #exceção KeyError
print('Conjunto: {}'.format(conjunto_float))

print('--' * 10)
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}
conjunto1.update(conjunto2) # Atualizar com outro conjunto
conjunto1.intersection(conjunto2)

print('Conjunto após atualizar com conjunto2: {}'.format(conjunto1))

print('--' * 10)
conjunto_clean = {1, 2, 3, 4}
conjunto_clean.clear() # Remove todos os elementos do conjunto
print(conjunto_clean)  # Saída: set()

print('--' * 10)
conjunto_x = {1, 2, 3}
conjunto_y = {2, 3, 4}

# Retorna a interseção de dois conjuntos (elementos comuns).
print('Retorna a interseção de dois conjuntos: {}'.format(conjunto_x.intersection(conjunto_y)))

# Retorna a diferença entre dois conjuntos (elementos em conjunto1 que não estão em conjunto2).
print('Retorna a diferença entre dois conjuntos: {}'.format(conjunto1.difference(conjunto2)))  

# Retorna a diferença simétrica entre dois conjuntos (elementos que estão em um dos conjuntos, mas não em ambos).
print('Retorna a diferença simétrica de dois conjuntos: {}'.format(conjunto1.symmetric_difference(conjunto2)))

# Verifica se todos os elementos do conjunto estão em outro conjunto.
print('Retorna True se todos os elementos do conjunto estão em outro conjunto: {}'.format(conjunto1.issubset(conjunto2)))

# Verifica se o conjunto contém todos os elementos de outro conjunto.
print('Retorna True se o conjunto contém todos os elementos de outro conjunto: {}'.format(conjunto1.issuperset(conjunto2)))