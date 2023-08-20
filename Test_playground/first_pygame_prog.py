import pygame

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT,
    KEYDOWN,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

while running:
    #look at every event in the queue
    for event in pygame.event.get():
        #check if user pressed a key
        if(event.type == KEYDOWN):
            #check if pressed key is the escpae key
            if(event.key == K_ESCAPE):
                running = False
        
        elif(event.type == QUIT):
                running = False
        #fill the entire screen white,the screen is a surface                
        screen.fill((255,255,255)) 
        
        surf = pygame.Surface((100,100))
        surf.fill((0,0,0))
        rect = surf.get_rect()
        surf_center = (

        (SCREEN_WIDTH-surf.get_width())/2,

        (SCREEN_HEIGHT-surf.get_height())/2

        )
        screen.blit(surf,surf_center)
        pygame.display.flip()
        
        

                
        
        

