A =int(input("Enter the first number: "))
B =int(input("Enter the second number: "))
C =int(input("Enter the third number: "))

if A<=B and A<=C:
    print("A is the smallest number:", A)
elif B<=A and B<=C:
    print("B is the smallest number:", B)
else:
    print("C is the smallest number:", C)
    