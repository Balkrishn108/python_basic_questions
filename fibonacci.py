nterm = int(input("How many terms"))

n1,n2 = 0,1
count = 0
if nterm <= 0:
    print("Please enter valid number ")
elif nterm==1:
    print("fibonacci series ",nterm ,":")
else:
    print("Fibonacci series are :")
    while(count<nterm):
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count+=1