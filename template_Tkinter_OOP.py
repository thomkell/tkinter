# mainfile to combine all files
# -*- coding: utf-8 -*-

#libraries
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory

# import ohter files\classes
# import parameters

class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # field options
        options = {'padx': 5, 'pady': 5}

        # Entries
        self.folderE = tk.StringVar()
        self.folderEntry = ttk.Entry(self, width=40, textvariable=self.folderE)
        self.folderEntry.grid(column=0, row=1, sticky=tk.W, **options)
        self.folderEntry.focus()

        self.XButton = ttk.Button(self, text='Select folder', command=self.selectfolderOld)
        self.XButton.grid(column=0, row=2, **options, sticky=tk.W)

    def selectfolderOld(self):
        # Load Last Caldata
        #self.file = askopenfilename(title='Select Folder')
        self.path = askdirectory(title='Select Folder') # shows dialog box and return the path
        self.folderEntry.delete(0, 'end') # clear entry
        self.folderEntry.insert(0, self.path) # insert path

if __name__ == "__main__":
    # create the application
    myapp = tk.Tk()

    # here are method calls to the window manager class
    myapp.title("Test")
    myapp.geometry('400x200')
    myapp.resizable(0, 0)

    App(myapp)
    myapp.mainloop()