def greet(name):
    return f"Hello, MY NAME IS {name}, I am upcoming AI Engineer."

name = input("Enter your name: ")
print(greet(name))


def add_numbers(num1, num2):
    return num1 + num2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"The sum of {a} and {b} is: {add_numbers(a, b)}")