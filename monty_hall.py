from random import shuffle, choice

simul = 1000

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