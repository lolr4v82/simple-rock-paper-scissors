import random
while True:
  plG = input("1, 2, 3 (Rock, Paper or Scissors): ")
  comG = random.randint(1, 3)
  plG = int(plG)
  
  if comG == 1:
    if plG == 1:
      print("It's a draw!")
    if plG == 2:
      print("You won! Paper -> Rock")
    if plG == 3:
      print("You lost! Scissors -> Rock")
  if comG == 2:
    if plG == 1:
      print("You lost! Rock -> Paper")
    if plG == 2:
      print("It's a draw!")
    if plG == 3:
      print("You won! Scissors -> Paper")
  if comG == 3:
    if plG == 1:
      print("You won! Rock -> Scissors")
    if plG == 2:
      print("You lost! Paper -> Scissors")
    if plG == 3:
      print("It's a draw!")
