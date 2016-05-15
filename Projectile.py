#===============================================================================
# This is the projectile module. It contains most of the classes to do with
# projectiles.
#===============================================================================

import pygame 
import math
#parent projectile class
pygame.init()
#===============================================================================
# PARENT PROJECTILE
#===============================================================================
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
        
        if any([self.rect.x > 1280, #If the projectile goes off screen,
               self.rect.y > 720,  # Kill it!!!!
               self.rect.x < 0, 
               self.rect.y < 0]):
            self.kill()
        else:
            
            self.move(deltatime)
            self.draw(display)
        
        pass
    
    def move(self, deltatime):
        
        radians = math.radians(self.angle + 90) #Changing the angle to radians because that is what python uses. Adding 90 to offset it correctly.
        
        self.rect.x += math.cos(radians) * self.speed * deltatime
        self.rect.y -= math.sin(radians) * self.speed * deltatime
        
    def draw(self, display):
        
        display.blit(self.sprite, (self.rect.x, self.rect.y))

class InkJet(projectile): #INKJET PROJECTILE
    
    def __init__(self, firer):
        
        projectile.__init__(self, 
                            firer.rect.center, 
                            firer.angle, 
                            (firer.speed[0] * 1.5) + 20, 
                            pygame.image.load('defaultProjectile.png'))
        
