#3. Crie um programa que o usuário calcule o valor a ser pago na loja de acordo com as #condições de pagamento:
#• À vista (dinheiro/pix): 10% de desconto
#
#• À vista (cartão): 5% de desconto
#
#• 2x no cartão: 5% de acréscimo
#
#• 3x até 10x no cartão: 10% de acréscimo

valorDaCompra = int(input("Digite o valor da compra: "))
print('''

\033[1;32;0mFORMAS DE PAGAMENTO:\033[m

\033[1;1;41m[1]\033[m À vista (dinheiro/pix) \033[1;32m(10% de desconto)\033[m

\033[1;1;41m[2]\033[m À vista no cartão \033[1;32m(5% de desconto)\033[m

\033[1;1;41m[3]\033[m 2x no cartão \033[1;33m(5% de acréscimo)\033[m

\033[1;1;41m[4]\033[m 3x até 10x no cartão \033[1;33m(10% de acréscimo)\033[m

\033[1;31mQual forma de pagamento? \033[m
      ''')
opcao = int(input("Digite a opção desejada: "))

match opcao:
  case 1:
    conta = (valorDaCompra)-(valorDaCompra*(10/100))
    print(f"O valor a ser pago é de R${conta}")
  case 2:
    conta = (valorDaCompra)-(valorDaCompra*(5/100))
    print(f"O valor a ser pago é de R${conta}")
  case 3:
    conta = (valorDaCompra*(5/100))+(valorDaCompra)
    print(f"O valor a ser pago é de R${conta}")
  case 4:
    conta = (valorDaCompra*(10/100))+(valorDaCompra)
    print(f"O valor a ser pago é de R${conta}")
  case _:
    print("Opção inválida")