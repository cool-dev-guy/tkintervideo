# tkintervideo

A simple Tkinter Python Package For synced audio & video playback with a real-time API.

## Installation
- From PyPi
    - ```bash
      pip install tkvideo
      ```
- From source
    - ```bash
      pip install -r requirements.txt
      ```
    - Build it normally(refer web).
## Features:

    - Controls Widget Added
    - Timeline seeking.(slider based & button based)
    - Synced audio playback.(Video is synced with audio)
    - Upto any Resolution video playback(using PIL & imageio)
    - TODO: youtube/hls support.
    - In-player real-time audio & video edits.


    - duration
    - fps
    - audio frame rate
    - state detection
    - auto resize(based on window resize)
    - total frames
    - current play position
    - seeking(to a second or a frame)
    - play/pause/stop/resume
    - volume
    - edits(you can edit the video & audio because moviepy & pydub are built-in)
## Usage

```python
from tkvideo.tkvideo import player
from tkvideo.tkvideo.tools import Controls
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
```

## Contributing

Pull requests are welcome.

## License

[GPL-3](https://choosealicense.com/licenses/gpl-3.0/)
