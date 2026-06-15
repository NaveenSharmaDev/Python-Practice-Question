
#Artimantic operation
# + - / * %

# # -------- Addition --------
a = 45
b = 30
c = a+b
d =  c + 5
print(d)

# -------- Subtraction --------
a = 50
b = 20
c = a-b
d = c-5
print(d)

# -------- Division --------
a = 50
b = 2
c = a/b
d = c/2
print(d)

# -------- Multiplication --------
a = 10
b = 5
c = a*b
print(c)

# -------- Modulus --------
a = 20
b = 5
c = a%b
print(a%b)

# -------- Exponentiation/Power --------
num1 = 5
num2 = 3
print(num1**num2)


#comparison operators
a = 7
b = 2
print(a//b)

a = 10
b = 3
print(a//b)


a = 7
b = 5
print(a != b)

a = 5
b = 5
print(a == b)

a = 5
b = 2
print(a == b)

num1 = 95
num2 = 169
res = num1>num2
print(res)

num3 = False
print(res == num3)

num3 = True
print(res != num3)


#Logical operators
a = 5
b = 50
print(a >= b and a==b)

a = 50
b = 50
print(a >= b and a==b)

a = 5
b = 50
print(a <= b or a==b)

print(not True)
print(not False)


#Assignment Operators
x = 5
x = x+3
print(x)

x = 5
x += 3
print(x)


# List of boolean values
num = [True, False]
print(num)
print(type(num))

# Print the list
list1 = ["Aman" , "Mohit" , "shoeb"]   #we are replace the index values
list1[1] = "Priya"          #we replace the Mohit to Priya here
list1[2] = "Raman"
list1.append("Naveen")
print(list1)


#Tuple
numbers = (9,7,3,45,5)
print(numbers)
print(type(numbers))       # Print tuple data type

#Sets
sets = {4,5,5,6,7,8}
print(sets)

#Dict
students = {
    "name" : "Shruti",
    "age" : 25,
    "course" : "python"
}
print(students["age"])


# Take input in Celsius and print its equivalent in Fahrenheit and Kelvin
Celsius = float(input("Enter Celsius: "))

# Print Fahrenheit equivalent of Celsius
Fahrenheit = (Celsius * (9/5))+32
print("Fahrenheit Value is:",Fahrenheit)

## Print Kelvin of Celsius
Kelvin = (Celsius + 273.15)
print("Kelvin Value is:",Kelvin)



# Check whether the value 2 is NOT present in the list or not
a = 2 not in [22 , 3]
print(a)

# Check whether a number is greater than, equal to, or less than 10
x = 10
if x > 10:
    print("Greater than 10")
elif x == 10:
    print("equal to 10")
else:
    print("Less than 10")

# Check the value of variable 'a'
    a = 10
    if a > 10:
        print("a is greater than 10")
    elif a == 10:
        print("a is equal to 10")
    else:
        print("a is Less than 10")


# Grade calculator using user input
marks = int(input("Enter marks: "))

if  marks >= 40:
    print("A")
elif marks >= 30:
    print("B")
elif marks >= 20:
    print("C")
elif marks >= 10:
    print("D")
elif marks >= 0:
    print("E")
else:
    print(" enter a valid number")


# Grade calculator using range conditions
marks = 20
if marks >= 40 and marks <= 50:
    print("A")
elif marks >= 30 and marks < 40:
    print("B")
elif marks >= 20 and marks < 30:
    print("C")
elif marks >= 10 and marks < 20:
    print("D")
elif marks >= 0 and marks < 10:
    print("E")
else:
    print("invalid marks")


# Write a Python program to print day number using match-case.
week = (input("enter a your day"))
day = week
match day:
    case "Monday":
        print("day One")
    case "Tuesday":
        print("day Two")
    case "Wednesday":
        print("day Three")
    case "Thursday":
        print("day Four")
    case "Friday":
        print("day Five")
    case "Saturday":
        print("day Six")
    case "Sunday":
        print("day Seven")


# we compare number of elements with printing values
day = "saturday"
if day in ["Monday", "Tuesday"]:
    print("Normalday")
elif day in ["wedneshday", "Thursday"]:
    print("causaual day")
elif day in ["friday", "Saturday"]:
    print("fun day")
elif day in ["saturday", "Sunday"]:
    print("week of")
else:
       print("invalid inputes")


