"""
Author: Goutham (cool-dev-guy)
This is the tools file..
"""
import tkinter as tk
from tkinter import ttk
from .player import Player
import time
class Controls(tk.Frame):
    def __init__(self, parent:Player, player, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.player = player
        # grid
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=0)
        self.columnconfigure(2,weight=0)
        self.columnconfigure(3,weight=0)
        self.columnconfigure(4,weight=1)
        self.columnconfigure(5,weight=0)

        self.rowconfigure(0,weight=1)

        # sub widgets
        self.play_button = ttk.Button(self,text="▶",command=self.play_pause)
        self.play_button.grid(row=0,column=0,sticky=tk.NSEW,padx=5,pady=5)

        self.bskip_button = ttk.Button(self,text='- 10s',command=lambda:self.player.seek(self.player.curr_time-10))
        self.bskip_button.grid(row=0,column=1,sticky=tk.NSEW,padx=5,pady=5)
        self.fskip_button = ttk.Button(self,text='+ 10s',command=lambda:self.player.seek(self.player.curr_time+10))
        self.fskip_button.grid(row=0,column=2,sticky=tk.NSEW,padx=5,pady=5)
        self.seeking = False
        self.scale = ttk.Scale(self,from_=0,to_=100)
        self.scale.grid(row=0,column=4,sticky=tk.NSEW,padx=5,pady=5)

        self.currn_time_label = tk.Label(self,text="00:00:00")
        self.total_time_label = tk.Label(self,text="00:00:00")

        self.currn_time_label.grid(row=0,column=3,sticky=tk.NSEW,padx=5,pady=5)
        self.total_time_label.grid(row=0,column=5,sticky=tk.NSEW,padx=5,pady=5)

        
        self.scale.bind("<Button-1>", self.seek)
        self.scale.bind("<ButtonRelease-1>", self.seek_release)
    def play_pause(self):
        if self.player.playing:
            self.player.pause()
            self.play_button.config(text="▶")
            time.sleep(0.1)
        elif self.player.paused:
            self.player.resume()
            self.play_button.config(text="II")
        else:
            self.play_button.config(text="II")
            self.player.play()
    def seek(self,event=None):
        self.play_pause()
    def seek_release(self,event=None):
        self.player.seek(self.scale.get())
        self.play_pause()
    def get_time_format(self,time):
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
    def update_scale(self,event):
        if not self.player.control.paused:
            self.scale.set(int(self.player.curr_time))
            self.scale.configure(to=self.player.video_duration)

            self.total_time_label.config(text = self.get_time_format(self.player.video_duration))
            self.currn_time_label.config(text = self.get_time_format(self.player.curr_time))
