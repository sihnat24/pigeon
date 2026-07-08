import pygame
import config

# Obstacles: (x, y, width, height) in meters
OBSTACLES = [
    # Outer walls
    (0,    0,    40,  1),    # top
    (0,    29,   40,  1),    # bottom
    (0,    0,    1,   30),   # left
    (39,   0,    1,   30),   # right

    # Internal structure — creates corridors, not open world
    (5,    5,    8,   2),
    (3,    15,   10,  4),
    (5,    5,    2,   10),
    (15,   3,    2,   12),
    (10, 23, 6, 6),
    (25,   15,   10,  2),
    (28,   5,    2,   10),
    (10,   20,   15,  2),
    (30,   20,   2,   8),
]

TARGET = (25,28)

class RectangleWorld:

    def __init__(self):
        self.obstacles = OBSTACLES
        self.target = TARGET

    
    def draw(self, surface: pygame.Surface) -> None:
        
        #draw rectangle obstacles
        for (x,y,w,h) in self.obstacles:
            rect = pygame.Rect(x * config.SCALE,
                               y * config.SCALE,
                               w * config.SCALE,
                               h * config.SCALE)
            
            pygame.draw.rect(surface, config.COLOR_OBSTACLE, rect)

            #draw the target
            tx = int(self.target[0] * config.SCALE)
            ty = int(self.target[1] * config.SCALE)
            pygame.draw.circle(surface, config.COLOR_TARGET, (tx, ty), 6)