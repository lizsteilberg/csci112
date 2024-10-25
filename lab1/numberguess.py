"""
Author: Lizzie Steilberg
Project 1
File: numberguess.py

The computational copmonent of numberguessapp. Always guesses
the number in the middle of the range, rounded down.
"""

class NumberGuess:
    def __init__(self, low, high):
        self.lo = low
        self.hi = high
        self.count = 0
    
    def updateCount(self):
        self.count += 1
        return self.count

    def guess(self):
        return(self.lo + self.hi) // 2

    def high(self):
        self.hi = self.guess()
        
   
    def low(self):
        self.lo = self.guess()
        
