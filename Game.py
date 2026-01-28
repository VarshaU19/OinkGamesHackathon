# Example file showing a basic pygame "game loop"
import pygame
import math
from character import *

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1000, 900), pygame.RESIZABLE)
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

character_image = pygame.Surface((225, 225)).convert_alpha()
user = character(150, 150)
screen.blit(character_image, (150, 150))

background1 = pygame.image.load('assets/background1/1.png')
foreground1_1= pygame.image.load('assets/background1/2.png')
foreground1_2 = pygame.image.load('assets/background1/3.png')
def scale_background1():
    return pygame.transform.scale(background1, screen.get_size())
def scale_foreground1_1():
    return pygame.transform.scale(foreground1_1, screen.get_size())
def scale_foreground1_2():
    return pygame.transform.scale(foreground1_2, screen.get_size())

background1 = scale_background1()
foreground1_1 = scale_foreground1_1()
foreground1_2 = scale_foreground1_2()

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            background1 = scale_background1()
            foreground1_1 = scale_foreground1_1()
            foreground1_2 = scale_foreground1_2()

    # flip() the display to put your work on screen
    screen.blit(background1, (0, 0))
    screen.blit(foreground1_1, (0, 0))
    screen.blit(foreground1_2, (0, 0))

    screen.blit(user.image, user.rect)
    keys = pygame.key.get_pressed()
    
    dt = clock.tick(60)  # limits FPS to 60
    user.update(keys, dt)

    pygame.display.update()

pygame.quit()