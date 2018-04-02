import tkinter

def aboutClick():
        a = About()

class Program(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title('title goes here')
        self.geometry('480x360')

    def menu(self):
        menubar = tkinter.Menu()
        filemenu = tkinter.Menu(menubar, tearoff = 0)

        #commands not implemented yet.
        filemenu.add_command(label='New', command='')
        filemenu.add_command(label='Open', command='')
        filemenu.add_command(label='Save', command='')
        filemenu.add_command(label='Save as...', command='')
        filemenu.add_command(label='Close', command='')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.destroy)
        menubar.add_cascade(label='File', menu=filemenu)

        #commands not implemented yet.
        editmenu = tkinter.Menu(menubar, tearoff = 0)
        editmenu.add_command(label = 'Undo', command = '')
        editmenu.add_separator()
        editmenu.add_command(label = 'Cut', command = '')
        editmenu.add_command(label = 'Copy', command = '')
        editmenu.add_command(label = 'Paste', command = '')
        editmenu.add_command(label = 'Delete', command = '')
        editmenu.add_command(label = 'Select All', command = '')
        menubar.add_cascade(label = 'Edit', menu = editmenu )

        #commands not implemented yet.
        helpmenu = tkinter.Menu(menubar, tearoff = 0)
        helpmenu.add_command(label = 'Help Index', command = '')
        helpmenu.add_command(label = 'About...', command = aboutClick )
        menubar.add_cascade(label = 'Help', menu = helpmenu)
        
        #This binds the menubar to the menu which then makes it display
        self.config(menu = menubar)

class About(tkinter.Toplevel):

    def __init__(self):
        tkinter.Toplevel.__init__(self)
        
        label = tkinter.Label(self, text='Author: Mike Stoneman')
        label.pack(pady=10, padx=10)
        self.geometry('240x120')
        self.title('')

        
