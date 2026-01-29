import pygame
import math

class Point():

    def __init__(self, x, y):
        super().__init__()
        
        self.image_corn = pygame.image.load('assets/points/corn.png').convert_alpha()
        self.rect = self.image_corn.get_rect(topleft=(x, y))

        self.width = 100
        self.height = 100 

        self.y = 0
        self.vel_y = 0
        self.gravity = 0.5

    def update(self):
        self.vel_y += self.gravity
        self.y += self.vel_y
    
    def draw(self, screen):
        screen.blit(self.image_corn, self.rect)

