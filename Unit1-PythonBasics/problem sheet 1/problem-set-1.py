# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 13:30:08 2021

@author: geohu
"""

### Problem Set 1
### --------------

## Problem 1

# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', 'u'.
# For example if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

numVowel = 0
s = 'azcbobobegghakl'

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        numVowel += 1
        
print("Number of vowels: " + str(numVowel))

### --------------

## Problem 2

# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print:
# Number of times bob occurs is: 2

numbob = 0
s = 'azcbobobegghakl'

for i in range(len(s) - 2):
    if s[i] == 'b' and s[i + 1] == 'o' and s[i + 2] == 'b':
        numbob += 1
             
print("Number of times bob occurs is: " + str(numbob))

### --------------

## Problem 3

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur 
# in alphabetrical order.
# For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

count = 0
maxcount = 0
end = 0

s = 'azcbobobegghakl'

for i in range(len(s) - 1):
    if (s[i] <= s[i + 1]):
        count += 1
        if count > maxcount:
            maxcount = count
            end = i + 1
    else:
        count = 0
        
start = end - maxcount
print("Longest substring in alphabetical order is: " + str(s[start:end + 1]))
        
        