#This is a rewrite of Octopi ocean
import pygame
import random
import Octopus


__version__ = '2.0.0'

clock = pygame.time.Clock()
display = pygame.display.set_mode((1280,720))
backdrop = pygame.image.load('Backdrop.png').convert()
    

player = Octopus.octopus()

#Game loop
while True:
    
    display.blit(backdrop, (0,0))
    
    move = False
    direction = ''
    
    deltatime = clock.tick(60)
    deltatime = float(deltatime) / 100
    
    #Lag generation!!!! For testing le delta time
    #for i in range(1,100000):
        
        #random.randrange(1,100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    '''
    This bit needs revising
    and intergrating into octopus
    just the keypress should be fed into octopus.
    '''
    keypressed = pygame.key.get_pressed()
    
    player.update(keypressed, deltatime, display)
    
    
    
  
    
    pygame.display.flip()
    
    #Need to make a DEBUG info function to call here.
    print 'FPS: ' + str(clock.get_fps())        
