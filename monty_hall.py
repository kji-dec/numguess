from random import shuffle, choice

simul = 1000

door = [0, 0, 1]

for _ in range(simul):
    shuffle(door)
    user_choice = choice(door)