# while loop
i = 1
while i <=5:
    print("Naveen Kumar")
    i +=1

# write program and print number 1 to 10 using while loop
i = 1
while i <=10:
    print(i)
    i +=1

# write program and print number from 10 down to 1 using while loop
i = 10
while i>0:
    print(i)
    i -=1

# write a program and print number is all even from 1 to 50 using while loop
num = 1
while num<=50:
      if num % 2==0:
        print(num)
      num = num+1


#write a program that prints the sum of first n natural number.
n = int(input("enter a number"))
sum= 0

while n>=1:
    sum = sum + n
    n = n-1

print("sum=",sum)
print("n=",n)

#write a program to print this pattern using a while loop
# *
# **
# ***
# ****
n = 1
while n<=4:
    print("*" * n)
    n += 1
print("we are out of the while loop and value of n checks", n)

#Naveen Kumar want to print her name 5 time , but each time with a number
#in front of it. program using a while loop that prints
i = 1
while i<=5:
   #print(i)
   print(i , "Naveen Kumar")
   i += 1

# write a program to print the multiplication table of any number using while loop
num = int(input("enter a number"))
i = 1
while i<=10:
    print(f"{num} * {i} = {num * i}")
    i += 1


