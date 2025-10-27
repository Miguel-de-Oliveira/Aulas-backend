def converter(lista_de_String):

  listaInt = []
  for valor in lista_de_String:
    try:
      listaInt.append(int(valor))
    except ValueError:
      print(f"Erro: Não foi possível converter '{valor}' para inteiro. Ignorando.")
  return listaInt

# Example usage:
listaString = []

numeros = input('Digite números: ')

while numeros != '':
  listaString.append(numeros)
  numeros = input('Digite números: ')
else:
  print('Fim da digitação')

print("Lista original:", listaString)
print("Lista convertida:",converter(listaString))