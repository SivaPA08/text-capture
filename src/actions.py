class Actions:
    def __init__(self, fullscreen):
        self.fullscreen = fullscreen

    def onclick(self, event):
        start_x, start_y = event.x, event.y
        self.fullscreen.get(start_x, start_y)

    def holding(self, event):
        current_x, current_y = event.x, event.y
        self.fullscreen.modify_rectangle(current_x, current_y)

    def release(self, event):
        self.fullscreen.end(event.x, event.y)
