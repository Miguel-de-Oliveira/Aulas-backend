option = input("Digite a opção: ")

match option.lower():
  case "kloud":
    print("Gênero Eletrônica, subgênero hardtechno")
  case "miss monique":
    print("Gênero Eletrônica, subgênero progressive e melodic")
  case "avoure":
    print("Gênero Eletrônica, subgênero Deep melodic")
  case _:
    print("Try again.")