import pygame, sys
from settings import *
from level import Level
# from debug import debug

class Game:
    def __init__(self):

        # general settings
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        pygame.display.set_caption("Runeblade Rhapsody")  # Setting custom window name
        game_icon = pygame.image.load("../graphics/runeblade_test_icon.png")  # Setting custom icon to the game window
        pygame.display.set_icon(game_icon)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            # debug('This called function is going to check some stuff later')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
