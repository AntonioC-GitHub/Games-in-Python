import random

name = input("What is your name?")

print("You are going down  ", name)

choices = ["hands", "cakes", "bullet", "pies", "pizza"]

computer = random.choice(choices)
print("Welcome to guess the word")

guesses = ''
turns = 10


while turns > 0:
    failed = 0
    for char in computer:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed =+ 1
    if failed == 0:
        print("You Win", " the Word is: ", computer)
        break

    print()
    guess = input("Guess a letter for the word I am thinking of").lower()

    guesses += guess

    if guess not in computer:
        turns -= 1
        print("Wrong")
        print("You have ", + turns, "more guesses left.")

        if turns == 0:
            print("You lose.")
            print("The word was, ", computer)
            break
