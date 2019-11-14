"""
Author: Kelley Fischer
File: ch8_p2_kfischer.py

This program converts given Fahrenheit values to Celsius
and vice versa. 
"""

from breezypythongui import EasyFrame

class TempConvert(EasyFrame):
    
    def __init__(self):
        
        EasyFrame.__init__(self, title = "Fahrenheit/Celsius Converter")
        
        # Labels and Input fields
        self.addLabel(text = "Fahrenheit", row = 0, column = 0, sticky = "EW")
        self.addLabel(text = "Celsius", row = 0, column = 1, sticky = "EW")
        self.fahrenheit = self.addFloatField(value = 32.0, row = 1, column = 0, precision = 1)
        self.celsius = self.addFloatField(value = 0, row = 1, column = 1, precision = 1)
        
        # Buttons for activating conversions
        self.addButton(text = ">>>>", row = 2, column = 0, command = self.calcCelsius)
        self.addButton(text = "<<<<", row = 2, column = 1, command = self.calcFahrenheit)
        
        # Bind keyboad events
        self.fahrenheit.bind("<Return>", lambda event: self.calcCelsius())
        self.celsius.bind("<Return>", lambda event: self.calcFahrenheit())


    # Converts Fahrenheit to Celsius
    def calcCelsius(self):
        convertF = (self.fahrenheit.getNumber() - 32)*(5/9)
        self.celsius.setNumber(convertF)


    # Converts Celsius to Fahrenheit
    def calcFahrenheit(self):
        convertC = (self.celsius.getNumber() * 9/5) + 32
        self.fahrenheit.setNumber(convertC)


def main():
    """Instantiates and pops up the window."""
    TempConvert().mainloop()

if __name__ == "__main__":
    main()

