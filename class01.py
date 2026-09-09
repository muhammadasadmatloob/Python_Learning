# first program
print("hello world")

# print() is an fuction - a reusable block of code that dose something.

# variables - storing data
# a variable is anamed box that holds a value

name = "John"
age = 20
height = 5.9

# so the name holds the text called a string(str)
# age holds a whole number called an integer(int)
# height holds a decimal number called a float(float)

# we dont need to declare the type of variable in python
# as any other language it automatically detects called dynamic type casting

print(name)
print(age)
print(height)

# data types:

x = "hello" #string
y = 25 #integer
z = 3.14 #float
a = True #boolean

# to check the type of variable
print(type(x))
print(type(y))
print(type(z))
print(type(a))


# how to take an input from user
name = input ("enter your name: ")
print("hello, "+name)

# input by default takes an string even if you type a number
age = input("enter your age")
print(type(age))

# to use it as a number we have to convert it 
age = int (input( "Enter your age:" ))
print(age+3)

# operators
# there are two type of operators arithmatic and comparison
# lets see first arithmatic
print(10+3) #addition
print(10-3) #subtraction
print(10*3) #multiplication
print(10/3) #division
print(10//3) #floor division
print(10%3) #modulus
print(10**3) #power

# comparison operator only checks true and false
print(10>3) 
print(10 == 3)
print(10 != 3 )

# why the % modulus matters
# this one operator alone solves ton of logic problems :
# check even/odd , checking divisibility , cycling through positions
# remeber it you'll use it constantly in dsa

# practice problem
# take an input veriable for your name and age and print them in an sentence
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"hello my name is {name} and iam {age} years old")

# take two numbers as an input from the user and print there sum

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print(number1+number2)

# take input number and check its even or odd
number = int(input("Enter number: "))
if number%2 == 0:
    print("even")
else:
    print("odd")


# logic building 

# how many years left to turn 100
# simple and easy
# first we will take an input age
# input age - 100 
# and the remaining years will be those years
# output will be years left

age = int ( input("Enter your age: "))
years = 100
years_remains_to_convert_to_100 =  years - age
print(years_remains_to_convert_to_100)