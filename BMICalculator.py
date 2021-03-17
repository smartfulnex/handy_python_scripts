print("Welcome to the BMI calculator\n")
height = float(input("Kindly Enter your height\n"))
weight = int(input("Kindly Enter your weight\n"))

bmi_data = int(weight) / float(height ** 2)
# bmi = float(bmi_data,2)
print(bmi_data)

if bmi_data < 18.5:
    print(f"Your BMI is {bmi_data} You're underweight")
elif bmi_data < 25:
    print("You have a normal weight dear")
elif bmi_data < 30:
    print("You are overweight dear")
elif bmi_data < 35:
    print("You are a obese dear")
else: 
    print("you are clinically obese")