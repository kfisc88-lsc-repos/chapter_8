"""
Author: Kelley Fischer
CIS 1415 - Intro to Programming
File: ch8_p1_kfischer.py

Creates a GUI for an income tax calculator. Unfortunately I don't know
the actual formula for caculcating income so I didn't create the function
to do so. However, it looks like an income tax calculator. 
"""

from breezypythongui import EasyFrame

class TaxCalc(EasyFrame):

    def __init__(self):

        # Create the main window
        EasyFrame.__init__(self, "Tax Calculator")

        # Create labels & fields
        self.addLabel(text = "Gross Income", row = 0, column = 0)
        self.income = self.addFloatField(value = 0.0, row = 0, column = 1, columnspan = 2)

        self.addLabel(text = "Dependents", row = 1, column = 0)
        self.depend = self.addIntegerField(value = 0, row = 1, column = 2)

        self.addLabel(text = "Total tax", row = 5, column = 0)
        self.total = self.addFloatField(value = 0.0, row = 5, column = 1, columnspan = 2)

        # Create the radio button group
        self.addLabel(text = "Filing Status", row = 2, column = 0, columnspan = 3)
        self.filingStatus = self.addRadiobuttonGroup(row = 3, column = 0, columnspan = 3, orient = "horizontal")
        defaultRB = self.filingStatus.addRadiobutton(text = "Single: 20%")
        self.filingStatus.setSelectedButton(defaultRB)
        self.filingStatus.addRadiobutton(text = "Married: 15%")
        self.filingStatus.addRadiobutton(text = "Divorced: 10%")

        # Create a button to compute the tax
        self.compute = self.addButton(text = "Compute", row = 4, column = 1, command = self.compute)


    # I tried in vain to find the actual calculations
    def compute(self):
        pass

def main():
    """Instantiates and pops up the window."""
    TaxCalc().mainloop()

if __name__ == "__main__":
    main()
