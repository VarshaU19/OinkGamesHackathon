import pygame

class Point(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image_corn = pygame.image.load('assets/points/corn.PNG').convert_alpha()
        
        self.image_corn = pygame.transform.scale(self.image_corn, (80, 80))
        self.rect = self.image_corn.get_rect(topleft=(x, y)) # position of corn
        
        self.vel_y = 0 # speed of vertical movement
        self.gravity = 0.3 

    def update(self): 
        self.vel_y += self.gravity # gravity makes the corn fall exponentially faster 
        self.rect.y += self.vel_y 
        # self.rect.y = where character is on the screen from top to bottom
        # moves corn down the screen at set speed

    def draw(self, screen):
        screen.blit(self.image_corn, self.rect)



