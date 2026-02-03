import pygame 
import math 

tilemap = [

'.................',
'.................',
'.................',
'.................',
'###.....####.....',
'...####......####',
'........####.....',
'####..####...####',

]

tilemap_width = 800
tilemap_height = 800

class platformClouds(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()

        self.cloudsheet = pygame.image.load('assets/background1/tileset1/pinkcloudsheet.PNG').convert_alpha()

        # frame dimensions
        self.frame_width = 150
        self.frame_height = 150 

        # load frames
        self.spritesheet_frames = self.load_frames(self.cloudsheet, 2)

        self.cloud_frames = [
            pygame.transform.scale(frame, (100, 100)) for frame in self.cloud_frames
        ]

        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.5

        self.cloud = self.cloudsheet[0]
        self.rect = self.cloudsheet.get_rect(center=(x, y))

    def load_frames(self, sheet, num_frames):
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface(
                (i * self.frame_width, 0, self.frame_height, self.frame_width)
            ).copy()
            frames.append(frame)
        return frames

    def update(self, dt):
        
        self.animation_timer += dt / 1000
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_index += 1

        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

    def create_tilemap(screen_size):
        screen_width = 800
        screen_height = 800

        tile_size = min(
            screen_height / tilemap_height, 
            screen_width / tilemap_width
        )

        

