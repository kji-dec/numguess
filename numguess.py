from random import randint
from time import sleep


def gen_answer(start, end) -> int:
    # Generate random number
    answer = randint(start, end + 1)

    return answer

def get_user() -> str:
    # Get user name
    user = input("What's your name?\n")

    # Say hello to user
    print(f"Hello, {user}!")

    return user

def game(answer):
    # Get user's guessing number
    guess = int(input("Guess random number(1-100) : "))

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
    # To give hint to user, compare which is larger (guess, answer)
    elif guess > answer:
        print("Your guess is larger than the answer")
    else:
        print("Your guess is smaller than the answer")

def main():
    pass


if __name__ == "__main__":
    main()