# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 18:40:51 2021

@author: geohu
"""

## Exercise: odd

# Write a Python function, odd, that takes in one number and returns True when the number is odd 
# and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    if x % 2 != 0:
        return True
    else:
        return False