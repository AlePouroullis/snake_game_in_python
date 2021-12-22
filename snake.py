direction_key = {"left": [-1, 0], "right": [1, 0], "down": [0, 1], "up": [0, -1]}

class snake:
    def __init__(self, x, y):
        self.head = self.Head(x, y)
        self.direction = "none"

    class Head:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    def set_direction(self, direction):
        if direction == "left" and self.direction != "left":
            self.direction = "left"
        elif direction == "right" and self.direction != "right":
            self.direction = "right"
        elif direction == "up" and self.direction != "up":
            self.direction = "up"
        elif direction == "down" and self.direction != "down":
            self.direction = "down"

    def move(self):
        if self.direction == "left" or self.direction == "right" or self.direction == "up" or self.direction == "down":
            self.head.x += direction_key[self.direction][0]
            self.head.y += direction_key[self.direction][1]


    def game_over(self):
        pass

    def respawn(self, x, y):
        self.head = self.x, self.y = x, y