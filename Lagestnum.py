A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))
if A>=B and A>=C:
    print("A is the largest number")
elif B>=A and B>=C:
    print("B is the largest number")  
else:
    print("C is the largest number")
