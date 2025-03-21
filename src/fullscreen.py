import tkinter as tk
from PIL import ImageGrab, ImageTk
from actions import Actions
import os
import sys

class FullScreen:
    def __init__(self, master):
        self.master = master
        self.start_x = None
        self.start_y = None
        self.rectangle = None

        #get the fullscreen code
        self.fullscreen_image = ImageGrab.grab()
        self.photo = ImageTk.PhotoImage(self.fullscreen_image)

        # screenshot as background
        self.canvas = tk.Canvas(master, width=self.fullscreen_image.width, height=self.fullscreen_image.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.photo, anchor="nw")

        # for actions
        self.actions = Actions(self)
        self.canvas.bind("<ButtonPress-1>", self.actions.onclick)
        self.canvas.bind("<B1-Motion>", self.actions.holding)
        self.canvas.bind("<ButtonRelease-1>", self.actions.release)

    def get(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.rectangle = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y,
                                                      outline="red", width=2)

    def modify_rectangle(self, x, y):
        if self.rectangle is not None:
            self.canvas.coords(self.rectangle, self.start_x, self.start_y, x, y)

    def end(self, end_x, end_y):
        #rectange
        x1, y1 = min(self.start_x, end_x), min(self.start_y, end_y)
        x2, y2 = max(self.start_x, end_x), max(self.start_y, end_y)

        #croping
        cropped_image = self.fullscreen_image.crop((x1, y1, x2, y2))
        cropped_image.save("screenshot.png")
        print("saved as screenshot.png")
        from get_text import Text as txt

        txt.extract_text()
        
        image="screenshot.png"

        if os.path.exists(image):
            os.remove(image)
        else:
            print("Error")


        sys.exit(0)

