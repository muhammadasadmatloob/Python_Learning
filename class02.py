# Day 2: Conditionals + Loops
# 1. Conditionals — Making Decisions
# Programs need to make choices. if, elif, else let your code branch based on conditions.

age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# Multiple conditions with elif:
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")

# Combining conditions:
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 18 or has_license == False:
    print("Cannot drive")

# 2. Loops — Repeating Actions
# for loop — when you know how many times to repeat
for i in range(5):
    print(i)
# Output: 0 1 2 3 4
# range(5) generates numbers 0 to 4 (5 numbers, stops before 5). This trips up beginners constantly — range(n) never includes n itself.

for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5 — start at 1, stop before 6.

for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8 — start, stop (exclusive), step size.

# while loop — when you don't know how many times, repeat until a condition is False
count = 0
while count < 5:
    print(count)
    count += 1   # same as count = count + 1
# Danger: if you forget count += 1, this loop runs forever (infinite loop). Always make sure something 
# inside the loop moves it toward the stopping condition.

# break and continue

for i in range(10):
    if i == 5:
        break        # stops the loop completely
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue     # skips this iteration, goes to next
    print(i)         # only prints odd numbers

# Why loops + conditionals matter for DSA
# Almost every DSA problem is: loop through data + check a condition + do something.
#  This is the actual skeleton of algorithmic thinking. 
# Master this combo and LeetCode Easy problems become very approachable. 

# Practice Problems
# Take a number as input. Print "Positive", "Negative", or "Zero".

number = int(input("enter a number: "))

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# Print all even numbers from 1 to 50 using a for loop.
for i in range(2,51,2):
        print(i)

# Take a number as input and print its multiplication table (1x to 10x) using a loop.

num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

# Using a while loop, keep asking the user to guess a number (fixed number in code, e.g. 7) until they get it right. Print "Correct!" when they do.
target = 7
guess = None
while guess != target:
    guess = int(input("guess the number:"))
    if guess == target:
        print("correct")
    else:
        print("try again")

# Today's Logic-Building Problem

# FizzBuzz (classic interview warm-up):
# Print numbers 1 to 30. But:

# If divisible by 3 → print "Fizz" instead of the number
# If divisible by 5 → print "Buzz" instead
# If divisible by both 3 and 5 → print "FizzBuzz"
# Otherwise → print the number

# Think about order of checks before coding — what happens if you check "divisible by 3" before "divisible by both"?

for i in range(1,31):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0 :
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)