#2. Crie um programa em python que solicite um número qualquer. Nele, criem duas funções, uma para calcular o quadrado do número digitado e outra para imprimir o resultado.
num = int(input('Digite qualquer valor: '))
def calcular(numero): return num**2
  
def printResult(resultado):
  print('Resultado do quadrado do número digitado: ', calcular(num))
quadrado = calcular(num)
printResult(quadrado)