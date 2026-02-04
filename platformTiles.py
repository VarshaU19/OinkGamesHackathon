import pygame
# --------------------
# LEVEL MAP
# --------------------
level_map = [
    ".........",
    ".........",
    ".........",
    "##.#..#..",
    ".#.##..#.",
    "#.#..#.##",
    ".#.#..#..",
]
MAP_WIDTH = 800
MAP_HEIGHT = 400
# build tiles
class platformClouds(pygame.sprite.Sprite):
    def __init__(self, x, y, sheet):
        super().__init__()

        self.frames = self.load_frames(sheet)

        self.animation_index = 0
        self.animation_speed = 0.3
        self.animation_timer = 0

        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.hit = self.rect.inflate(-10, -70)        

    def load_frames(self, sheet):
        frames = []

        frame_width = 100
        frame_height = 75

        sheet_width, sheet_height = sheet.get_size()
        num_frames = sheet_width // frame_width

        for i in range(num_frames):
            frame = sheet.subsurface(
                (i * frame_width, 0, frame_width, frame_height)
            ).copy()
            frames.append(frame)

        return frames

    def update(self, dt):
        self.animation_timer += dt / 1000
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_index = (self.animation_index + 1) % len(self.frames)
            self.image = self.frames[self.animation_index]

    tile_size = 100

    MAP_WIDTH = len(level_map[0])
    MAP_HEIGHT = len(level_map)

def create_tile_map(sheet, tile_size):
    tile_group = pygame.sprite.Group()
    sheet = pygame.image.load(sheet).convert_alpha()

    for row_index, row in enumerate(level_map):
        for col_index, tile in enumerate(row):
            if tile == "#":
                x = col_index * tile_size
                y = row_index * tile_size
                tile_group.add(platformClouds(x, y, sheet))

    return tile_group
