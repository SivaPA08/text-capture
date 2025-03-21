from fullscreen import FullScreen as fs
from launch import Launch as l
import tkinter as tk
from PIL import ImageGrab, ImageTk
from pynput import keyboard #type: ignore

hotkey = '<cmd>+<ctrl>+<shift>+p'
print(f"Waiting for hotkey {hotkey} to launch screenshot tool...")

with keyboard.GlobalHotKeys({hotkey: l.on_activate}) as listener:
    listener.join()