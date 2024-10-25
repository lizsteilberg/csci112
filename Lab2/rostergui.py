"""
File: rostergui.py
Provides a GUI-based view of a Roster object.

RosterGUI shows the students' names in a scrolling list box,
with the selected student's info displayed in a text area.
Command buttons will add, remove, or modify a student.
"""

from breezypythongui import EasyFrame, EasyDialog
from student import Student
from tkinter import END

class RosterGUI(EasyFrame):
    """Displays the student's info in a text area."""

    def __init__(self, roster):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, title = "Student Roster")

        # Instance variable to track the roster.
        self.roster = roster

        # Set up the list box
        self.listBox = self.addListbox(row = 0, column = 0, width = 25,
                                       listItemSelected = self.listItemSelected)

        # A text area to display the student's info
        self.textArea = self.addTextArea(text = "",
                                         row = 0, column = 1, width = 25)

        # Commands to modify, add, or remove
        buttonPanel = self.addPanel(row = 1,column = 0, columnspan = 2)
        self.modifyButton = buttonPanel.addButton(text = "Modify", row = 0,
                                                  column = 0, command = self.modify)
        self.newButton = buttonPanel.addButton(text = "New", row = 0,
                                               column = 1, command = self.new)
        self.removeButton = buttonPanel.addButton(text = "Remove", row = 0,
                                                  column = 2, command = self.remove)
        # Add student names to the list box and select the first one
        if self.roster.isEmpty():
            self.selectedName = ""
        else:
            for name in self.roster.getNames():
                self.listBox.insert(END, name)
            self.listBox.setSelectedIndex(0)

        # Update the text area and buttons
        self.listItemSelected(0)


    def listItemSelected(self, index):
        """Responds to the selection of an item in the list box.
        Updates the the text area with the selected student's info.
        Also updates the states of the buttons."""
        self.selectedName = self.listBox.getSelectedItem()
        if self.selectedName == "":
            self.textArea.setText("")
            self.modifyButton["state"] = "disabled"
            self.removeButton["state"] = "disabled"
        else:
            self.textArea.setText(str(self.roster.get(self.selectedName)))
            self.modifyButton["state"] = "normal"
            self.removeButton["state"] = "normal"

    def new(self):
        """Creates a new student, pops up the student dialog to enter
        student info, adds the student to the roster, and makes it the
        current student."""
        newStudent = Student()
        StudentDialog(self,newStudent)
        self.insert(newStudent)

    def modify(self):
        """Pops up a dialog to edit the selected student.
        Updates the list box and text area if student was modified."""
        student = self.roster.get(self.listBox.getSelectedItem())
        StudentDialog(self,student)
        self.remove()
        self.insert(student)
    
    def remove(self):
        """Removes the current student from the roster. If the roster becomes empty,
        the current position becomes -1.  Otherwise, if the student removed
        was not the last one, the current position does not change.
        Otherwise, the current position becomes the previous one."""
        selectedStudent = self.listBox.getSelectedItem()
        selectedIndex = self.listBox.getSelectedIndex()
        self.listBox.delete(self.listBox.getSelectedIndex())
        newIndex = 0
        if self.roster.isEmpty():
            newIndex = -1
        elif selectedIndex >= (len(self.roster)-1):
            newIndex = len(self.roster)-2
        else:
            newIndex = selectedIndex
        
        self.listBox.setSelectedIndex(newIndex)
        self.listItemSelected(newIndex)
        self.roster.remove(selectedStudent)
    
    def insert(self, student):
        """Adds student to the roster and updates the view.
        """
        self.roster.add(student)
        self.listBox.clear()
        
        if self.roster.isEmpty():
            self.selectedName = ""
        else:
            for name in self.roster.getNames():
                self.listBox.insert(END, name)
        
        self.listBox.setSelectedIndex(self.listBox.getIndex(student.getName()))
        self.listItemSelected(self.listBox.getIndex(student.getName()))

class StudentDialog(EasyDialog):
    """Opens a dialog on a student object."""

    def __init__(self, parent, student):
        """Sets up the window."""
        self.student = student
        EasyDialog.__init__(self, parent, "Student Editor")
    
    def body(self, master):
        """Sets up the widgets."""
        self.addLabel(master, text = "Name", row = 0, column = 0)
        self.nameField = self.addTextField(master, text = self.student.getName(),
                                           row = 0, column = 1)
        # Labels and fields for the student's scores
        self.scoreFieldList = list()
        for index in range(self.student.getNumberOfScores()):
            self.addLabel(master, text = "Score " + str(index + 1),
                          row = index + 1, column = 0)
            field = self.addIntegerField(master,
                                         value = self.student.getScore(index),
                                         row = index + 1, column = 1)
            self.scoreFieldList.append(field)

    # Event handling method
    def apply(self):
        """When the OK button is clicked, transfers data from the
        fields to the student."""
        if self.nameField.getText() == "":
            self.messageBox("ERROR", "Name is missing")
            return
        self.student.setName(self.nameField.getText())
        for index in range(self.student.getNumberOfScores()):
            self.student.setScore(index, self.scoreFieldList[index].getNumber())
        self.setModified()






            
        
        

