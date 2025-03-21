import tkinter as tk
from fullscreen import FullScreen

class Launch:
    def __init__(self):
        pass

    def launch_screenshot_tool(self):
        root = tk.Tk()
        root.attributes("-fullscreen", True)
        app = FullScreen(root)
        root.mainloop()

    def on_activate(self):
        print("hotkey pressed successfully")
        self.launch_screenshot_tool()
