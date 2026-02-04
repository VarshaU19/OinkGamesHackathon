import pygame
import math
import sys
import random
from character import *
from platformTiles import *
from cornPoints import *

# pygame setup
pygame.init()

screen = pygame.display.set_mode((800, 700))
tiles = create_tile_map('assets/background1/tileset1/pinkcloudsheet.PNG', 100)

pygame.display.set_caption('Hungry Piggy')
clock = pygame.time.Clock()

screen_width = screen.get_width()
screen_height = screen.get_height()

user = character(100, 100)
cornpoint = []
cornpoint.append(Point(random.randint(0, screen_width -80), -80))
score = 0
font = pygame.font.SysFont('mv boli', 40) # import font module to write on screen using font style and font size; already in system

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
            screen = pygame.display.set_mode((800, 700))
            background1 = scale_background1()
            foreground1_1 = scale_foreground1_1()
            foreground1_2 = scale_foreground1_2()

    # draws background images on screen in descending order
    screen.blit(background1, (0, 0))
    screen.blit(foreground1_1, (0, 0))
    screen.blit(foreground1_2, (0, 0))

    screen.blit(user.image, user.rect) # draw user with frames and rect
    score_text = font.render(f"Score: {score}", False, "white", None) # initialize score text with text, antialias, color, background
    screen.blit(score_text, (20, 10)) # draw score tracker on screen

    for point in cornpoint:
        point.update()
        if point.rect.colliderect(user): # when collision between user and corn
            cornpoint.remove(point)
            score += 1
            cornpoint.append(Point(random.randint(0, screen_width -80), -80))
            print(score)

        if point.rect.top > screen_height: # when corn falls past height of screen
            cornpoint.remove(point)
            cornpoint.append(Point(random.randint(0, screen_width -80), -80))

        point.draw(screen) 

    for cloud in tiles:
        if user.rect.colliderect(cloud.hit):
            user.vel_y = 0
            user.y = 0

    keys = pygame.key.get_pressed()  

    dt = clock.tick(60)  # limits FPS to 60
    user.update(keys, dt) #update frames for character
    tiles.update(dt) # updates tiles with the animation speed
    tiles.draw(screen) # draws the tiles on the screen 
    
    pygame.display.update()
pygame.quit()