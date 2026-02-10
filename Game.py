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

pygame.display.set_caption('Hungry Piggy')
clock = pygame.time.Clock()

screen_width = screen.get_width()
screen_height = screen.get_height()

user = character(100, 100)
tile1 = platformClouds(100, 350)
tile2 = platformClouds(300, 450)
tile3 = platformClouds(400, 450)
tile4 = platformClouds(550, 350)
tile5 = platformClouds(650, 350)
tile6 = platformClouds(0, 525)
tile7 = platformClouds(100, 525)
tile8 = platformClouds(600, 550)
tile9 = platformClouds(250, 600)

tile9_vel = 4
tile1_vel = 2
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

def draw_game_over():
    screen.fill('#ffe6f2')
    font = pygame.font.SysFont('mv boli', 40)
    title = font.render('Game Over', False, 'white')
    restart = font.render('Try Again', False, 'white')
    quit_text = font.render('Quit', False, 'white') 

    screen.blit(title, (screen_width//2 - title.get_width()//2, screen_height//3))
    screen.blit(restart, (screen_height //2 - restart.get_width()//2, screen_height//2))
    screen.blit(quit_text, (screen_width//2 - quit_text.get_width()//2, screen_height//1.5))
    pygame.display.update()

running = True
game_over = False
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                user.jumping()

    # draws background images on screen in descending order
    screen.blit(background1, (0, 0))
    screen.blit(foreground1_1, (0, 0))
    screen.blit(foreground1_2, (0, 0))

    screen.blit(tile1.image, tile1.rect)
    screen.blit(tile2.image, tile2.rect)
    screen.blit(tile3.image, tile3.rect)
    screen.blit(tile4.image, tile4.rect)
    screen.blit(tile5.image, tile5.rect)
    screen.blit(tile6.image, tile6.rect)
    screen.blit(tile7.image, tile7.rect)
    screen.blit(tile8.image, tile8.rect)
    screen.blit(tile9.image, tile9.rect)

    if tile9.rect.left >= 450 or tile9.rect.left< 250:
        tile9_vel *= -1

    tile9.rect.left += tile9_vel

    if tile1.rect.left >= 300 or tile1.rect.left < 100:
        tile1_vel *= -1
    
    tile1.rect.left += tile1_vel

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
            game_over = True
            if game_over:
                draw_game_over()

        point.draw(screen)

    keys = pygame.key.get_pressed()  

    dt = clock.tick(60)  # limits FPS to 60
    user.update(keys, dt) #update frames for character=
    tile1.update(dt)
    tile2.update(dt)
    tile3.update(dt)
    tile4.update(dt)
    tile5.update(dt)
    tile6.update(dt)
    tile7.update(dt)
    tile8.update(dt)
    tile9.update(dt)
    pygame.display.update()
pygame.quit()