# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:25:10 2021

@author: geohu
"""

## Exercise: how many

# Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# We want to write some simple procedures that work on dictionaries to return information.

# First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:

# >>> print(how_many(animals))
# 6

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        result += len(value)
    return result