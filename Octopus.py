#This is the octopus module and it contains the octopus class.
import pygame
import math
import utils


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
        
        #Movement
        self.angle = 0
        self.turnrate = [40, 40]
        self.turnpenalty = [1, 1]
        
        self.speed = [1,1]
        self.acceleration = 15
        self.maxspeed = 200
        self.minspeed = 1

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
        
        
        
    def update(self, direction, move, deltatime):
        
        if direction != '':
            
            self.turn(direction, deltatime)
        
        elif move: #If turned don't accelerate
            
            self.accelerate(deltatime)
        
        if move: #If move, move   
            self.move(deltatime)
            
        else:
            #If they haven't moved reduce their speed
            self.speed[0] = utils.chkmin(self.speed[0], -((self.acceleration*deltatime)/5), self.minspeed)
        #DEBUG
        print
        print 'DELTA TIME:' + str(deltatime)  
        print 'ANGLE ' + str(self.angle)
        print 'SPEED' + str(self.speed)
        
    def draw(self):

        pass #Needs to be written.
        