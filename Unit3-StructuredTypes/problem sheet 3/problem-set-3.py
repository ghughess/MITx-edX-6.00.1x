# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 13:26:36 2021

@author: geohu
"""

### Problem Set 3
### --------------

# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
    
### --------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

### --------------

## Problem 1 - Is the Word Guessed

# Please read the Hangman Introduction before starting this problem. We'll start
# by writing 3 simple functions that will help us easily code the Hangman problem.
# First, implement the function isWordGuessed that takes in two parameters - a string,
# secretWord, and a list of letters, lettersGuessed. This function returns a boolean -
# True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed)
# and False otherwise.

# Example Usage:

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))
# False

# For this function, you may assume that all the letters in secretWord and lettersGuessed are
# lowercase.

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
    """
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

print(isWordGuessed(secretWord, lettersGuessed))

### --------------
    
## Problem 2 - Getting the User's Guess
    
# Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord,
# and a list of letters, lettersGuessed. This function returns a string that is comprised of letters
# and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too
# different from isWordGuessed!
    
# Example Usage:

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))
# '_ pp_ e'
    
# When inserting underscores into your string, it's a good idea to add at least a space after each one,
# so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ 
# with _ _ _ _ ). This is called unsability - it's very important, when programming, to consider the usability
# of your program. If users find your program difficult to understand or operate, they won't use it!
    
# For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters
# and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability
# when designing.
    
# For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
    
def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed so far.
    """
    result = []
    for i in secretWord:
        if i in lettersGuessed:
            result.append(i)
        else:
            result.append('_')
    return ' '.join(result)
    
print(getGuessedWord(secretWord, lettersGuessed))

### --------------
    
## Problem 3 - Printing Out all Avaiable Letters
    
# Next, implement the function getAvaiableLetters that takes in one parameter - a list of letters,
# lettersGuessed. This function returns a string that is comprised of lowercase English letters - all
# lowercase English letters that are not in lettersGuessed.
    
# Example Usage:

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))
# abcdfghjlmnoqtuvwxyz
    
# Note that this function should return the letters in alphabetical order, as in the example above.
# For this function, you may assume that all the letters in lettersGuessed are lowercase.
# Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:
    
# import string
# print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
    
import string
alph = string.ascii_lowercase
    
def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
        yet been guessed.
    """
    remain = []
    for i in alph:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)

print(getAvailableLetters(lettersGuessed))
    
### --------------
    
## Problem 4 - The Game
    
# Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess.
# This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of
# the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the
# previous part.
    
# Hints:
    
# You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the
# words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local
# machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.
    
# Consider using lower() to convert user input to lower case. For example:
guess = 'A'
guessInLowerCase = guess.lower()
    
# Consider writing additional helper functions if you need them!
    
# There are four important pieces of information you may wish to store:
# 1. secretWord: The word to guess.
# 2. lettersGuessed: The letters that have been guessed so far.
# 3. mistakesMade: The number of incorrect guesses made so far.
# 4. availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter
# must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a
# message telling them they've already guessed that - so try again!).
    
# Note that if you choose to use the helper function isWordGuessed, getGuessedWord or getAvailableLetters, you do not need
# to paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of
# the problem. If you use additional helper functions, you will need to paste those definitions here.
    
# Your function should include calls to input to get the user's guess.
    
def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many letters the secretWord contains.
    
    * Ask the user to supply one guess (i.e. letter) per round.
    
    * The user should receive feedback immediately after each guess about whether their guess appears in the computers word.
    
    * After each round, you should also display to the user the partially guessed word so far, as well as letters that the user
    has not yet guessed.
    
    Follows the other limitations detailed in the problem write-up.
    """
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []
    
    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("-----------")
            print("Congratulations, you won!")
            break
        else:
            print("-----------")
            print("You have", 8 - mistakesMade, "guesses left.")
            print("Available letters:", getAvailableLetters(lettersGuessed))
            guess = str(input("Please guess a letter:")).lower()
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            elif guess not in secretWord:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guess)
                mistakesMade += 1
        if 8 - mistakesMade == 0:
            print("-----------")
            print("Sorry, you ran out of guesses. The word was", secretWord)
            break
        else:
            continue
        
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
