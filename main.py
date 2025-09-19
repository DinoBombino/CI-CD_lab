def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Calculator ready!")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Sum: {add(a, b)}")
    print(f"Subtract: {subtract(a, b)}")