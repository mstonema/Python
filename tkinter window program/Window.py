import tkinter   

class Window:
    def __init__(self):
        self.window = tkinter.Tk()

        self.window.title('Title Goes Here')
        self.window.geometry('360x256')

    def runWindow(self):
        self.window.mainloop()
        
    def menu(self):
        menubar = tkinter.Menu()
        filemenu = tkinter.Menu(menubar, tearoff = 0)

        #commands not implemented yet.
        filemenu.add_command(label='New', command = '')
        filemenu.add_command(label='Open', command = '')
        filemenu.add_command(label='Save', command = '')
        filemenu.add_command(label='Save as...', command = '')
        filemenu.add_command(label='Close', command = '')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command = self.window.destroy)
        menubar.add_cascade(label = 'File', menu = filemenu)

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
        helpmenu.add_command(label = 'About...', command = '')
        menubar.add_cascade(label = 'Help', menu = helpmenu)

        #This binds the menubar to menu which then make it display.
        self.window.config(menu = menubar)
        

        
