print("Welcome to the rollercoaster ride")

height= int(input("What is your height in cm? "))

if height >= 120:
    print("Nice! you can ride the rollercoaster") 
    age = int(input("What is your age?"))
    
    if age < 12:
        print("Please pay $5 only.")
    else:
        print("please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride")