
from fullscreen import FullScreen as fs


class Actions:
    def __init__(self):
        pass


    def onclick(self,event):
        start_x,start_y=event.x,event.y
        fs.get(start_x,start_y)
    

    def holding(self,event):
        current_x,current_y=event.x,event.y
        fs.modifyrectange(current_x,current_y)

    def release(self,event):
        fs.end(event.x,event.y)
    
