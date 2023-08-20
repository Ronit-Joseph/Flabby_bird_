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

SCREEN_WIDTH = 868
SCREEN_HEIGHT = 936

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flabby bird")

running = True
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')

screen.blit(bg,(0,0))
screen.blit(ground_img,(0,768))

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
          
    
    pygame.display.flip() 

                
        
        

