from random import randint

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

# Print answer
print(f"The random number was {answer}!")
