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
flying = False
game_over = False

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
        self.vel = 0
        self.clicked = False
    #the update func controles the animation aand movement
    def update(self):
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8                    #basically adding gravity
            if self.rect.bottom <768:
                self.rect.y += int(self.vel)     #adding falling capabilty for bird
        if game_over == False:   
            #adding jumping abilty for bird
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:    #checks for left click of mouse therfore index [0]
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:                     #checks if mouse is not clicked,or its released 
                self.clicked = False
            self.counter+=1
            flap_cooldown = 5
            
            if self.counter >flap_cooldown:
                self.counter = 0
                self.index += 1
                if(self.index >= len(self.images)):
                    self.index = 0
            self.image = self.images[self.index]
            
            #rotate bird
            self.image = pygame.transform.rotate(self.images[self.index],self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)
            
class pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100,int(SCREEN_HEIGHT/2))

bird_group.add(flappy)

btm_pipe = pipe(300,int(SCREEN_HEIGHT/2))
pipe_group.add(btm_pipe)


while running:
    
    
    clock.tick(fps)
    #drawing the background
    screen.blit(bg,(0,0))
    #adding the bird sprite in
    bird_group.draw(screen)
    #adding animation to the bird,basically going through various indexes of diff images 
    bird_group.update()
    
    pipe_group.draw(screen)
    pipe_group.update()
    
    
    #dmoving teh ground
    screen.blit(ground_img,(ground_scroll,768))
    
    #check if bird touched ground ,as to end the game
    if flappy.rect.bottom > 768:
        game_over = True
        flying = False
        
    if game_over == False:
        ground_scroll -= scroll_speed
        if(abs(ground_scroll) >35):
            ground_scroll = 0
        
    #look at every event in the queue
    for event in pygame.event.get():
        #check if user pressed a key
        if(event.type == KEYDOWN):
            #check if pressed key is the escpae key
            if(event.key == K_ESCAPE):
                running = False
        if(event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False):
            flying = True
        elif(event.type == QUIT):
                running = False
          
    
    pygame.display.flip() 

                
        
        

