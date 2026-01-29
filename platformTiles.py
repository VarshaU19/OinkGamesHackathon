import pygame

# --------------------
# LEVEL MAP
# --------------------
level_map = [
    "...................",
    "...................",
    "...................",
    "#####.....###..##..",
    "...................",
    "...###..###.....###",
    "...................",
    "#####.....#######..",
]

MAP_WIDTH = len(level_map[0])
MAP_HEIGHT = len(level_map)

# --------------------
# ANIMATED PLATFORM TILE
# --------------------
import pygame

class PlatformTile(pygame.sprite.Sprite):
    def __init__(self, x, y, sheet, tile_size, scale_factor=2.5): 
        ''' parameters: 
                x, y = where the tile goes on the screen
                sheet = spritesheet
                scale_factor = how much bigger we want the tile_size
        '''
        super().__init__() #turn on sprite 

        self.scale_factor = scale_factor

        # cut spritesheet into frames
        self.frames = self.load_frames(sheet) 

        # Scale frames to be bigger
        # int(tile_size * scale_factor) = width, int(tile_size * scale_factor) = height
        self.frames =[
            pygame.transform.scale(
                frame, (int(tile_size * scale_factor), int(tile_size * scale_factor)))
                for frame in self.frames
        ]

        self.animation_speed = 0.3 
        self.animation_index = 0 # keep track of frame being shown
        self.animation_timer = 0 # keep track of when to change frame

        self.image = self.frames[0] #start tiles with first frame
        self.rect = self.image.get_rect(topleft=(x, y)) # creates invisible box around image; used to detect collisions, locate tile, draw image

    def load_frames(self, sheet):
        frames = []
        sheet_width, sheet_height = sheet.get_size() # ask for sheet size

        frame_width = 100 # set width to frame size 
        frame_height = 100 #set height to frame size

        num_frames = sheet_width // frame_width # figure out how many frames fit across the picture

        # loop for each animation frame
        for i in range(num_frames): 
            # cuts out one small picture from spritesheet
            # i * frame_width = moves to right in spritesheet to next frame
            frame = sheet.subsurface((i * frame_width, 0, frame_width, frame_height)).copy()
            # saves picture/frame into list
            frames.append(frame)
        return frames

    #runs every frame of the game
    def update(self, dt):
        # add time to the stopwatch
        #dt / 1000 = how much time has passed divided by 100 seconds
        self.animation_timer += dt / 1000
        # if enough time has passed...
        if self.animation_timer >= self.animation_speed:
            # reset stopwatch
            self.animation_timer = 0
            # move to next animation picture 
            # % = go back to the start of spritesheet if we reached the end
            self.animation_index = (self.animation_index + 1) % len(self.frames)
            # show picture on screen
            self.image = self.frames[self.animation_index]


# Create Map
# function to build all tiles in platforms
''' parameters:
        screen_size = how big the game window is 
        tile_shhet_path = where tile spritesheet is saved
        scale_factor = how much bigger to make the tiles
'''
def create_tile_map(screen_size, tile_sheet_path, scale_factor=2):

    '''split screen size into 
        1) how wide the screen is 
        2) how tall the screen is
    '''
    screen_width, screen_height = screen_size

    # base tile size (fit to screen)
    # how big can each tile be so the whole map fits on the screen
    '''MAP_WIDTH = how many tiles wide the map is
       MAP_HEIGHT = How many tiles tall the map is 
       min(...) = picks the smaller size so nothing goes off screen
    '''
    tile_size = min(
        screen_width / MAP_WIDTH,
        screen_height / MAP_HEIGHT
    )

    # final tile size after scaling
    # make the tiles as big as the scaling; this is the real size used for drawing and spacing
    final_size = tile_size * scale_factor

    # center the map
    offset_x = (screen_width - MAP_WIDTH * final_size) / 2 # this moves the map left or right so its centered + finds empty space and splits it in half
    offset_y = (screen_height - MAP_HEIGHT * final_size) / 2 # this moves the map up or down so its centered + finds empty space and splits it in half

    # Box to hold all platform tiles
    '''Makes it easy to:
        draw them
        update them
        check collisions
    '''
    tile_group = pygame.sprite.Group()
    # loads the tile image from your computer
    # convert_alpha() = keeps transparency (no ugly boxes)
    tile_sheet = pygame.image.load(tile_sheet_path).convert_alpha()

    # loop to go through map by row
    # row_index = which row we're on
    for row_index, row in enumerate(level_map):
        # go through each letter in the row
        # col_index = which column we're in
        # tile = the character (. or #)
        for col_index, tile in enumerate(row):
            # '#' = put a platform here
            # '.' = empty space
            if tile == "#":
                # decides left/right position
                # col_index * final_size = space tiles evenly
                # offset_x = keeps everything centered
                x = offset_x + col_index * final_size
                # decides up/down position
                # row_index * final_size = space tiles evenly
                # offset_y = keeps everything centered
                y = offset_y + row_index * final_size
                # Make a new platform tile
                # put it in the group
                # Draw and animate it
                tile_group.add(PlatformTile(x, y, tile_sheet, tile_size, scale_factor))
    ''' Give back: 
            all platform tiles
            final tile size (used for collisions, player size, etc.)
    '''
    return tile_group, final_size

