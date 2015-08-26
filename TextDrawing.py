'''
Created on 25.08.2015

@author: BlaXun
'''

import Superclasses
import pygame
from pygame.locals import *

class SingleLineTextRenderer(Superclasses.Renderable) : 

    targetSurface = None
    visible = True
    font = None
    fontSize = 10
    fontName = None
    text = None
    textSurface = None
    textColor = (0,0,0)
    textCoords = (0,0)
    drawOutlines = False
    outlineColor = (0,0,0)
    outlineSurface = None
    __outlineDistance = 1
    enableAntialiasing = False

    def __init__(self, targetSurface, fontName, fontSize, textColor):
        self.targetSurface = targetSurface
        self.fontName = fontName
        self.fontSize = fontSize
        self.font = pygame.font.Font('ressources/fonts/' + fontName, fontSize)
        self.textColor = textColor
        
    def onRender(self):
        if (self.visible == True and self.textSurface != None and self.targetSurface != None):
            
            if (self.drawOutlines):
                self.targetSurface.blit(self.outlineSurface,(self.textCoords[0]-self.__outlineDistance,self.textCoords[1])) #    Left
                self.targetSurface.blit(self.outlineSurface,(self.textCoords[0],self.textCoords[1]-self.__outlineDistance)) #    Top
                self.targetSurface.blit(self.outlineSurface,(self.textCoords[0]+self.__outlineDistance,self.textCoords[1])) #    Right
                self.targetSurface.blit(self.outlineSurface,(self.textCoords[0],self.textCoords[1]+self.__outlineDistance)) #    Bottom
             
            self.targetSurface.blit(self.textSurface,self.textCoords)

    def setText(self,text):
        
        if (self.text != text):
            self.text = text
            self.textSurface = self.font.render(text,self.enableAntialiasing,self.textColor)
            
            if (self.drawOutlines):
                self.outlineSurface = self.font.render(text, self.enableAntialiasing, self.outlineColor)             

    def setTextCoords(self, textCoords):
        
            if (self.textCoords != textCoords):
                    self.textCoords = textCoords