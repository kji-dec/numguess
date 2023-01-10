from random import randint
from time import sleep

#Generate random number
answer = randint(1, 100)

# Get user name
user = input("What\'s your name?\n")

# Say hello to user
print(f"Hello, {user}!")

# Get user's guessing gnumber
guess = input("Guess random number : ")

# Print user's guess
print(f"You guessed {guess} as random number!")

# Compare answer with user's guess
if guess == answer:
    print("**************************")
    sleep(1)
    print("**************************")
    sleep(1)
    print("**************************")
    sleep(1)
    print(f"You got the right answer! the answer was {answer}!")
else:
    print(f"~~XD~~ You got the wrong answer~~ the answer was {answer} :-P")