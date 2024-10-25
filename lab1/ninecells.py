"""
Author: Lizzie Steilberg
Project 1
File: ninecells.py

"""

from breezypythongui import EasyFrame

class NineCells(EasyFrame):
    """Displays a 3x3 grid with each grid position labeled."""

    def __init__(self):
        """Sets up grid,adds labels."""
        EasyFrame.__init__(self)
        for row in range(0,3):
            for column in range(0,3):
                text = "(" + str(row) + ", " + str(column) + ")"
                self.addLabel(text=text, row=row, column=column, sticky='ns')
def main():
    """Starting point for the program."""
    NineCells().mainloop()

if __name__ == "__main__":
    """Creates and pops up window."""
    main()
