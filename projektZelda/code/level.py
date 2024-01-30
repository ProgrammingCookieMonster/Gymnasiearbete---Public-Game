import pygame
from settings import *
from tile import Tile
from player import PLayer

class Level:
    def __init__(self):

        # get display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprite = pygame.sprite.Group()

        # sprite setup
        self.create_map()
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TITLESIZE
                y = row_index * TITLESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites], self.obstacle_sprites)
                if col == 'p':
                    PLayer((x, y), [self.visible_sprites])


    def run(self):
        # update and run the game
        self.visible_sprites.draw(self.display_surface)