import random

states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]

print(states_of_america[2])

states_of_america.append("Nigeria")

namesAsCSV = input("Give me everybody's names, separated by a space and comma: \n")
names = namesAsCSV.split(", ")
# print(len(names))

random_index = random.randint(0, len(names) - 1)

payer = names[random_index]
print(f"{payer} is going to buy the meal today")