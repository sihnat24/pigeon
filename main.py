import config
import drone
import world
import pygame

def main():
    
    pygame.init()
    surface = pygame.display.set_mode((config.WINDOW_W, config.WINDOW_H))
    pygame.display.set_caption("drone course")
    clock = pygame.time.Clock()
    

    py_world = world.RectangleWorld()
    player = drone.Drone2D()

    #init prev pos vars
    prev_x = player.x
    prev_y = player.y 
    running = True
    while running:
        dt = clock.tick(config.FPS) / 1000
        for event in pygame.event.get(): #event queue, fires ONCE per key press
            if event.type == pygame.QUIT: #pressing x on the window
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        #apply force based on key presses
        keys = pygame.key.get_pressed() #gives a snapshot of all keys, so multiple keys held down will fire all fxns
        if keys[pygame.K_w]:
            player.apply_thrust(1,dt)
        if keys[pygame.K_s]:
            player.apply_thrust(-1,dt)
        if keys[pygame.K_a]:
            player.apply_strafe(1,dt)
        if keys[pygame.K_d]:
            player.apply_strafe(-1,dt)
        if keys[pygame.K_q]:
            player.rotate(1,dt)
        if keys[pygame.K_e]:
            player.rotate(-1,dt)
        
        #check obstacles for collision
        for (x,y,w,h) in world.OBSTACLES:
            if (player.x > x and player.x < x+ w) and (player.y > y and player.y < y+h): #if collision, set v to 0 and reset pos
                player.vx = 0
                player.vy = 0
                player.x = prev_x
                player.y = prev_y
        
        #update position 
        prev_x, prev_y = player.x, player.y #store prev position
        player.update(dt)
        
        #draw
        surface.fill(config.COLOR_BG) #clear the screen
        py_world.draw(surface) #draw world and player
        player.draw(surface) 

        pygame.display.flip() #push to screen


    #quit Pygame
    pygame.quit()




if __name__ == "__main__":
    main()