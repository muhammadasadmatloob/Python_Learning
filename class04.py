# Day 4: Lists Deep Dive + Big O Intro + First LeetCode Problem
# 1. Lists — Python's Core Data Structure
# You've used lists already ([3, 7, 1, 9]). Today we go deeper — this is the data structure you'll use in almost every DSA problem.

numbers = [10, 20, 30, 40, 50]

# Indexing and slicing (same rules as strings)

print(numbers[0])     # 10
print(numbers[-1])    # 50
print(numbers[1:3])   # [20, 30]


# Modifying lists
numbers.append(60)          # adds to the end -> [10,20,30,40,50,60]
numbers.insert(0, 5)         # insert 5 at index 0 -> [5,10,20,30,40,50,60]
numbers.remove(20)           # removes the VALUE 20 (first occurrence)
numbers.pop()                 # removes and returns the LAST item
numbers.pop(0)                 # removes and returns item at index 0

# Key distinction: remove() deletes by value, pop() deletes by index (and gives it back to you). 
# Mixing these up is a common beginner bug.


# Useful list operations
numbers = [5, 3, 8, 1, 9]

print(len(numbers))        # 5
print(max(numbers))        # 9
print(min(numbers))        # 1
print(sum(numbers))        # 26
print(sorted(numbers))     # [1, 3, 5, 8, 9]  -> new sorted list, doesn't change original
numbers.sort()              # sorts the ORIGINAL list in place
numbers.reverse()           # reverses the original list in place

# Looping with index using enumerate

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# This is very common in DSA — you often need both the position and the value.

# List comprehension (a Python superpower — condensed loop)
squares = [x**2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# This is exactly the same as:

squares = []
for x in range(1, 6):
    squares.append(x**2)
# Just written in one line. You'll see this constantly in clean Python code 
# — worth getting comfortable with it now, but the plain loop version is
#  always fine too.

# 2. Big O Notation — How to Measure "Good" Code
# This is the single most important concept for technical interviews.
#  Big O describes how the runtime of your code grows as input size grows 
# — it's not about speed in seconds, it's about scaling.

# Common complexities, from best to worst:

# O(1) — Constant time. Doesn't matter how big the input is, same amount 
# of work.
def get_first(arr):
    return arr[0]   # always 1 step, whether arr has 5 or 5 million items

# O(n) — Linear time. Work grows directly with input size. 
# One loop through the data.

def find_max(arr):
    biggest = arr[0]
    for num in arr:       # loops once through n items
        if num > biggest:
            biggest = num
    return biggest

# O(n²) — Quadratic time. A loop inside a loop. 
# Gets slow fast as input grows.

def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):     # nested loop = n * n
            if i != j and arr[i] == arr[j]:
                return True
    return False

# O(log n) — Logarithmic time. Cuts the problem in half each step 
# (binary search — we'll cover this in a few days). 
# Extremely efficient even for huge inputs.

# Why this matters: In interviews, writing working code isn't enough — 
# they ask "can you do better?" expecting you to reduce O(n²) to O(n), 
# for example. From today onward, after solving a problem, I'll ask you 
# to state its Big O — that's part of building the "problem-solving mindset"
#  you asked for.

# Given a list of numbers, write a function second_largest(arr) that returns
# the second largest number (don't use sorted() — loop through manually).

arr = [1,3,5,4,2,6]

def secondLargest(arr):
    largest = sec_Largest = float('-inf')

    for num in arr:
        if num > largest:
            sec_Largest = largest
            largest = num
        elif num > sec_Largest and num != largest:
            sec_Largest = num

    return sec_Largest

print(secondLargest(arr))

# Write a function remove_duplicates(arr) that takes a list and returns a 
# new list with duplicates removed, preserving order.

def remove_duplicates(arr):
    new_array = []

    for num in arr:
        if num not in new_array:
            new_array.append(num)

    return new_array
print(remove_duplicates([2,7,8,5,5,6,2,5]))

# Using list comprehension, create a list of all squares
# of even numbers from 1 to 20.

square = [n**2 for n in range(1,21) if n%2 == 0]
print(square)

# Today's First Official LeetCode Problem
# LeetCode 1: Two Sum

# Given a list of integers nums and a target integer target,
#  return the indices of the two numbers that add up to 
# target. Assume exactly one solution exists, and you 
# can't use the same element twice.

nums = [2, 7, 11, 15]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(f"{nums[i]} and {nums[j]} gives target value")


def two_sum(target,arr):
    seen = {}
    for index,num in enumerate(arr):
        needed = target - num

        if needed in seen:
            return[seen[needed],index]

        seen[num] = index

nums = [2, 7, 11, 15]
target = 9

print(two_sum(target,nums))
        

# Mindset Note

# From today, every problem you solve, ask yourself: 
# "What's the brute-force way, and is there a smarter
#  way?" That question alone is 80% of what interviewers
#  are testing for. You don't need the optimal solution instantly 
# — you need to recognize when a solution is brute-force and know 
# that's a starting point, not the final answer.