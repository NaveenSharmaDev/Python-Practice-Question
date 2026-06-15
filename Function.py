# Function Basic
def SumFunc():
    a = 5
    b = 6
    Sum = a+b
    print(Sum)

SumFunc()
#....100 line of code print then direct call function
SumFunc()
# ....100 line of code
SumFunc()

# Q) write a function name Welcome_message() that print
# "welcome to Python Programming!" three times.
def Welcome_message():
    print("welcome to Python Programming!")

Welcome_message()
Welcome_message()
Welcome_message()

# write a function display_python() that print "python is fun"
def display_python():
    print("Python is Fun!")

display_python()

#Function Definition with parameter
def average(a , b):
    Averagevalue = (a+b)/2
    print(Averagevalue)

#Fuction calling with Arguments
average(5 , 10)
average(7 , 10)
average(80 , 98)
average(2, 4)


# Default parameter
def average(a=10, b=20):
    Averagevalue = (a + b) / 2
    print(Averagevalue)

#Fuction calling with Arguments
average(5, 10)
average(7, 10)
average(80, 98)
average()

#write a function show_age(name, age) that prints: "Naveen Kumar is 24year old".
def show_age(name, age):
    print(f"{name} is {age} years old")
show_age("Naveen Kumar", 24)
show_age("Nitesh Kumar", 25)

#Return statement
def multiply(num1, num2):
    return num1 * num2

result = multiply(2, 3)
print(result)


# write a function that takes a string and return the count of vowel and consonants separately
def countvowConso(userInput):

    vowels = "aeiouAEIOU"
    countVowel = 0
    countConsonant = 0

    for eachChar in userInput:
        if eachChar.isalpha():
            if eachChar in vowels:
                countVowel += 1
            else:
                countConsonant += 1

    return countVowel, countConsonant


# Function call
vowels, consonants = countvowConso("Naveen Kumar")

print("Vowels =", vowels)
print("Consonants =", consonants)