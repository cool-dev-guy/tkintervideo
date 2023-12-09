from tkvideo import player
from tkvideo.tools import Controls
import tkinter as tk
from tkinter import ttk
import sv_ttk
import time

class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        sv_ttk.set_theme('dark')
        self.m_widget = player.Player(self,height=200,width=300)

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=0)
        self.columnconfigure(0,weight=1)

        self.m_widget.grid(column=0,row=0,sticky=tk.NSEW,padx=5,pady=5)
        self.m_widget.load('output.avi')

        self.controls = Controls(self,self.m_widget)
        self.m_widget.bind("<<Duration>>",self.controls.update_scale)
        self.controls.grid(column=0,row=1,sticky=tk.NSEW,padx=10,pady=10)
myApp = App()
myApp.mainloop()
