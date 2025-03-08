def factorial_recursion(n):
    if n==1:
        return n
    else:
        return n*factorial_recursion(n-1)

number = int(input("Enter number to find factorial : "))
if number < 0:
    print("factorial not available :") 
elif number == 0:
    print("Factorial of 0 is 1")
else :
    print(f"Factorial of {number} is =  {factorial_recursion(number)}")