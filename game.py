import random
import sys

points = 0
score = 0
win = 0
lose = 0
start = True

while start:
    try:
        win = int(input("How many points do you want to win with? "))
    except:
        print("Incorrect value!\n")
        continue
    try:
        lose = int(input("How many points should the Computer win with? "))
    except:
        print("Incorrect value!\n")
        continue
    start = False

while True:
    try:
        player = int(input("Choose Rock (1) Paper (2) or Scissors (3)! "))
    except:
        print("Incorrect value!\n")
        continue

    computer = random.randint(1, 3)
    computer_string = {
    1: "rock",
    2: "paper",
    3: "scissors"
    }
    
    if computer == player:
        print("Computer chose the same, tie!")
        print(f"Your Points = {points}")
        print(f"Computers Points = {score}\n")

    elif computer == 1 and player == 2 or computer == 2 and player == 3 or computer == 3 and player == 1:
        print(f"Computer chose {computer_string.get(computer)}, you win!")

        points += 1
        print(f"Your Points = {points}")
        print(f"Computers Points = {score}\n")

    elif computer == 1 and player == 3 or computer == 2 and player == 1 or computer == 3 and player == 2:
        print(f"Computer chose {computer_string.get(computer)}, you lose!")

        score += 1
        print(f"Your Points = {points}")
        print(f"Computers Points = {score}\n")
        
    else:
        print("Incorrect value!\n")

    if points == win:
        print("You win!")
    if score == lose:
        print("You lose...")

    if points == win or score == lose:
        replay = input("Do you want to play again? (y/n) ")

        if replay == 'y':
            points = 0
            score = 0
            
            print("Have fun! \n")
            start = True
        else:
            sys.exit()
