"""
Author: Lizzie Steilberg
Project 1
File: numberguessgui.py

This is the GUI component of the number guessing game, based on the countergamegui. 
"""

from breezypythongui import EasyFrame

class NumberGuessGui(EasyFrame):
    """Sets up window for game."""

    def __init__(self,model):
        """Adding buttons and labels to our game window."""
        
        EasyFrame.__init__(self, title="Guessing Game")
        self.model = model

        self.label = self.addLabel(text="My " + str(model.updateCount()) + " guess is " + str(model.guess()),
                                   row=0,
                                   column=0,
                                   sticky='nsew',
                                   columnspan=3)

        self.addButton(text="Too Low",
                       row = 1,
                       column = 0,
                       command = self.low)
        
        self.addButton(text="Too High",
                       row = 1,
                       column = 1,
                       command = self.high)
        
        self.addButton(text="correct",
                       row = 1,
                       column = 2,
                       command = self.correct)

    def high(self):
        self.model.high()
        self.label["text"] = "My " + str(self.model.updateCount()) + " guess is " + str(self.model.guess())

    def low(self):
        self.model.low()
        self.label["text"] = "My " + str(self.model.updateCount()) + " guess is " + str(self.model.guess())

    def correct(self):
        self.messageBox(title="I win!",message="Game over, I win!")
        self.quit()
