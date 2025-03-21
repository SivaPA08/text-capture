import tkinter as tk
from PIL import ImageGrab,ImageTk
from pynput import keyboard  # type: ignore

from actions import Actions as ac

class FullScreen:
    def __init__(self,master):
        self.master=master
        self.start_x,self.start_y=None,None #starting of corrdinates

        self.rectangle=None

        self.fullscreen_image=ImageGrab.grab()
        self.photo=ImageTk.PhotoImage(self.fullscreen_image)


        self.canvas=tk.Canvas(master, width=self.fullscreen_image.width, height=self.fullscreen_image.height)
        self.canvas.pack()
        self.canvas.create_image(0,0,image=self.photo, anchor="nw")




        self.canvas.bind("<ButtonPress-1>", ac.onclick)
        self.canvas.bind("<B1-Motion>", ac.holding)
        self.canvas.bind("<ButtonRelease-1>", ac.release)
    
    def get(self,start_x,start_y):
        self.start_x=start_x
        self.start_y=start_y
        self.rectangle=self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red", width=2)
    
    def modifyrectange(self,x,y):
        self.canvas.coords(self.rect, self.start_x, self.start_y, x, y)
    

    def end(self, end_x,end_y):
        
        x1, y1 = min(self.start_x, end_x), min(self.start_y, end_y)
        x2, y2 = max(self.start_x, end_x), max(self.start_y, end_y)

        
        cropped_image = self.fullscreen_image.crop((x1, y1, x2, y2))
        cropped_image.save("screenshot.png")
        print("Screenshot saved as 'screenshot.png'")
        self.master.quit()

    
