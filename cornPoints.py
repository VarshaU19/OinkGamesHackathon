import pygame

class Point():

    def __init__(self, x, y):
        super().__init__()
        
        self.image_corn = pygame.image.load('assets/points/corn.png').convert_alpha()
        self.rect = self.image_corn.get_rect(topleft=(x, y))

        self.width = 80
        self.height = 80 

    def draw(self, screen):
        screen.blit(self.image_corn, self.rect)

        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

    

