# Day 3: Functions + Strings
# 1. Functions — Reusable Blocks of Code

# A function is a named block of code you can run whenever you need it, instead of rewriting the same logic repeatedly.

def greet():
    print("Hello!")

greet()   # calling the function
greet()   # can call it as many times as you want

# def defines a function. The indented block below it is the function's body — same indentation rule as if/for

# Parameters — passing data into a function

def greet(name):
    print(f"Hello, {name}!")

greet("Ali")
greet("Sara")


# name is a parameter — a placeholder. "Ali" and "Sara" are arguments — the actual values you pass in.

# Return values — getting data back out
def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # 8

# return sends a value back to wherever the function was called. This is different from print() — print just displays something, 
# return actually gives you the value to use later (store it, do math with it, pass it elsewhere).

def add(a, b):
    print(a + b)   # only displays, doesn't return anything

x = add(5, 3)   # x is now None, because add() didn't return anything
print(x)   # None
# This distinction confuses almost every beginner. Remember: print shows, return gives back.

# Default parameters
def greet(name="friend"):
    print(f"Hello, {name}!")

greet()          # Hello, friend!
greet("Ali")     # Hello, Ali!

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = get_min_max([3, 7, 1, 9, 4])
print(lo, hi)   # 1 9

# 2. Strings — Working with Text

# Strings are sequences of characters, and Python treats them almost like lists — you can index into them, slice them, 
# loop through them.

# Indexing
word = "Python"
print(word[0])    # P  (indexing starts at 0)
print(word[-1])   # n  (negative index = from the end)

# Slicing
word = "Python"
print(word[0:3])   # Pyt   (index 0 up to, not including, 3)
print(word[:3])    # Pyt   (start omitted = from beginning)
print(word[3:])    # hon   (end omitted = to the end)
print(word[::-1])  # nohtyP  (reverses the string — very common trick)

# Common string methods

s = "  Hello World  "
print(s.lower())         # "  hello world  "
print(s.upper())         # "  HELLO WORLD  "
print(s.strip())         # "Hello World"  (removes leading/trailing spaces)
print(s.replace("World", "Python"))  # "  Hello Python  "
print(len(s))             # length of string, including spaces
print("Hello" in s)       # True — checks if substring exists

# Splitting and joining
sentence = "I love Python programming"
words = sentence.split()      # splits on spaces by default
print(words)   # ['I', 'love', 'Python', 'programming']

joined = "-".join(words)
print(joined)  # I-love-Python-programming


# Looping through a string
for char in "Python":
    print(char)


# f-strings (you've already used these)

name = "Ali"
age = 22
print(f"{name} is {age} years old")

# Why this matters for DSA

# String manipulation problems are one of the most common LeetCode categories — 
# reversing strings, checking palindromes, counting characters, anagrams. 
# Indexing, slicing, and loops are the toolkit for almost all of them.

# Practice Problems
# Write a function is_even(number) that returns True if the number is even, False otherwise.
def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

num = int (input("Enter a number:"))
print(is_even(num))

# Write a function square(n) that returns n squared. Call it with 3 different numbers and print each result.
def square(n):
    return n**2


number = int (input("enter any number:"))
print(square(number))

# Take a string as input and print it reversed
s = input("enter any word:")
print(s[::-1])

# Write a function count_vowels(word) that counts and returns how many vowels are in a given word.
def count_vowels(word):
    count_vowels = 0
    for char in word:
        if char in "aeiou":
            count_vowels += 1

    return count_vowels
word = input("enter any word: ")
print(count_vowels(word))

# Today's Logic-Building Problem

# Palindrome Check: Write a function is_palindrome(word) that returns 
# True if a word reads the same forwards and backwards (e.g., "madam", "racecar"), 
# False otherwise. Ignore case (so "Madam" should still count as a palindrome).

# Hint: think about how slicing ([::-1]) can help you here in one line.

def check_palindrome(word):
    word= word.lowercase()
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
            
    
words = input("enter any word:")
print(check_palindrome(words))

