# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:22:04 2021

@author: geohu
"""

## Exercise: apply to each

# Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# Assume that:
testList = [1, -4, 8, -9]

# For each of the following questions (which you may assume is evaluated independently of the 
# previous questions, so that testList has the value indicated above), provide an expression using 
# applyToEach, so that after evaluation testList has the indicated value. You may need to write 
# a simple procedure in each question to help with this process.

# >>> print(testList)
# [1, 4, 8, 9]

def absolute(a):
    return abs(a)

applyToEach(testList, absolute)