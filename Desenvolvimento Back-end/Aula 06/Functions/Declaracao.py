# Forma 1 de Declarar Função:
def mostrarPrint():
  print("Bora codar!")

mostrarPrint()

#Forma 2
def mostrarPrint2():
  return "Código executado!"

print(mostrarPrint2())

####Aplicação de exemplo
num1 = float(input("Valor 1: "))
num2 = float(input("Valor 2: "))
def somaNumeros():
  soma = num1+num2
  print('Soma: ', soma)
somaNumeros()


#-----PARÂMETROS
def digite_nome(nome):
  print('O nome é: ',nome)
nome = input("Teu nome: ")
digite_nome(nome)

#Com valor padrão, caso o user n digite nada
def digite_nome(nome='Oi!'):
  print('O nome é: ',nome)
nome = input("Teu nome: ")
digite_nome()

# ------Com Return
def recebe_numero(numero1, numero2):
  soma = numero1 + numero2
  return soma
n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))
print('Resultado: ',recebe_numero(n1,n2))