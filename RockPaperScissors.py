import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    player = input("rock paper or scissors").lower()
    if player == "rock":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("It is a tie!")
            print("-----------------------------")
        elif computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer Wins!")
            break
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win!")
            break
    elif player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("The Computer Wins!")
            break
        elif computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You Win !")
            break
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Its a Tie!")
            print("--------------------")
    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win!")
            break
        elif computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("its a Tie!")
            print("------------------------------")
        elif computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("The Computer Wins")
            break
