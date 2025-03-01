def compute_hcf(x,y):
    if x>y:
        smalller = y
    else:
        smalller = x
    for i in range(1,smalller+1):
        if((x%i == 0) and (y %i ==0)):
            hcf = i
    return hcf

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print(compute_hcf(num1,num2))