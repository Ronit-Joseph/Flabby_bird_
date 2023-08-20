import pygame
from pygame.locals import *

# from pygame.locals import(
#     K_UP,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_ESCAPE,
#     QUIT,
#     KEYDOWN,
# )

pygame.init()

clock = pygame.time.Clock()
fps = 60


SCREEN_WIDTH = 868
SCREEN_HEIGHT = 936

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flabby bird")

#defining game variables

ground_scroll = 0
scroll_speed = 4


running = True
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)      
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img =  pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    
    def update(self):
        self.counter+=1
        flap_cooldown = 5
        
        if self.counter >flap_cooldown:
            self.counter = 0
            self.index += 1
            if(self.index >= len(self.images)):
                self.index = 0
        self.image = self.images[self.index]
        
        
bird_group = pygame.sprite.Group()

flappy = Bird(100,int(SCREEN_HEIGHT/2))

bird_group.add(flappy)


while running:
    
    
    clock.tick(fps)
    #drawing the background
    screen.blit(bg,(0,0))
    #adding the bird sprite in
    bird_group.draw(screen)
    #adding animation to the bird,basically going through various indexes of diff images 
    bird_group.update()
    #dmoving teh ground
    screen.blit(ground_img,(ground_scroll,768))
    ground_scroll -= 4
    if(abs(ground_scroll) >35):
        ground_scroll = 0
        
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

                
        
        

