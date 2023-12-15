# tkintervideo

A simple Tkinter Python Package For synced audio & video playback with a real-time API.

`beta 0.0.3`
<p align="center">
<img src="https://github.com/cool-dev-guy/tkintervideo/assets/116984615/73b591e6-234e-464b-9e0d-2a350ca73946)" width=100% height=100%>
</p>

## Installation
- From PyPi
    - ```bash
      pip install tkvideo
      ```
- If any error's:
    - ```bash
      pip install -r requirements.txt
      ```
    - Or Build it normally(refer web).
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

### Buy me a cool-milk for support & updates

<a href="https://www.buymeacoffee.com/cooldevguy"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a cool-milk&emoji=🥛&slug=cooldevguy&button_colour=49a835&font_colour=ffffff&font_family=Comic&outline_colour=ffffff&coffee_colour=FFDD00" /></a>

    (Note: Two buttons are the same,added both because i like the color.)

## Usage

```python
from tkintervideo import player
from tkintervideo.tools import Controls
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
