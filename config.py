# World
WORLD_W = 40        # meters
WORLD_H = 30        # meters
SCALE   = 20        # pixels per meter

# Window
WINDOW_W = WORLD_W * SCALE   # 800px
WINDOW_H = WORLD_H * SCALE   # 600px
FPS      = 30

# Drone
DRONE_SPEED = 5.0   # m/s — push this as high as possible once stable
DRONE_ACCEL = 15.0 # constant 15 m/s^2 accel for noe
ROTATION_SPEED = 120

# Colors (R, G, B)
COLOR_BG       = (20,  20,  20)   # dark background
COLOR_OBSTACLE = (100, 100, 100)  # grey
COLOR_DRONE    = (255, 255,   0)  # yellow
COLOR_TARGET   = (255,  50,  50)  # red
COLOR_FOV      = (100, 200, 255)  # light blue
