#===============================================================================
# This is the projectile module. It contains all of the classed to do with
# projectiles.
#===============================================================================

import pygame 
import math
#parent projectile class


class projectile(pygame.sprite.Sprite):
    
    def __init__(self, firercenter, angle, speed, sprite):
        
        pygame.sprite.Sprite.__init__(self)
        
        #Sprite and hit box
        self.sprite = sprite
        self.sprite = pygame.transform.rotate(self.sprite, angle - 90)
        self.rect = self.sprite.get_rect()
        self.rect.center = firercenter
        
        #Attributes
        self.speed = speed * 1.2
        self.angle = angle

        
    def update(self, deltatime, display):
        
        self.move(deltatime)
        self.draw(display)
        
        pass
    
    def move(self, deltatime):
        
        radians = math.radians(self.angle + 90) #Changing the angle to radians because that is what python uses. Adding 90 to offset it correctly.
        
        self.rect.x += math.cos(radians) * self.speed * deltatime
        self.rect.y -= math.sin(radians) * self.speed * deltatime
        
    def draw(self, display):
        
        display.blit(self.sprite, (self.rect.x, self.rect.y))
    
        
        
        
        