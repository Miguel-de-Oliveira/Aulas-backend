lista = []
try:
  for i in range(1,3):
    numero = float(input(f'Digite o {i}° número: '))
    lista.append(numero)

  for i in lista:
    resultado = i/i+1
  print('Resultado: ', resultado)
except ValueError:
  print('Somente aceitamos valores numéricos')
except ZeroDivisionError:
  print("Não pode dividir valores por zero")
else:
  print('Código executado com sucesso!')
finally:
  print('End of line')