nome = 'Evandro Moura' 
altura = 1.95
peso = 155
imc = peso / (altura * altura) 

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

"f strings"

print(nome, 'tem', altura, 'de altura', )
print('pesa', peso, 'quilos e seu imc é',)
print(imc)
print(linha_1)
print(linha_2)
print(linha_3)