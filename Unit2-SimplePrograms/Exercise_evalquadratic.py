# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 18:33:35 2021

@author: geohu
"""

## Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the 
# quadratic ax^2 + bx + c .

# This function takes in four numbers and returns a single number.

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*(x**2) + b*x + c