class snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def respawn(self, x, y):
        self.x = x
        self.y = y