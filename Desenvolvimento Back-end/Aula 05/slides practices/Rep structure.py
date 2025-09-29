# Estrutura While Loop sintaxe
#usa para repetir o bloco de código enquanto for true.

#while condition:
  #code for execute while the condition is true


class Example1:
  contador = 1
  while contador <= 5:
    print(contador)
    contador += 1


#While with else
#Sintax:
#while condition:
  #code's block
#else:
  #code's block for execute when the condition is false

class Example2:
  count = 1
  while count <= 5:
    print(count)
    count +=1
  else:
    print(f"Variable : ", count)
    print(f"Final do loop while!")