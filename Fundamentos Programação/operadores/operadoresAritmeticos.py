# OPERADORES ARITMÉTICOS 
print('--' * 5);
print('OPERADORES ARITMÉTRICOS');
print('--' * 5);
# SOMA +
print('SOMA');
n1 = int(input('Digite o primeiro número: '));
n2 = int(input('Digite o segundo número: '));
soma = n1 + n2;
print('Resultado da soma dos valores {} e {} é igual a {}'.format(n1, n2, soma));

# SUBTRAÇÃO -
print('SUBTRAÇÃO');
ano_nascimento = int(input('Digite o ano do seu nascimento: '));
ano_atual = int(input('Digite o ano atual: '));
idade = ano_atual - ano_nascimento;
print('Se você nasceu em {} e o ano atual é {} você tem {} anos'.format(ano_nascimento, ano_atual, idade));

# MULTIPLICAÇÃO *
print('MULTIPLICAÇÃO');
valor_produto = int(10);
quant_produto = int(input('Digite a quantidade de unidade do produto deseja: '))
valor = valor_produto * quant_produto;
print(' Valor do produto: {} \n Quantidade de uidades do produto: {}  \n Valor total da compra R${}'.format(valor_produto, quant_produto, valor));

# # DIVISÃO /
print('DIVISÃO');
conta = int(500);
pessoas_mesa = int(6);
conta_dividida = conta / pessoas_mesa;
print('A conta de {}, dividida entre {} é igual a {:.2f}'.format(conta, pessoas_mesa, conta_dividida));

#  DIVISÃO INTEIRA //
print('DIVISÃO INTEIRA');
heranca = int(15251);
filhos = 5;
divisao = heranca // filhos;
print('A Herança de {}, dividida igualmente entre os {} filhos é: {}'.format(heranca, filhos, divisao));

# EXPONENCIAÇÃO **
print('EXPONENCIAÇÃO');
numero = int(6)
raiz_quad = numero ** 2;
print('A raiz quadrada do número {} é igual a {}'.format(numero, raiz_quad));

# RESTO %
print('RESTO');
fatias_bolo = 5;
num_pessoas = 3
fatia_sobrando = 5 % 3; # result é 1
print('Vai restar {} fatia de bolo'. format(fatia_sobrando));