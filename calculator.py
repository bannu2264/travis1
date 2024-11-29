# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

def main():
    print("Welcome to the Calculator!")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    operation = input("Enter operation (+, -, *, /): ").strip()
    
    if operation == '+':
        print(f"The result is {add(a, b)}")
    elif operation == '-':
        print(f"The result is {subtract(a, b)}")
    elif operation == '*':
        print(f"The result is {multiply(a, b)}")
    elif operation == '/':
        print(f"The result is {divide(a, b)}")
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
