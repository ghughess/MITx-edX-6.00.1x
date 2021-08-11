# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 12:05:23 2021

@author: geohu
"""

## Exercise: genPrimes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to 
# its next() method: 2, 3, 5, 7, 11,...

def genPrimes():
    number = 2
    def isPrime(x):
        
        if x > 1:
            for i in range(2, x):
                if (x % i) == 0:
                    return False
            else:
                return True
                
    while True:
        if isPrime(number) == True:
            yield number
        number += 1