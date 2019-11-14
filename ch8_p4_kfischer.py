#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Author: Kelley Fischer
File: ch8_p4_kfischer.py

A simple image browser that can open .gif files
and view them. 
"""


# In[2]:


from breezypythongui import EasyFrame
import tkinter.filedialog
from tkinter import PhotoImage


# In[3]:


class ImageBrowser(EasyFrame):
    
    def __init__(self):
        
        EasyFrame.__init__(self, title = "Image Browser")
        
        # Sets the window size to adjust to the image
        self.setResizable(False)
        
        # Add label and button
        self.imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        self.addButton(text = "Open", row = 1, column = 0, columnspan = 3, command = self.openFile)
        

    # Opens the open file dialog to open an existing file
    def openFile(self):
        
        """Pops up an open file dialog, and if a file is selected displays its 
        text in the text area and its pathname in the title bar."""
        
        fList = [("GIF files", "*.gif")]
        fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)
        
        if fileName != "":
            self.image = PhotoImage(file = fileName)
            self.imageLabel["image"] = self.image
            self.setTitle(fileName)        


# In[4]:


def main():
    """Instantiates and pops up the window."""
    ImageBrowser().mainloop()


# In[5]:


if __name__ == "__main__":
    main()


# In[ ]:




