import random
points=0
computerpoints=0
Aichoice=["rock","paper","scissors"]
print("Welcome to Rock, Paper, Scissors!")
while points<3 and computerpoints<3:
  Computer=random.choice(Aichoice)

  Choice=input("What do you choose? Rock, Paper or Scissors:").lower()
  if Choice == "rock" and Computer=="paper":
    print ("U lose")
    computerpoints +=1
  if Choice=="rock" and Computer=="scissors":
    print ("U win")
    points=+1
  if Choice=="rock" and Computer=="rock":
     print ("Draw")
  if Choice=="paper" and Computer=="paper":
      print ("Draw")
  if Choice=="paper" and Computer=="scissors":
      print ("U lose")
      computerpoints +=1
  if Choice=="paper" and Computer=="rock":
      print ("U Win")
      points +=1
  if Choice=="scissors" and Computer=="paper":
      print ("U Win")
      points+=1
  if Choice=="scissors" and Computer=="scissors":
      print ("Draw")
  if Choice=="scissors" and Computer=="rock":
      print ("U lose")
      computerpoints +=1
       
  if Choice not in Aichoice:
    print("Invalid input")
  print("You have",points,"points")
  print("The computer has",computerpoints,"points")
  if points==3:
    print("You Beat the computer")
  if computerpoints==3:
    print("The computer beat you!")