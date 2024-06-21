import random
print("Welcome to Rock, Paper, Scissors")
print("1. Rock")
print("2. Paper")
print("3. Scissors")
score=0
play = "1"
while(play=="1"):
    choose = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ")
    if choose == "1":
        print("You chose Rock")
    elif choose == "2":
        print("You chose Paper")
    elif choose == "3":
        print("You chose Scissors")
    else:
        print("Invalid Input")

    computer = random.randint(1, 3)
    if computer == 1:
        print("Computer chose Rock")
    elif computer == 2:
        print("Computer chose Paper")
    else:
        print("Computer chose Scissors")
    if choose == "1" and computer == 1:
        print("It's a tie")                             
    elif choose == "1" and computer == 2:
        print("You lose")
    elif choose == "1" and computer == 3:
        print("You win")
        score+=1
    elif choose == "2" and computer == 1:
        print("You win")
        score+=1
    elif choose == "2" and computer == 2:
        print("It's a tie")
    elif choose == "2" and computer == 3:
        print("You lose")
    elif choose == "3" and computer == 1:
        print("You lose")
    elif choose == "3" and computer == 2:
        print("You win")
        score+=1
    elif choose == "3" and computer == 3:
        print("It's a tie")
    print("Your score is: ",score)
    
    play = input("Enter 1 to play again, 0 to quit: ")
print("Game Over")
