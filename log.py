import math
num = float(input("Enter +ve number : "))
if num<=0:
    print("Enter a positive number ")
else:
    result = math.log(num)
print(f"Logrithm of {num} is = {result}")