# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 16:27:03 2021

@author: geohu
"""

## Exercise: while exercise 1

# In this problem you'll be given a chance to practice writing some while loops.

# 1. Convert the following into code that uses a while loop.

# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

num = 0
while num < 9:
    num += 2
    print(num)
print('Goodbye!')

# ---------------------

## Exercise: while exercise 2

# 2. Convert the following into code that uses a while loop.

# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2

print('Hello!')
num = 10
while num > 0:
    print(num)
    num -= 2
    
# ---------------------

## Exercise: while exercise 3
    
# 3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that 
# we define for you. So, for example, if we define end to be 6, your code should print out the result:

# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

# For problems such as these, do not include input statements or define variables we will provide for you. 
# Our automating testing will provide values so write your code in the following box assuming these variables 
# are already defined.

total = 0
current = 1
while current <= end:
    total += current
    current += 1
    
print(total)