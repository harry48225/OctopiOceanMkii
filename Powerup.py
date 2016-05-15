#===============================================================================
# This is the powerup module it contains most of the power up classes
#===============================================================================

import pygame
from random import randrange

pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()
pygame.mixer.init()

#===============================================================================
# PARENT POWERUP CLASS
#===============================================================================



class powerup(pygame.sprite.Sprite):
    
    def __init__(self, sprite, player):
        
        pygame.sprite.Sprite.__init__(self) #init the pygame class
        
        #Sprite and hit box
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        
        self.player = player
        
    def detectcollision(self):
        
        if self.rect.colliderect(self.player.rect):
            
            return True
        
        return False
   
    def draw(self, display):
        
        display.blit(self.sprite, (self.rect.x, self.rect.y))

class InkPot(powerup):  #INKPOT POWERUP
    
    def __init__(self, player):
        
        sprite = pygame.image.load('INKpot.png')
        powerup.__init__(self, sprite, player)
        
        self.InkFillAmount = 10
        
        self.rect.x, self.rect.y = randrange(100, 1180), randrange(100, 620)
    
    def update(self, display):
        
        if self.detectcollision():
            
            self.player.inkamount += self.InkFillAmount
            self.kill()
            
        else:
            
            self.draw(display)

class InkPots(pygame.sprite.Group): #INKPOT GROUP
    
    def __init__(self, player):
        
        pygame.sprite.Group.__init__(self)
        self.player = player
        
        self.add(InkPot(self.player))
        
        self.collectInkSound = pygame.mixer.Sound('Collect INK.ogg')
        
    def update(self, display):
        
        pygame.sprite.Group.update(self, display)
        
        if len(self) == 0: #No ink pots in the list so add one
            
            #Since one must have been collected, play the collection sound
            self.collectInkSound.play()
            self.add(InkPot(self.player))
        
class Coin(powerup):

 
    def __init__(self, player):
        
        sprite = pygame.image.load('coin.png')
        powerup.__init__(self, sprite, player)
        
        self.scoreincrease = 10
        self.rect.x, self.rect.y = randrange(100, 1180), randrange(100, 620)
    
    def update(self, display):
        
        if self.detectcollision():
        
            self.player.score += self.scoreincrease
            self.kill()
        

        else:
            
            self.draw(display)
        
class Coins(pygame.sprite.Group):
    
    def __init__(self, player):
        
        pygame.sprite.Group.__init__(self)
        self.player = player
        
        self.collectCoinSound = pygame.mixer.Sound('Collect coin.ogg')
        
        self.coinamount = 1
        
        for i in range(self.coinamount):
            
            self.add(Coin(self.player))
            
    def update(self, display):
        
        pygame.sprite.Group.update(self, display)
        
        if len(self) < self.coinamount: #There are no coins in the list to make a new one
            
            #One must have been collected so play the sound!
            self.collectCoinSound.play()
            
            self.add(Coin(self.player))        
                    
    
    