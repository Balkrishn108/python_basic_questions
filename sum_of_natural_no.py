# Write a Python Program to Find the Sum of Natural Numbers.
limit = int(input("Enter limit of natural number : "))
sum = 0
for i in range(1,limit+1):
    sum +=i
print(f"Sum of all natural number from 1 to {limit} is = {sum}")