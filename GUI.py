'''
Created on 25.08.2015

@author: BlaXun
'''

import os, sys
import Superclasses
import datetime

import pygame
from pygame.locals import *
import TextDrawing

'''    Shows the current time     '''
class Clock(Superclasses.Renderable):
    
    singleLineTextRenderer = None
    x = 0
    y = 0
    timeFormat = ''
    
    def __init__(self, targetSurface, timeFormat='%d.%m.%Y - %H:%M:%S'):
        self.singleLineTextRenderer = TextDrawing.SingleLineTextRenderer(targetSurface, 'emulogic.ttf', 8, (255,255,255))
        self.singleLineTextRenderer.enableAntialiasing = False
        self.singleLineTextRenderer.drawOutlines = True
        self.timeFormat = timeFormat
        
    def onRender(self):
        self.singleLineTextRenderer.setText(datetime.datetime.strftime(datetime.datetime.now(), self.timeFormat))
        self.singleLineTextRenderer.onRender()
        self.singleLineTextRenderer.textCoords = (self.x,self.y)
    
''' Button class to react to clicks '''
class Button(Superclasses.Renderable):

        def __init__(self,image_file,location):
            
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
            self.pressed = False
                
        def onEvent(self, event):
            
            if (event.type == pygame.MOUSEBUTTONUP):
                print("mouse up")
                pos = pygame.mouse.get_pos()
                print(pos)
                print(self.rect)
                
                if (self.rect.collidepoint(pos)):
                    self.onPress()

        def onPress(self):
            raise NotImplementedError( "onPress was not implemented on a Button")

        def onRender(self, surface):
            surface.blit(self.image, [320-(self.rect.width+8),240-(self.rect.height+8)])