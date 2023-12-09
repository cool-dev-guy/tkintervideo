"""
Author: Goutham (cool-dev-guy)
This is the main player file.
"""
import moviepy.editor as mpe
from imageio import imwrite,RETURN_BYTES
from pydub import AudioSegment
from just_playback import Playback
from PIL import Image
import tkinter as tk
import threading

class Player(tk.Label):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.frame_image = tk.PhotoImage()
        self.config(image=self.frame_image,bg="#000000")
        self.cache_directory = 'cache'
        self.playback_h = 0
        self.playback_w = 0
        self.aspect_ratio = 0
        self.bind('<Configure>',self._resize)
        self._current_frame_size = 0
        self._keep_aspect_ratio = True
        self.playing = False
        self.paused = False
    def _resize(self, event):
        """ scales the label frame dynamically """
        new_width = event.width
        new_height = int(new_width / self.video.w * self.video.h)

        if self._keep_aspect_ratio:
            if new_height > event.height:
                new_height = event.height
                new_width = int(new_height / self.video.h * self.video.w)

        self._current_frame_size = (new_width, new_height)


    def load(self,file_path:str):
        self.video = mpe.VideoFileClip(file_path)
        self.audio = AudioSegment.from_file(file_path)
        self.audio.export(f'{self.cache_directory}/output.wav',format='wav')

        # SET PROPERTIES
        self.video_duration = self.video.duration
        self.video_fps = self.video.fps
        self.video_frames = self.video_duration * self.video_fps
        self.audio_rate = self.audio.frame_rate
        self.video_size = self.video.size

        self.video_w = self.video.w
        self.video_h = self.video.h
        self.playback_w = self.video_w
        self.playback_h = self.video_h

        self.aspect_ratio = self.video.w/self.video.h
    def _play(self):
        print('[LOGGER] : Playing Video ',self.video)
    
        self.playback = Playback()
        self.playback.load_file(f'{self.cache_directory}/output.wav')
        
        # SET PROPERTY
        self.control = self.playback
        """
        USE OF:
            - self.control.active   : return True if player is active(playing or paused) and false if inactive.
            - self.control.playing  : return True if player is playing and false if inactive.
            - self.control.volume   : return the volume
            - self.control.duration : return the duration(an alternative approach,based on `just_playback`)
            - self.control.curr_pos : return the current time its playing(alternative approach for `self.duration`)

        ALTERNATIVE OF:
            - self.control.play()   : plays loaded audio file from the beginning.[AUDIO ONLY - NOT IMPLEMENTED use `self.play()` instead]
            - self.control.pause()  : pauses playback. Has no effect if playback is already paused.
            - self.control.resume() : resumes playback. Has no effect if playback is playing.
            - self.control.stop()   : stops playback. Has no effect if playback is not active.[AUDIO ONLY - NOT IMPLEMENTED use `self.stop()` instead]

            - self.control.seek(second)         : positions playback at `second` from the start of the file
            - self.control.set_volume(0.5)      : sets the playback volume to 50% of the audio file's original value(value from 0 to 1)
        """

        self.playback.play()
        self.curr_time = 0
        while self.playback.active:
            if self._player_exit:break;
            self.numpy_array = self.video.get_frame(self.playback.curr_pos)
#            self.frame_image.config(data=f"P6\n{self.playback_w} {self.playback_h}\n255\n{Image.fromarray(self.numpy_array).resize((self.playback_w,self.playback_h)).tobytes().decode('latin-1')}")
            
            self.frame_image.config(data=imwrite(RETURN_BYTES,Image.fromarray(self.numpy_array).resize(self._current_frame_size), format='PPM'))
            self.curr_time = self.playback.curr_pos
            self.event_generate("<<Duration>>", when="tail")
    def play(self):
        self.playing = True
        self.paused = False
        self._player_exit = False
        self.play_thread = threading.Thread(target=self._play)
        self.play_thread.start()
    def pause(self):
        self.playing = False
        self.paused = True
        self.playback.pause()
    def stop(self):
        self.playing = False
        self.paused = False
        self.playback.stop()
    def resume(self):
        self.playing= True
        self.paused = False
        self.playback.resume()
    def stop(self):
        if self.play_thread:
            self._player_exit = True
            print("[TODO] kill thread")
        self.playback.stop()
    def seek(self,second:float):
        self.playback.seek(second)
