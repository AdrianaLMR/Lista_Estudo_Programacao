#OPERADORES RELACINAIS
print('--' * 5);
print('OPERADORES RELACIONAIS');
print('--' * 5);

# == (igual)
n1 = 10;
n2 = 100;
comparacacao = n1 == n2;
print('O número {} é igual ao número {}? RESULTADO: {}'.format(n1, n2, comparacacao));

print('--' * 5);

# != (diferente)
senha: str = 'srhd34@';
senha_digitada = str(input('Digite a senha: '));
if senha != senha_digitada: 
    print('Senha incorreta');
else: 
    print('Sucesso! Senha correta.');

print('--' * 5);

# > (maior que)
idade = int(input('Digite sua idade: '));
if idade > 60:
    print('Você ja pode se aposentar');
else:
    print('Você ainda não pode se aposentar');

print('--' * 5);

# < (menor que)
idade = int(input('Digite sua idade: '));
if idade < 18:
    print('Você não pode beber');
else:
    print('Você ja pode beber');

print('--' * 5);

# >= (maior ou igual)
altura: float = 1.50;
altura_permitida: float = 1.60;
if altura >= altura_permitida:
    print('Você pode ir na montanha-russa.');
else:
    print('Você não pode ir na montanha-russa.');

print('--' * 5);

# <= (menor ou igual)
valor_produto: int = 100; 
if valor_produto <= 50:
    print('o produto está barato, vale a pena comprar.');
else:
    print('o produto está barato, vale a pena comprar.');

print('--' * 5);