# OPERADORES LÓGICOS
print('--' * 10);
print('OPERADORES LÓGICOS');
print('--' * 10);

# Operador AND : Retorna True se ambas as condições forem verdadeiras. Caso contrário, retorna False.
print('OPERADORE AND');
a: int = 10;
b: int = 5;
resultado = (a > 5) and (b < 10);
print(resultado);  
print('--' * 10);

# Operador OR : Retorna True se pelo menos uma das condições for verdadeira. Retorna False se todas as condições forem falsas.
print('OPERADORE OR');
x: int = 10;
z: int = 50;
result1 = (x > 5) or (z < 10);
print(result1);
print('--' * 10);

# Operador NOT :  Inverte o valor booleano da condição. Retorna True se a condição for falsa e False se a condição for verdadeira.
print('OPERADORE NOT');
verdadeiro: bool = True;
inversao = not verdadeiro;
print('Valor original: {}'.format(verdadeiro))
print('Valor invertido: {}'.format(inversao))
print('--' * 10);

#Operadores Lógicos em Condições Compostas: Operadores lógicos usados para combinar múltiplas condições em estruturas de controle.
print('OPERADORES LÓGICOS EM CONDIÇÕES COMPOSTAS');
idad: int = 22;
tem_ingresso: bool = True;
amigo_convidado: bool = False;

# Usando o operador `or` para verificar se a pessoa pode entrar no clube
pode_entrar = (idad >= 18 and tem_ingresso) or amigo_convidado;

if pode_entrar:
    print("Você pode entrar no clube.");
else:
    print("Você não pode entrar no clube.");
