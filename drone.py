import config
import pygame
import math

#straoght up +y is forward, straight right +x is right

class Drone2D:

    def __init__(self):
        self.x = 4
        self.y = 4
        self.vx = 0
        self.vy = 0
        self.heading = 0 #angle in degrees
        self.drag = 0.9
 
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx *= self.drag
        self.vy *= self.drag

        #scale down drone speed if its going too fast
        speed = math.hypot(self.vx, self.vy) #magnitude of velocity vector
        if speed > config.DRONE_SPEED:
            scale = config.DRONE_SPEED / speed
            self.vx *= scale
            self.vy *= scale


    def apply_thrust(self, direction, dt):
        head = math.radians(self.heading)
        ax = direction * (config.DRONE_ACCEL * math.sin(head))
        ay = direction * (-1 * config.DRONE_ACCEL * math.cos(head))
        self.vx += dt * ax
        self.vy += dt * ay

    def apply_strafe(self, direction, dt):
        head = math.radians(self.heading)
        ax = direction * (config.DRONE_ACCEL * math.cos(head))
        ay = direction * (config.DRONE_ACCEL * math.sin(head))
        self.vx += dt * ax
        self.vy += dt * ay

    def rotate(self, direction, dt):
        self.heading += direction * config.ROTATION_SPEED * dt

    def draw(self, surface):
        head = math.radians(self.heading)
        px = int(self.x * config.SCALE)
        py = int(self.y * config.SCALE)
        pygame.draw.circle(surface, config.COLOR_DRONE, (px,py),5)
        
        #facing forward
        l= 15
        end_x = int(px + l * math.sin(head))
        end_y = int(py - l * math.cos(head))
        pygame.draw.line(surface, config.COLOR_DRONE, (px,py), (end_x, end_y), 2)

        #draw vision cone
        fov_half = config.FOV_ANGLE / 2
        points = [(px, py)]
        for i in range(31):  # 30 steps across the arc
            angle_deg = self.heading - fov_half + (config.FOV_ANGLE * i /30) 
            angle_rad = math.radians(angle_deg)
            cone_x = px + int(config.FOV_RANGE * config.SCALE * math.sin(angle_rad))
            cone_y = py - int(config.FOV_RANGE * config.SCALE * math.cos(angle_rad))
            points.append((cone_x, cone_y))

        pygame.draw.polygon(surface, config.COLOR_FOV, points, 1)  # 1 =

                            

        