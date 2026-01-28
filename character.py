import pygame 
import math

class character(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image_sheet = pygame.image.load('assets/characters/idle.PNG').convert_alpha()

        self.frame_width = 150
        self.frame_height = 150
        self.num_frames = 2

        self.idle_frames = self.load_frames(self.image_sheet, self.frame_height, self.frame_width, self.num_frames)
        self.idle_frames = [pygame.transform.scale(frame, (75, 75)) for frame in self.idle_frames]

        self.animation_speed = .3
        self.animation_index = 0
        self.animation_timer = 0

        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def load_frames(self, sheet, frame_width, frame_height, num_frames):
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames
    
    def update(self, keys, dt):
        self.animation_timer += dt/ 1000 # make sure that the dt is in seconds
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_index = (self.animation_index + 1) % len(self.idle_frames)
            self.image = self.idle_frames[self.animation_index]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 15
        if keys[pygame.K_d]:
            self.rect.x += 15
        if keys[pygame.K_w]:
            self.rect.y -= 15
        if keys[pygame.K_s]:
            self.rect.y += 15

        self.rect.clamp_ip(pygame.display.get_surface().get_rect())
