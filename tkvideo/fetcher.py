"""
Author: Goutham (cool-dev-guy)
This is a TODO implementation of YT/HLS support
"""
import m3u8
import requests
class Backend:
    def __init__(self):
        self.cache_dir = ['cache/vid','cache/wav','cache/thumb']
        self.reset()
    def reset(self):
        self.total_duration = 0
    def load(self,playlist=None):
        self.playlist = m3u8.load(playlist)  # this could also be an absolute filename
        self.packets_len = len(self.playlist.segments)        
        print("packets: ",self.packets_len)
        # print(playlist.target_duration)

        for x,i in enumerate(self.playlist.segments):
            print(f"Reading: {i.title}{i.duration}")
            self.total_duration += i.duration
            uri = f'{i.base_uri}{i.uri}'
            with open(f'{self.cache_dir[0]}/t{x}.ts','wb') as cache_file:
                r = requests.get(uri)
                cache_file.write(r.content)
#backend = Backend()
#backend.load()
