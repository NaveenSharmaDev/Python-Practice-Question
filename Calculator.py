A =int(input("Enter the first number: "))
B =int(input("Enter the second number: "))
Operator = input("Enter the operator (+, -, *, /): ")

if Operator == "+":
    result = A + B
    print("The sum is:", result)
elif Operator == "-":
    result = A - B
    print("The difference is:", result)
elif Operator == "*":
    result = A * B
    print("The product is:", result)
elif Operator == "/":
    result = A / B
    print("The quotient is:", result)
else:
    print("Invalid operator")
    