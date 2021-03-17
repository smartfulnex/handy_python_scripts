is_even = 0
total_evens = 0
for numbers in range(1, 100+1):
    is_even = numbers % 2
    if is_even == 0:
        total_evens += numbers
print(f"Total even numbers is {total_evens}")