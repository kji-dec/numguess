from random import shuffle, choice


simul = int(input("Enter some num (100 - 10000) to simulate: "))

door = [0, 0, 1]
result_win = {"changed": 0, "not_changed": 0}

for _ in range(simul):
    shuffle(door)
    user_choice = choice(door)

    # user changed choice
    if user_choice == 0:
        result_win["changed"] += 1

    # user didn't change choice
    if user_choice == 1:
        result_win["not_changed"] += 1

print(f"""{simul} times of simulation
    you won {result_win["changed"]} times when you changed your choice. ({result_win["changed"] / simul}%)
    you won {result_win["not_changed"]} times when you didn't changed your choice. ({result_win["not_changed"] / simul}%)
    """)
