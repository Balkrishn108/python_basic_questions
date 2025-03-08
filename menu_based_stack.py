stack = []
def push():
    print("Enter element for stack : ")
    element = input()
    stack.append(element)

def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Removed element : ",e)
        print(stack)

while True:
    print("Select the operation push:1, pop:2,quit:3  ->")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Please enter correct operation!")
    