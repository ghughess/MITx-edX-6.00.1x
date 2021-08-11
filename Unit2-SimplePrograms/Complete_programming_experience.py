# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:10:56 2021

@author: geohu
"""

## Complete Programming Experience: polysum

# A regular polygon has n number of sides. Each side has length s.

# The area of a regular polygon is: (0.25*n*s^2)/tan(pi/n)
# The perimeter of a polygon is: length of the boundary of the polygon

# Write a function called polysum that takes 2 arguments, n and s. This function should sum 
# the area and square of the perimeter of the regular polygon. The function returns the sum, 
# rounded to 4 decimal places.

from math import *

def polysum(n, s):
    area = (0.25 * n * s**2) / tan(pi/n)
    perimeter = s * n
    tot = area + perimeter**2
    return round(tot, 4)