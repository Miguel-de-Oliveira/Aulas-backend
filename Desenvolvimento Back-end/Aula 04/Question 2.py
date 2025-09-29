team = input("Choice the team: ")
match team.lower():
  case "sport":
    print("The team has 46 titles. ")
  case "santa":
    print("The team has 21 titles.")
  case "nautico":
    print("The team has 17 titles.")
  case _:
    print("Something is wrong, Try again.")