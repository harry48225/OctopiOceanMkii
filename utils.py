#This contains odd functions that are used sometimes
import pygame



def changeangle(originalangle, amountofchange): #This is an angle function to calculate the change in angle. It handles going above 360 and below 0
    #Change the originalangle
    newangle = originalangle + amountofchange
    
    #If we've gone above 360 go to the 0 angles so we minus 360
    if newangle > 360:
        
        newangle -= 360
    #If we go below 360 we need to subtract from 360 so we add 360     
    if newangle < 0:
        
        newangle += 360
    #Return the result    
    return newangle
    


def chkmin(value, change, minimum): #This is for making sure that stuff doesn't go below the minimum
    #Apply the change in value
    newvalue = value + change
    
    #Check if it is below the minimum
    if newvalue < minimum:
        #Make it the minimum
        newvalue = minimum
        
        
    #return it
    return newvalue
    
def rotatesprite(sprite, angle): #Rotate a sprite keeping the center
    newsprite = sprite
    oldrect = sprite.get_rect()
    rotatedsprite = pygame.transform.rotate(newsprite, angle)
    rotatedrect = (oldrect.copy())
    rotatedrect.center = rotatedsprite.get_rect().center
    newsprite = rotatedsprite.subsurface(rotatedrect).copy()
    return newsprite
