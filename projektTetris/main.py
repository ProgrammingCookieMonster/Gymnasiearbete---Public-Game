#The main file for the code of the game Tetris.
import pygame,sys
from game import Game

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600)) #game screen
pygame.display.set_caption("Tetris (Python version)")

clock = pygame.time.Clock()

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: #movement
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
    #Drawing
    screen.fill(dark_blue) #background color
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)