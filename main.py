#This is a rewrite of Octopi ocean
import pygame
import random
import Octopus
import Powerup
__version__ = '2.0.0'

pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()
pygame.mixer.init() #Init the music package so that we can use it


clock = pygame.time.Clock()
display = pygame.display.set_mode((1280,720))
backdrop = pygame.image.load('Assets/Art/Backdrop.png').convert()
    

player = Octopus.octopus()

InkPots = Powerup.InkPots(player)
Coins = Powerup.Coins(player)

def loadandplaymusic():
    
    pygame.mixer.music.load('Assets/Sounds/Main game music.ogg')
    pygame.mixer.music.play(-1, 0) 

def updatepowerups():
    
    InkPots.update(display)
    Coins.update(display)
loadandplaymusic()
#Game loop
while True:
    
    display.blit(backdrop, (0,0))
    
    #===========================================================================
    # DELTA TIME STUFF
    #===========================================================================
    deltatime = clock.tick(60)
    deltatime = float(deltatime) / 100
    
    #===========================================================================
    # LAG GENERATION
    #===========================================================================
    #Lag generation!!!! For testing le delta time
    #for i in range(1,100000):
        
        #random.randrange(1,100)
    
    #===========================================================================
    # EVENT COLLECTION
    #===========================================================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    keypressed = pygame.key.get_pressed()
    
    #===========================================================================
    # UPDATES
    #===========================================================================
    player.update(keypressed, deltatime, display)
    
    updatepowerups()

    
    pygame.display.flip()
    
    #Need to make a DEBUG info function to call here.
    print 'FPS: ' + str(clock.get_fps())        
