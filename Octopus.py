#This is the octopus module and it contains the octopus class.
import pygame
import math
import utils
import Projectile



class InkJet(Projectile.projectile):
    
    def __init__(self, firer):
        
        Projectile.projectile.__init__(self, firer.rect.center, firer.angle, firer.speed[0] + 20, pygame.image.load('defaultProjectile.png'))
        
        

class octopus(pygame.sprite.Sprite):
    
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        
        #Sprite and hit box
        self.sprite = self.defaultsprite = pygame.image.load('8pi1.png')
        self.rect = self.sprite.get_rect()
        
        #Gameplay
        self.health = 3
        self.inkamount = 10
        self.score = 0
        self.firerate = [0.2, 0.2] #seconds between each shot
        
        #Movement
        self.angle = 0
        self.turnrate = [40, 40]
        self.turnpenalty = [3, 3]
        
        self.speed = [1,1]
        self.acceleration = 15
        self.maxspeed = 200
        self.minspeed = 1
        
        #InkJets
        
        self.InkJets = pygame.sprite.Group()
               
    def turn(self, direction, deltatime): #Changing the angle and applying turn penalty. and rotating the sprite
        print direction
        
        self.turnrate[1] = float(self.turnrate[0] * deltatime) #Accounting for deltatime
        
        self.turnpenalty[1] = float(self.turnpenalty[0] * deltatime)
        
        #Turn right
        if direction == 'RIGHT':
            
            self.angle = utils.changeangle(self.angle, -(self.turnrate[1])) #This function handles going over 360 and below 0
        #Turn left    
        if direction == 'LEFT':
            
            self.angle = utils.changeangle(self.angle, +(self.turnrate[1]))
          
        self.angle = int(self.angle) 
        
      
        self.speed[0] = utils.chkmin(self.speed[0], -(self.turnpenalty[1] + self.speed[0]/200), self.minspeed) #This subtracts the middle value and ensure that it doesn't go below the minimum speed
        
        self.sprite = utils.rotatesprite(self.defaultsprite, self.angle)                     

    def accelerate(self, deltatime): #Purely adding to the speed
        
        
        #Acceleration logic     
        #Will accelerate at full speed up to the max speed
        if self.speed[0] < self.maxspeed:
            
            self.speed[0] += (self.acceleration * deltatime)
        #Past max speed it will accelerate at 1/10th of regular acceleration  
        else:
            
            self.speed[0] += ((self.acceleration * deltatime)/10)
            
    def move(self, deltatime): #Purely moving the octopus, and off screen logic        
       
        self.speed[1] = self.speed[0] * deltatime #Updating needed variable for Deltatime

            
        radians = math.radians(self.angle + 90)
        self.rect.x += math.cos(radians) * self.speed[1]
        self.rect.y -= math.sin(radians) * self.speed[1]
       
        #Moving off the screen logic
        if self.rect.x > 1280:
            
            self.rect.x -= 1280
            
        if self.rect.x < 0:
            
            self.rect.x += 1280
            
        if self.rect.y > 720:
            
            self.rect.y -= 720
    
        if self.rect.y < 0:
            
            self.rect.y +=720
            
    def update(self, keypressed, deltatime, display):
        
        
        #=======================================================================
        # TURNING DETECTION
        #=======================================================================
        if keypressed[pygame.K_a]: #A has been pressed so turn left
            
            direction = 'LEFT'
        
        elif keypressed[pygame.K_d]: #A has been pressed to turn right
            
            direction = 'RIGHT'
            
        else: #No turning has happened
            
            direction = ''
        
        #=======================================================================
        # MOVING DETECTION
        #=======================================================================
        if keypressed[pygame.K_w]: #W has been pressed so go forward
            
            move = True
        
        else: #W hasn't been pressed so don't move at all
            
            move = False
        
        #=======================================================================
        # APPLYING TURNING AND MOVEMENT
        #=======================================================================
        if direction != '':
            
            self.turn(direction, deltatime)
        
        elif move: #If turned don't accelerate
            
            self.accelerate(deltatime)
        
        if move: #If move, move   
            self.move(deltatime)
            
        else:
            #Kill their speed, pulling them Gs
            self.speed[0] = 0
        
        
        self.draw(display)
        
        #=======================================================================
        # CHECKING IF FIRED
        #=======================================================================
        
        self.firerate[1] -= deltatime / 10 #Deltatime is in seconds * 10, so we divide by 10 to get seconds
        
        if keypressed[pygame.K_SPACE] and self.firerate[1] <= 0 and self.speed[0] > 0:
            
            self.fire()
            self.firerate[1] = self.firerate[0]
        
        #=======================================================================
        # OTHER UPDATES
        #=======================================================================
        
        self.InkJets.update(deltatime, display)
        
        #DEBUG
        print
        print 'DELTA TIME:' + str(deltatime)  
        print 'ANGLE ' + str(self.angle)
        print 'SPEED' + str(self.speed)
        
    def draw(self, display):
        
        display.blit(self.sprite, (self.rect.x, self.rect.y))


        pass #Needs to be written.
        
    def fire(self):
        
        Ink = InkJet(self)
        self.InkJets.add(Ink)
        print self.InkJets.sprites()
        
        
