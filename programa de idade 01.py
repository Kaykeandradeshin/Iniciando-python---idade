
import time 

print('Olá, Seja Bem Vindo!!!')
time.sleep(2)

print('Por favor responda as perguntas para calcularmos sua idade')

nasci = int(input('digite o ano que você nasceu:'))
atual = int(input('digite o ano atual:'))
mes = int(input('digite o mês que você nasceu:'))

result = atual - nasci

if mes >= 4:
    result = atual - nasci - 1

else:
    result = atual - nasci


print(f'você tem {result} anos')