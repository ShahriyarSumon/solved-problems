def find_largest(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Largest number is:", find_largest(num1, num2))
