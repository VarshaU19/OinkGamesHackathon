import pygame
import math
import sys
import random

class Point():

    def __init__(self, x, y):
        super().__init__()
        
        self.image_corn = pygame.image.load('assets/points/corn.png').convert_alpha()
        self.rect = self.image_corn.get_rect(topleft=(x, y))

        self.width = 100
        self.height = 100 

    def draw(self, screen):
        screen.blit(self.image_corn, self.rect)

    

