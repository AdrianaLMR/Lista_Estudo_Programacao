# ESTRUTURAS DE CONTROLE
print('IF / Elif / Else');
idade: int = 18;

if idade <= 18: #  Executa um bloco de código se a condição for verdadeira.
    print('Você é menor de idade');
elif idade >= 18: # Checa múltiplas condições.
    print('Você é maior de idade');
else: # Executa um bloco de código se a condição do if for falsa.
    print('Você é adulto');


print('For');
frutas = ['maçã', 'banana', 'laranja'];

for fruta in frutas:  # Itera sobre uma sequência (lista, string, intervalo) / Executa um bloco de código para cada item na sequência.
    print(fruta);

print('While');
n = 0;

while n < 5: # Continua enquanto a condição for verdadeira.
    print(n);
    n += 1;