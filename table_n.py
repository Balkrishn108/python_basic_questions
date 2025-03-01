startNum = int(input("Enter start number : "))
endNum = int(input("Enter end number : "))
for num in range(startNum, endNum+1):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i} ")
    print(" " ,end=" ")
