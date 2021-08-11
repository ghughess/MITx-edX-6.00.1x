# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 15:23:19 2021

@author: geohu
"""
### Final Exam
### ----------

## Problem 3

# Write a Python function that returns True if aString is a palindrome (reads the same forwards 
# or reversed) and False otherwise. Do not use Python's built-in reverse function or 
# aString[::-1] to reverse strings.

# This function takes in a string and returns a boolean.

def isPalindrome(aString):
    """
    aString: a string
    """
    
    def toChars(aString):
        aString = aString.lower()
        ans = ''
        for c in aString:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(aString):
        if len(aString) <= 1:
            return True
        else:
            return aString[0] == aString[-1] and isPal(aString[1:-1])
        
    return isPal(toChars(aString))

# ---------------------------
    
## Problem 4
    
# Write a function that satisfies the docstring
    
# For example, if
# largest_odd_times([2,2,4,4]) returns None
# largest_odd_times([3,9,5,3,5,3]) returns 9
    
# Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
        
def largest_odd_times(L):
    """ 
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number 
    of times in L. If no such element exists, returns None 
    """
    res = {}
    for e in L:
        if e in res.keys():
            res[e] += 1
        else:
            res[e] = 1
            
    copy = {}
    for i in res.keys():
        if res[i] % 2 != 0:
            copy[i] = res[i]

    if len(copy) == 0:
        return None
    else:
        return max(copy)
    

largest_odd_times([2,2,4,4])
largest_odd_times([3,9,5,3,5,3])
    
# ---------------------------
    
## Problem 5

# For example,
# cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same) 
# ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')

# Paste your entire function, including the definition, in the box below. Do not leave any debugging 
# print statements.

def cipher(map_from, map_to, code):
    """
    map_from, map_to: strings where each contain N unique lowercase letters. 
    code: string (assume it only contains letters also in map_from)
    Returns a tuple of (key_code, decoded).
    key_code is a dictionary with N keys mapping str to str where 
    each key is a letter in map_from at index i and the corresponding 
    value is the letter in map_to at index i. 
    decoded is a string that contains the decoded version of code using the key_code mapping. 
    """
    dct = dict(zip(map_from, map_to))
    txt = ''
    for i in code:
        txt += dct[i]
    return(dct, txt)


cipher("abcd", "dcba", "dab")

# ---------------------------
    
## Problem 6
    
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Person): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that ' + self.name + ' says: ' + stuff # or + Person.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that '  + self.name + ' says: ' + stuff # + Person.say(self, stuff)
    

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')
    
e.say('the sky is blue')
le.say('the sky is blue')
le.lecture('the sky is blue')
pe.say('the sky is blue')
pe.lecture('the sky is blue')
ae.say('the sky is blue')
ae.lecture('the sky is blue')

# ---------------------------
    
## Problem 7

class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tent_loc = tent_loc
        self.tents = [self.tent_loc]
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        for tent in self.tents:
            if new_tent_loc.dist_from(tent) < 0.5:
                return False
        
        if True:
            self.new_tent_loc = new_tent_loc
            self.tents.append(self.new_tent_loc)
        return True
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        self.tents.remove(tent_loc)
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        lst = []
        for e in self.tents:
            lst.append(e.__str__())
        lst.sort()
        return lst


c = MITCampus(Location(1,2))

c.add_tent(Location(2,3)) # return True
c.add_tent(Location(1,2)) # return True
c.add_tent(Location(0,0)) # return False
c.add_tent(Location(2,3)) # return False
c.get_tents() # return ['<0,0>', '<1,2>', '<2,3>']
