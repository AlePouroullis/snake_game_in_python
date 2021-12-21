import pygame, const

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(const.size)

        while True:
            self.Loop()

    def Loop(self):
        self.eventLoop()
        self.Draw()
        pygame.display.flip()

    def Draw(self):
        self.screen.fill((0, 0, 0))

    def eventLoop(self):
        pass


if __name__ == '__main__':
    print("hello world")
    Game()
