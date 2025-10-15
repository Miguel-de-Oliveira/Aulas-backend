#2. Crie um programa que o usuário digite duas notas e apareça uma mensagem informando se ele foi:
#• APROVADO: nota superior a 7.0
#• RECUPERAÇÃO: nota entre 5.0 e 6.9
#• REPROVADO: nota abaixo de 5.0

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media >=7:
  print("\033[0;1;42mAPROVADO!\033[m")
elif media >=5:
  print("\033[1;30;43mRECUPERAÇÃO!\033[m")
else:
  print("\033[0;1;41mREPROVADO!\033[m")