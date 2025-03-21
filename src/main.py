from launch import Launch
from pynput import keyboard  # type: ignore

hotkey = '<cmd>+<ctrl>+<shift>+p'
print("Here <cmd> means windows key")
print(f"Press the {hotkey} to start")

launch = Launch()

with keyboard.GlobalHotKeys({hotkey: launch.on_activate}) as listener:
    listener.join()
