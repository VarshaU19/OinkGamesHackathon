import pygame
import math

class character(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        # Load sprite sheets
        self.idle_sheet = pygame.image.load(
            'assets/characters/idle.PNG'
        ).convert_alpha()

        self.walk_sheet = pygame.image.load(
            'assets/characters/walking.PNG'
        ).convert_alpha()

        # Frame sizes
        self.frame_width = 150
        self.frame_height = 150

        # Load frames
        self.idle_frames = self.load_frames(self.idle_sheet, 2)
        self.walk_frames = self.load_frames(self.walk_sheet, 4)

        # Scale frames
        self.idle_frames = [
            pygame.transform.scale(frame, (105, 105))
            for frame in self.idle_frames
        ]

        self.walk_frames = [
            pygame.transform.scale(frame, (105, 105))
            for frame in self.walk_frames
        ]

        # Flip frames
        self.idle_left = [pygame.transform.flip(f, True, False) for f in self.idle_frames]
        self.walk_left = [pygame.transform.flip(f, True, False) for f in self.walk_frames]

        self.idle_right = self.idle_frames
        self.walk_right = self.walk_frames

        # State
        self.facing_right = True
        self.walking = False

        # Animation
        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.25

        # Image + rect
        self.image = self.idle_right[0]
        self.rect = self.image.get_rect(center=(x, y))

    def load_frames(self, sheet, num_frames):
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface(
                (i * self.frame_width, 0, self.frame_width, self.frame_height)
            ).copy()
            frames.append(frame)
        return frames

    def update(self, keys, dt):
        
        # Movement
        if keys[pygame.K_a]:
            self.rect.x -= 10
            self.facing_right = True
            self.walking = True
        if keys[pygame.K_d]:
            self.rect.x += 10
            self.facing_right = False
            self.walking = True
        if keys[pygame.K_w]:
            self.rect.y -= 10
        if keys[pygame.K_s]:
            self.rect.y += 10

        # Animation timer
        self.animation_timer += dt / 1000
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_index += 1

        # Choose animation set
        if self.walking:
            frames = self.walk_right if self.facing_right else self.walk_left
        else:
            frames = self.idle_right if self.facing_right else self.idle_left

        self.animation_index %= len(frames)
        self.image = frames[self.animation_index]


        # Keep on screen
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())

