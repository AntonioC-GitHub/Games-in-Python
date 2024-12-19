import random

my_list = list(range(100))

name = input("What is your name?")

print("GoodLuck ", name)

computer = str(random.choice(my_list))
print("Welcome to guess the number")

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
        print("You Win", " the number was: ", computer)
        break

    print()
    guess = input("Guess the number I am thinking of")

    guesses += guess

    if guess not in computer:
        turns -= 1
        print("Wrong")
        print("You have ", + turns, "more guesses left.")

        if turns == 0:
            print("You lose.")
            print("The word was, ", computer)
            break
