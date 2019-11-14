"""
Author: Kelley Fischer
File: ch8_p3_kfischer.py

This is a simple text editor that allows a user to 
open, create, edit, and save text documents.
"""


from breezypythongui import EasyFrame
import tkinter.filedialog


class TextEdit(EasyFrame):

    def __init__(self):

        EasyFrame.__init__(self, title = "Text Editor")

        # Create the menu bar
        menuBar = self.addMenuBar(row = 0, column = 0)

        # Create the "File" menu option and add menu items
        appMenu = menuBar.addMenu("File")
        appMenu.addMenuItem("New",  self.newFile)
        appMenu.addMenuItem("Open", self.openFile)
        appMenu.addMenuItem("Save", self.saveFile)

        # Creates text area for document text
        self.outputArea = self.addTextArea("", row = 1, column = 0, columnspan = 10, width = 80, height = 15, wrap = "word")


    # Creates a new text file
    def newFile(self):
        self.setTitle("new document")
        self.outputArea.setText("")


    # Saves the current text file
    def saveFile(self):
        fList = [("Text files", "*.txt")]
        fileName = tkinter.filedialog.asksaveasfilename(parent = self, filetypes = fList)
        
        file = open(fileName, 'w')
        file.write(self.outputArea.getText())
        file.close()
        self.setTitle(fileName)


    # Opens the open file dialog to open an existing file
    def openFile(self):
        """Pops up an open file dialog, and if a file is selected displays its 
        text in the text area and its pathname in the title bar."""
        fList = [("Text files", "*.txt")]
        fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)

        if fileName != "":
            file = open(fileName, 'r')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.setTitle(fileName)        


def main():
    """Instantiates and pops up the window."""
    TextEdit().mainloop()


if __name__ == "__main__":
    main()

