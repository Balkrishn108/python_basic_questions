# Write a Python program to solve quadratic equation
import math
a=float(input("Enter value of a : "))
b=float(input("Enter value of b : "))
c=float(input("Enter value of c : "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c
# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
 # Two real and distinct roots
 root1 = (-b + math.sqrt(discriminant)) / (2*a)
 root2 = (-b - math.sqrt(discriminant)) / (2*a)
 print(f"Root 1: {root1}")
 print(f"Root 2: {root2}")
elif discriminant == 0:
 # One real root (repeated)
 root = -b / (2*a)
 print(f"Root: {root}")
else:
 # Complex roots
 real_part = -b / (2*a)
 imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
 print(f"Root 1: {real_part} + {imaginary_part}i")
 print(f"Root 2: {real_part} - {imaginary_part}i")
    


