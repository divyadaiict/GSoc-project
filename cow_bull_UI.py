import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import cow_bull_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    cow_bull_support.set_Tk_var()
    top = Cow_and_Bull (root)
    cow_bull_support.init(root, top)
    root.mainloop()

w = None
def create_Cow_and_Bull(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    cow_bull_support.set_Tk_var()
    top = Cow_and_Bull (w)
    cow_bull_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Cow_and_Bull():
    global w
    w.destroy()
    w = None


class Cow_and_Bull:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family Arial -size 11 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("396x449+472+140")
        top.title("Cow and Bull")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.05, rely=0.02, relheight=0.95, relwidth=0.9)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=355)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.06, rely=0.14, height=34, width=77)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''New Game''')
        self.Button1.configure(width=77)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.7, rely=0.14, height=34, width=77)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Quit''')
        self.Button2.configure(width=77)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.23, rely=0.28,height=30, relwidth=0.52)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font9)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=cow_bull_support.Enter)
        self.Entry1.configure(width=184)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.82, rely=0.28, height=34, width=37)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''ok''')
        self.Button3.configure(width=37)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.03, rely=0.28, height=31, width=44)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Input :''')
        self.Label1.configure(width=44)

        self.Message1 = Message(self.Frame1)
        self.Message1.place(relx=0.08, rely=0.02, relheight=0.1, relwidth=0.82)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Welcome to cow and bull game''')
        self.Message1.configure(width=290)






if __name__ == '__main__':
    vp_start_gui()
