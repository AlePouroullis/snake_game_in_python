import pygame, const, random
from grid import grid
from snake import snake

class Game:
    def __init__(self):
        pygame.init()
        self.counter = 0
        self.screen = pygame.display.set_mode(const.size)
        self.running = True
        self.grid = grid(const.width/const.dimension, const.height/const.dimension)
        self.snake = snake(random.randint(1, self.grid.width-1), random.randint(1, self.grid.height-1))
        while self.running:
            self.Loop()


    def Loop(self):
        self.eventLoop()
        self.Draw()
        pygame.display.flip()

    def Draw(self):
        self.screen.fill((0, 0, 0))
        for x in range(0, int(self.grid.width)):
            for y in range(0, int(self.grid.height)):
                if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                    pygame.draw.rect(self.screen, const.grid_colour1, pygame.Rect(x * const.dimension, y*const.dimension, const.dimension, const.dimension))
                else:
                    pygame.draw.rect(self.screen, const.grid_colour2, pygame.Rect(x * const.dimension, y*const.dimension, const.dimension, const.dimension))
        pygame.draw.rect(self.screen, const.snake_colour, pygame.Rect(self.snake.head.x*const.dimension, self.snake.head.y*const.dimension, const.dimension, const.dimension))

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # get player input to move snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.set_direction("left")
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction("right")
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction("down")
                elif event.key == pygame.K_UP:
                    self.snake.set_direction("up")
        self.counter += 1
        if self.counter == 5:
            self.snake.move()
            self.counter = 0



if __name__ == '__main__':
    Game()
