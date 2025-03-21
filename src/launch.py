from fullscreen import FullScreen as fs
import tkinter as tk
from PIL import ImageGrab, ImageTk
from pynput import keyboard #type: ignore

class Launch:
    def __init__(self):
        pass

    def launch_screenshot_tool():
        root=tk.Tk()
        root.attributes("-fullscreen",True)
        app=fs(root)
        root.mainloop()
    
    def on_activate():
        print("Hotkey pressed! Launching screenshot tool...")
        listener.stop()  # Stop listening for the hotkey
        launch_screenshot_tool()
