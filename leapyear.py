userinput = int(input("Which year do you want to check?\n"))

moduld = int(userinput % 4)
moduld1 = int(userinput % 100)
moduld2 = int(userinput % 400)
new = int(0)

if moduld == 0:
    new+=1
    if moduld1 != 0:
        new+=1
    if moduld2 == 0:
        new+=1
    
if new == 2:
   print(f"{userinput} is a leap year because it has no remainder")

else:
   print(f"{userinput} is not a leap year because it has a remainder")