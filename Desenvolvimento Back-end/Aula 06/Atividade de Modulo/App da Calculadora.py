import Calculadora

print("1.Soma \n2.Subtração \n3.Multiplicação \n4.Divisão")
opcao = input("Escolha a operação: ")

n1 = float(input("Digite o valor 1: "))
n2 = float(input("Digite o segundo número: "))

match opcao:
  case '1':
    print('Soma: ',Calculadora.soma(n1,n2))
  case '2':
    print('Subtração: ',Calculadora.subtracao(n1,n2))
  case '3':
    print('Multiplicação: ',Calculadora.multiplicacao(n1,n2))
  case '4':
    print('Divisão: ',Calculadora.divisao(n1,n2))
  case _:
    print("Tente de novo!")