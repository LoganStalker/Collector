import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame

from settings import *

class Thing:
    def __init__(self, x, y, name, surface=None, color=(200, 100, 200)):
        self.image = pygame.Surface((30, 30))
        self.name = name
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.surface = surface

    def draw(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.draw()

class ThingsNames:
    apple = 'apple'
    banana = 'banana'

class ThingsFactory:
    def __init__(self, surface):
        self.surface = surface
    def apple(self, x, y):
        return Thing(x, y, ThingsNames.apple, surface=self.surface, color=(50, 250, 50))
    def banana(self, x, y):
        return Thing(x, y, ThingsNames.banana, surface=self.surface, color=(250, 250, 50))