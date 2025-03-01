# Write a Python program to do arithmetical operations addition and division

num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))

sum = num1 + num2
print(f"Sum of {num1} + {num2} = {sum}")

diff = num1 - num2
print(f"Sum of {num1} - {num2} = {diff}")

mul = num1 + num2
print(f"Sum of {num1} * {num2} = {mul}")

if num2 > 0:
    div = num1 / num2
    print(f"Sum of {num1} / {num2} = {div}")
else:
    print("Please enter 2nd number greater th10an 0")
