# bounce.py
#
# Exercise 1.5
initial_height = 100
num_bounces, cur_height = 0, initial_height

while num_bounces < 10:
    num_bounces += 1
    cur_height *= 0.6

    print(f"{num_bounces} {round(cur_height, 4)}")