def recursion_fibonacci(n):
    if n<=1:
        return n
    else:
        return(recursion_fibonacci(n-1)+recursion_fibonacci(n-2))
    
nterm = int(input("Enter the number of terms (grrater than 0): "))
if nterm <= 0:
    print("please enter +ve integer value : ")
else:
    print("Fibonacci Sequence : ")
    for i in range(nterm):
        print(recursion_fibonacci(i))