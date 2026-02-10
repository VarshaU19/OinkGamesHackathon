import pygame

class platformClouds(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sheet = pygame.image.load("assets/background1/tileset1/pinkcloudsheet.png").convert_alpha()
        self.frame_width = 100
        self.frame_height = 48

        self.frames = self.load_frames()
        self.image = self.frames[0]
        self.rect = self.sheet.get_rect(topleft=(x, y))

        self.animation_speed = 0.5
        self.animation_index = 0
        self.animation_timer = 0

    def load_frames(self):
        frames = []
        self.sheet_width = 200
        num_frames = self.sheet_width // self.frame_width 
        for i in range(num_frames):
            frame = self.sheet.subsurface(
                (i * self.frame_width, 0, self.frame_width, self.frame_height)
            ).copy()
            frames.append(frame)

        return frames

    def update(self, dt):
        self.animation_timer += dt / 1000
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_index += 1
            self.animation_index %= len(self.frames)
            self.image = self.frames[self.animation_index]



