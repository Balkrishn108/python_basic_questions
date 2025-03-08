def add(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

print("Select operation :- ")
print("Press 1 to add    ")
print("Press 2 to subtraction    ")
print("Press 3 to multiplication   ")
print("Press 4 to division   ")

while True:
    choice = input("Enter 1/2/3/4 :-  ")
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter  number 1 : "))
            num2 = float(input("Enter  number 2 : "))
        except ValueError:
            print("Please enter valid value to perform any operation....")
            continue
        if choice == '1':
            print(f"Sum of {num1} and {num2} is {add(num1,num2)}")
        elif choice == '2':
            print(f"Subtrsction of {num1} and {num2} is = {subtraction(num1,num2)}")
        elif choice == '3':
            print(f"Multipliaction of {num1} and {num2} is = {multiplication(num1,num2)}")
        elif choice == '4':
            print(f"Divison of {num1} and {num2} is = {division(num1,num2)}")
        next_calculation = input("Do you want to next calculation (yes/no)")
        if next_calculation == "no":
            break
    else:
        print("invalid syntex")
            
