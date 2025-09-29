# 1. Crie um programa em python que possua 2 funções que receba 5 valores inteiros, determine e imprima:
# a) Em uma função, a soma dos números positivos;
# b) Em uma segunda função, a quantidade de valores negativos;

def somaPositivos(valor):
  soma = 0
  for num in valor:
    if num > -1:
      soma +=num
  return soma

def contarNegativo(valor):
  negativo = 0
  for num in valor:
    if num < 0 :
      negativo += 1
  return negativo

valor = []
for i in range(1,6):
  inserirValor = int(input(f'Digite o {i}º valor: '))
  valor.append(inserirValor)

print('Resultado da soma dos positivos: ',somaPositivos(valor))
print('Quantidade de nº negativos', contarNegativo(valor))