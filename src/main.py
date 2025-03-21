from launch import Launch
from pynput import keyboard  # type: ignore

hotkey = '<cmd>+<ctrl>+<shift>+p'
print(f"Waiting for hotkey {hotkey} to launch screenshot tool...")

launch = Launch()

with keyboard.GlobalHotKeys({hotkey: launch.on_activate}) as listener:
    listener.join()
