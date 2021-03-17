user_number = int(input("Welcome to the Odd or Even number checker.\n Kindly enter a value: "))
modulo_value = int(user_number) % 2

if modulo_value == 0:
    print(f"{user_number} is an Even number!") 
else:
    print(f"{user_number} is an Odd number!")
# print(user_number)