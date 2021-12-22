import copy

direction_key = {"left": [-1, 0], "right": [1, 0], "down": [0, 1], "up": [0, -1]}

class snake:
    def __init__(self):
        self.direction = "none"
        self.last_position = self.segment(-1, -1)
        self.body = list()

    class segment:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    def set_direction(self, direction):
        if direction == "left" and self.direction != "right":
            self.direction = "left"
        elif direction == "right" and self.direction != "left":
            self.direction = "right"
        elif direction == "up" and self.direction != "down":
            self.direction = "up"
        elif direction == "down" and self.direction != "up":
            self.direction = "down"

    def move(self):
        self.last_position = copy.copy(self.body[-1])
        for i in reversed(range(1, len(self.body))):
            self.body[i] = copy.copy(self.body[i-1])
        if self.direction == "left" or self.direction == "right" or self.direction == "up" or self.direction == "down":
            self.body[0].x += direction_key[self.direction][0]
            self.body[0].y += direction_key[self.direction][1]


    def grow(self):
        new_segment = self.segment(self.last_position.x, self.last_position.y)
        self.body.append(new_segment)

    def get_head(self):
        return self.body[0]

    def respawn(self, x, y):
        self.body.clear()
        head = self.segment(x, y)
        self.body.append(head)