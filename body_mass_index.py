def bodymassindex(height,weight):
    return round((weight / height**2),2)

h = float(input("Enter height : "))
w = float(input("Enter weight"))

print("Welcome to Body Mass Index Value...")
bmi = bodymassindex(h,w)
print("Your Body Mass",bmi)