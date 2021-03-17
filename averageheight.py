student_heights = input("Input a list of student heights ").split()


for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

lenght = 0
total_height = 0
for height in student_heights:
    total_height += height 
    lenght+=1
# print(add) print(plus_new)
average = total_height / add
average = int(average)
print(f"\nAverage heights = {average}")
