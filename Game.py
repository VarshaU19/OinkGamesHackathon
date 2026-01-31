# Example file showing a basic pygame "game loop"
import pygame
import math
import sys
import random
from character import *
from platformTiles import *
from cornPoints import Point

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1000, 900), pygame.RESIZABLE)
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

screen_width = screen.get_width()
screen_height = screen.get_height()
gravity = .5
vel_y = 30
cornpoint_y = 0

user = character(150, 150)
tiles, tiles_size = create_tile_map(screen.get_size(), 'assets/background1/tileset1/pinkcloudsheet.PNG')
cornpoint = []
cornpoint.append(Point(random.randint(0, screen_width - 100), -50))

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
            #scale background images to fit window size upon change
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            tiles, tiles_size = create_tile_map(screen.get_size(), 'assets/background1/tileset1/pinkcloudsheet.PNG')
            background1 = scale_background1()
            foreground1_1 = scale_foreground1_1()
            foreground1_2 = scale_foreground1_2()

    # flip() the display to put your work on screen
    screen.blit(background1, (0, 0))
    screen.blit(foreground1_1, (0, 0))
    screen.blit(foreground1_2, (0, 0))

    screen.blit(user.image, user.rect)

    for point in cornpoint:
        
        cornpoint_y = cornpoint_y + vel_y
        if cornpoint_y > screen_height:
            cornpoint_y = -25

        if point.rect.colliderect(user):
            cornpoint.remove(point)
            new_point = random.randint(0, screen_width - 30)
            cornpoint.append(Point(new_point, - 50))
        point.draw(screen)
        
    keys = pygame.key.get_pressed()      

    dt = clock.tick(60)  # limits FPS to 60
    user.update(keys, dt) #update frames for character
    tiles.update(dt) # update frames for tiles 
    
    tiles.draw(screen) #draws tiles according to map on screen

    pygame.display.update()

pygame.quit()