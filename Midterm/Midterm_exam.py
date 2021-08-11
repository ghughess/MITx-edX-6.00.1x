# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 12:12:11 2021

@author: geohu
"""

### Midterm Exam
### ------------
   
## Problem 3
    
# Write a simple procedure, myLog(x, b), that computes the logarithm of a number x relative to a base b. 
# For example, if x = 16 and b = 2, then the result is 4 - because 2^4 = 16. If x = 15 and b = 3, then the result is 
# 2 - because 3^2 is the largest power of 3 less than 15.

# In other words, myLog should return the largest power of b such that b to that power is still less than or equal to x.

# x and b are both positive integers; b is an integer greater than or equal to 2. Your function should return an integer answer.

def myLog(x, b):
    """
    x: a positive integer
    b: a positive integer; b >= 2
    
    returns: log_b(x), or, the logarithm of x relative to a base b.
    """
    for i in range(x):
        if b**i > x:
            break
    return i - 1
        
# ------------------------------
        
## Problem 4
    
# Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB 
# have the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product 
# is 1*4 + 2*5 + 3*6, meaning your function should return: 32

# This function takes in two lists of numbers and returns a number.
  
def dotProduct(listA, listB):
    """
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    """
    sum = 0
    for i in range(len(listA)):
        dot = listA[i] * listB[i]
        sum += dot
        
    return sum

# ------------------------------
        
## Problem 5
    
# Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted 
# in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return 
# an empty list.)

# This function takes in a dictionary and an integer and returns a list.
    
def keysWithValue(aDict, target):
    """
    aDict: a dictionary
    target: an integer
    """
    result = []
    for i in aDict:
        if aDict[i] == target:
            result.append(i)
        result.sort()
        
    return result

# ------------------------------
        
## Problem 6
    
# For example,
    
# max_val((5, (1,2), [[1],[2]])) returns 5.
# max_val((5, (1,2), [[1],[9]])) returns 9.
    
def max_val(t): 
    """ 
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t 
    """
    lst = []
    biggestValue = 0
    
    for ele in t:
        if type(ele) == int:
            lst.append(ele)
        elif type(ele) == tuple:
            for i in ele:
                lst.append(i)
        elif type(ele) == list:
            for i in ele:
                if type(i) == int:
                    lst.append(int(i))
                else:
                    for j in i:
                        lst.append(j)
                        
    print(lst)
                                
    for e in lst:
        if e > biggestValue:
            biggestValue = e
        
    return biggestValue
        
        
max_val((5, (1,2), [[1],[2]]))
max_val((5, (1,2), [[1],[9]]))

# ------------------------------
        
## Problem 7
    
# Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10) 
# should evaluate to 1234 because 1*10^3 + 2*10^2 + 3*10^1 + 4*10^0.
    
def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def calculate(x):
        k = 0
        for i in L:
            k = x*k + i
        return k
    return calculate
