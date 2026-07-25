N = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")

for i in range(N):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
      