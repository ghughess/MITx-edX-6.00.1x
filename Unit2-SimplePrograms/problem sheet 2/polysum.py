# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 18:09:43 2021

@author: geohu
"""

### Complete Programming Experience: polysum

from math import *

def polysum(n, s):
    area = (0.25 * n * s**2) / tan(pi/n)
    perimeter = s * n
    tot = area + perimeter**2
    return round(tot, 4)

polysum(75, 88)
polysum(30, 40)
