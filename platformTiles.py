import pygame

class platformClouds(pygame.sprite.Sprite):
    def __init__(self, x, y ):
        super().__init__()

        self.cloud_image = pygame.image.load('assets/background1/tileset1/pinkcloudsheet.PNG')

        self.frame_width = 100
        self.frame_height = 100

        self.spritesheet_frames = self.load_frames(self.cloud_image, 2)

        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.5

        # start with first frame
        self.image = self.spritesheet_frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))

    def load_frames(self, sheet, num_frames):
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface(
                (i * self.frame_width, 0, self.frame_width, self.frame_height)
            ).copy()
            frames.append(frame)
        return frames

    def update(self, dt):
        self.animation_timer += dt / 1000
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_index = (self.animation_index + 1) % len(self.spritesheet_frames)
            self.image = pygame.transform.scale(
                self.spritesheet_frames[self.animation_index],
                (self.rect.width, self.rect.height)
            )
