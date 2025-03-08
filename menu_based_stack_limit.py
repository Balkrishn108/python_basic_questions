stack = []
def push():
    if len(stack) == n:
        print("Stack is full!")
    else:
        element = input("Enter element to stack ")
        stack.append(element)
        print(stack)
def pop_element():
    if not stack:
        print("stack is empty: ")
    else:
        e = stack.pop()
        print("Removed element is :",e)
        print(stack)

n = int(input("Enter the limit of stack : "))
while True:
    print("Select correct operation push:1,pop:2,quit:3")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Please select the correct operation")