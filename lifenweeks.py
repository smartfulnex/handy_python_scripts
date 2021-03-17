user_age = input("What's your current age: \n")
years_left = int(90) - int(user_age) 
# print(years_left)

months_left = int(years_left) * int(12)
days_left = int(years_left) * int(365)
weeks_left = int(years_left) * int(52)

print(f"You have {days_left} Days, {weeks_left} Weeks and {months_left} Months Left to live")