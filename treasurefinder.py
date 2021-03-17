row1 = ["👋","👋","👋"]
row2 = ["👋","👋","👋"]
row3 = ["👋","👋","👋"]

map = [row1,row2,row3]

userInput = input("Where do you want to put the Treasure: ")
horizontal = int(userInput[0])
vertical = int(userInput[1])

selected_row = map[horizontal - 1]
selected_row[vertical - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

