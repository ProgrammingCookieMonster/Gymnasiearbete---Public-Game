import asyncio
import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        # general settings
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()

        # sounds
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.3)
        main_sound.play(loops = - 1)

        # outside look
        pygame.display.set_caption("Runeblade Rhapsody")  # Setting custom window name
        game_icon = pygame.image.load("graphics/runeblade_test_icon.png")  # Setting custom icon to the game window
        pygame.display.set_icon(game_icon)

    async def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type ==  pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            await asyncio.sleep(0)

if __name__ == '__main__':
    game = Game()
    asyncio.run( game.run())
