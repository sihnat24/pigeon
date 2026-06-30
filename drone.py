import config
import pygame

class Drone2D:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.heading = 0 #angle in degrees
        self.drag = 0.9
    
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.vx *= self.drag
        self.vy *= self.drag

    def apply_force(self, dx, dy):
        self.vx += dx
        self.vy += dy
    
    def draw(self, surface):
        px = int(self.x * config.SCALE)
        py = int(self.y * config.SCALE)
        pygame.draw.circle(surface, config.COLOR_DRONE, (px,py),3)
        