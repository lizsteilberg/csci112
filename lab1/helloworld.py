"""
Author: Lizzie Steilberg
Project 1
File: helloworld.py

"""

from breezypythongui import EasyFrame

class HelloWorld(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self)
        self.addLabel(text = "Hello world!", font=('Helvetica', 24,"bold"),row = 0, column = 0, foreground='red',sticky='ns')
    

def main():
    """The starting point for launching the program."""
    HelloWorld().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
