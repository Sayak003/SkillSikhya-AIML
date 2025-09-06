print("Hello World!")
name = input("What is your name? ")
age = input("How old are you? ")
print(f"Welcome {name}, you are {age} years old!")
x = input("Enter any Number: ")
y = input("Enter Second Number")
a = input("Choose one sign +, -, *, /: ")
if a == "+":
    print(f"{x} + {y} = {int(x) + int(y)}")
elif a == "-":
    print(f"{x} - {y} = {int(x) - int(y)}") 
elif a == "*":
    print(f"{x} * {y} = {int(x) * int(y)}") 
elif a == "/":
    print(f"{x} / {y} = {int(x) / int(y)}") 
else:
    print("Invalid Operation")
print(f"Thank you for using this simple calculator Mr.{name}")
