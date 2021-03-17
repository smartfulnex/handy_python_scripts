import random
# c = random.randint(100,200)
# print(c)
# 
# random_float = random.random()
# print(random_float)

seed_input = int(input("Create a seed number: "))
seed = random.seed(seed_input)

random_checker = random.randint(0,1)
if random_checker == 1:
    print("Heads")
else: print ("Tails")
