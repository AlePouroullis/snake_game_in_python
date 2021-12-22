import pygame, const, random
from grid import grid
from snake import snake
from food import food

class Game:
    def __init__(self):
        pygame.init()
        self.counter = 0
        self.screen = pygame.display.set_mode(const.size)
        self.running = True
        self.grid = grid(const.width/const.dimension, const.height/const.dimension)
        self.snake = snake()
        self.food = food()
        self.spawn_snake()
        self.spawn_food()
        while self.running:
            self.Loop()

    def spawn_snake(self):
        self.snake.direction = "none"
        snake_pos_x, snake_pos_y = random.randint(1, self.grid.width - 1), random.randint(1, self.grid.height - 1) - 1
        self.snake.respawn(snake_pos_x, snake_pos_y)

    def spawn_food(self):
        while True:
            food_pos_x, food_pos_y = random.randint(0, self.grid.width-1), random.randint(0, self.grid.height-1)
            valid = True
            for segment in self.snake.body:
                if segment.x == food_pos_x and segment.y == food_pos_y:
                    valid = False
                    break
            if valid:
                break
        self.food.respawn(food_pos_x, food_pos_y)


    def Loop(self):
        self.eventLoop()
        self.Draw()
        pygame.display.flip()

    def Draw(self):
        self.draw_grid()
        self.draw_snake()
        self.draw_food()

    def draw_snake(self):
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, const.snake_colour, (segment.x*const.dimension, segment.y*const.dimension, const.dimension, const.dimension))

    def draw_grid(self):
        for x in range(0, int(self.grid.width)):
            for y in range(0, int(self.grid.height)):
                if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
                    pygame.draw.rect(self.screen, const.grid_colour1, (x * const.dimension, y * const.dimension, const.dimension,
                                                 const.dimension))
                else:
                    pygame.draw.rect(self.screen, const.grid_colour2, (x * const.dimension, y * const.dimension, const.dimension,
                                                 const.dimension))

    def draw_food(self):
        pygame.draw.rect(self.screen, const.food_colour, (self.food.x*const.dimension, self.food.y*const.dimension, const.dimension, const.dimension))

    def check_collision_with_boundaries(self):
        snake_head = self.snake.get_head()
        if snake_head.x < 0 or snake_head.x > self.grid.width or snake_head.y < 0 or snake_head.y > self.grid.height:
            self.game_over()

    def check_for_collision_with_snake(self):
        for segment in self.snake.body[1:]:
            if self.snake.body[0].x == segment.x and self.snake.body[0].y == segment.y:
                self.game_over()

    def game_over(self):
        self.spawn_snake()
        self.spawn_food()

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
            self.check_collision_with_boundaries()
            self.check_for_collision_with_snake()
            snake_head = self.snake.get_head()
            if snake_head.x == self.food.x and snake_head.y == self.food.y:
                self.snake.grow()
                self.spawn_food()
            self.counter = 0


if __name__ == '__main__':
    Game()
