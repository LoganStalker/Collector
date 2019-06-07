# import pygame_sdl2
# pygame_sdl2.import_as_pygame()
import pygame

from hero import Hero
from things import ThingsFactory
from settings import *

Size = namedtuple('Size', ['width', 'height'])
SIZE = Size(WIN_WIDTH, WIN_HEIGHT)

window = pygame.display.set_mode(SIZE)
screen = pygame.Surface(SIZE)

make_thing = ThingsFactory(screen)
hero1 = Hero(10, 10, surface=screen, color=COLORS.hero1)

things_list = []
things_on_the_ground = []

new_thing = make_thing.apple(90, 90)
things_list.append(new_thing)
things_on_the_ground.append(new_thing)

new_thing = make_thing.apple(90, 150)
things_list.append(new_thing)
things_on_the_ground.append(new_thing)

new_thing = make_thing.banana(220, 50)
things_list.append(new_thing)
things_on_the_ground.append(new_thing)

up = right = down = left = action = False
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_e:
                action = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_e:
                action = False
    screen.fill(COLORS.background_fill)

    hero1.update(up=up, right=right, down=down, left=left, action=action, things=things_on_the_ground)

    for thing in things_on_the_ground:
        thing.draw()

    window.blit(screen, (0, 0))
    pygame.display.flip()