import pygame_sdl2
pygame_sdl2.import_as_pygame()
import pygame

from settings import *
from things import ThingsNames

class Backpack:
    def __init__(self, x, y, surface):
        self.image = pygame.Surface((400, 40))
        self.background_color = (40, 40, 40)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.surface = surface
        self.things = []

    def add(self, thing):
        if len(self.things) < 10:
            thing.rect.x = 5 + (len(self.things) * (thing.rect.width + 5))
            thing.rect.y = 5
            self.things.append(thing)
    def delete(self, thing):
        self.things.remove(thing)
    def draw(self):
        self.image.fill(self.background_color)
        for thing in self.things:
            self.image.blit(thing.image, (thing.rect.x, thing.rect.y))
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
    def __len__(self):
        return len(self.things)
    def __iter__(self):
        return self.things.__iter__()

class Hero:
    def __init__(self, x, y, surface=None, color=(200, 100, 100)):
        self.image = pygame.Surface((30, 30))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 1
        self.speedx = 0
        self.speedy = 0
        self.surface = surface
        self.backpack = Backpack((WIN_WIDTH - 400)/2, WIN_HEIGHT - 50, surface=self.surface)

    def draw(self):
        self.backpack.draw()
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, up, right, down, left, action, things):
        if up:
            self.speedy = -self.vel
        if down:
            self.speedy = self.vel
        if left:
            self.speedx = -self.vel
        if right:
            self.speedx = self.vel

        if action:
            for thing in things:
                if self.rect.colliderect(thing.rect):
                    self.backpack.add(thing)
            for bt in self.backpack:
                if bt in things:
                    things.remove(bt)

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right >= WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
        self.speedx = 0
        self.speedy = 0
        self.draw()