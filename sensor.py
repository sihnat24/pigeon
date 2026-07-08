import math
import pygame
import config


def cast_rays(drone_x, drone_y, heading, obstacles):
    """
    Cast rays within the FOV cone from the drone's position.
    Returns a list of dicts: {angle_deg, distance, hit}
    - angle_deg: absolute angle of the ray
    - distance: how far the ray travelled before hitting (FOV_RANGE if no hit)
    - hit: True if the ray struck an obstacle
    """
    fov_half = config.FOV_ANGLE / 2
    results = []

    for i in range(config.RAY_COUNT):
        angle_deg = heading - fov_half + (config.FOV_ANGLE * i / (config.RAY_COUNT - 1))
        angle_rad = math.radians(angle_deg)

        dx = math.sin(angle_rad)
        dy = -math.cos(angle_rad)  # negative because y increases downward in pygame

        min_dist = config.FOV_RANGE
        hit = False

        for (ox, oy, ow, oh) in obstacles:
            dist = _ray_rect_intersect(drone_x, drone_y, dx, dy, ox, oy, ow, oh)
            if dist is not None and dist < min_dist:
                min_dist = dist
                hit = True

        results.append({
            "angle_deg": angle_deg,
            "distance": min_dist,
            "hit": hit
        })

    return results


def _ray_rect_intersect(rx, ry, dx, dy, ox, oy, ow, oh):
    """
    Slab method ray-AABB intersection.
    Returns distance to hit, or None if no intersection within FOV_RANGE.
    rx, ry: ray origin
    dx, dy: ray direction (unit vector)
    ox, oy, ow, oh: obstacle rect (x, y, width, height) in meters
    """
    t_min = 0.0
    t_max = config.FOV_RANGE

    # X slabs
    if dx != 0:
        tx1 = (ox - rx) / dx
        tx2 = (ox + ow - rx) / dx
        t_min = max(t_min, min(tx1, tx2))
        t_max = min(t_max, max(tx1, tx2))
    else:
        if rx < ox or rx > ox + ow:
            return None

    # Y slabs
    if dy != 0:
        ty1 = (oy - ry) / dy
        ty2 = (oy + oh - ry) / dy
        t_min = max(t_min, min(ty1, ty2))
        t_max = min(t_max, max(ty1, ty2))
    else:
        if ry < oy or ry > oy + oh:
            return None

    if t_max >= t_min and t_min >= 0:
        return t_min

    return None


def draw_pov(surface, rays):
    """
    Draw the drone's-eye POV panel on the right half of the window.
    Each ray becomes a vertical bar — taller and brighter means closer.
    """
    panel_x = config.WORLD_W * config.SCALE  # left edge of right panel
    panel_w = config.WORLD_W * config.SCALE
    panel_h = config.WORLD_H * config.SCALE

    # black background for POV panel
    pygame.draw.rect(surface, (0, 0, 0), (panel_x, 0, panel_w, panel_h))

    bar_w = panel_w / len(rays)

    for i, ray in enumerate(rays):
        if ray["hit"]:
            
            ratio = 1.0 - (ray["distance"] / config.FOV_RANGE)
            bar_h = int(ratio * panel_h)
            brightness = int(55 + 200 * ratio)
            color = (brightness, brightness, brightness)

            x = int(panel_x + i * bar_w)
            y = int((panel_h - bar_h) / 2)
            pygame.draw.rect(surface, color, (x, y, max(1, int(bar_w)), bar_h))
