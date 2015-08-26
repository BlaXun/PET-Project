'''
Created on 25.08.2015

@author: BlaXun
'''

import Superclasses

import pygame
from pygame.locals import *

class Background(pygame.sprite.Sprite, Superclasses.Renderable):

        targetSurface = None
        image = None
        rect = None
        
        def __init__(self, targetSurface, image_file, location):
            pygame.sprite.Sprite.__init__(self) #call Sprite initializer
            self.targetSurface = targetSurface
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
            
        def onRender(self):
            self.targetSurface.blit(self.image,self.rect)