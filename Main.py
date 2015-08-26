import os, sys

import GFX
import TextDrawing
import GUI
import Superclasses

# Need MethodType for dynamic method-binding (e.g Buttons)
from types import MethodType

import pygame
from pygame.locals import *
from cgi import log

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
   
class App:      

        currentBackground = None
        screen = pygame.display.set_mode((320,240))
        guiRenderables = None
        otherRenderables = None
        
        rockman = None
        
        def __init__(self):
            self._running = True
            self._display_surf = None
            self.size = self.weight, self.height = 320, 240
            self.exitButton = None

            self.otherRenderables = []
            self.guiRenderables = []
            
            self.rockman = pygame.image.load('ressources/sprites/navis/rockman/idle.png')

        def exitButtonPressed(self):
            print("test")
            
        def onInit(self):
            
            pygame.init()
            pygame.display.set_caption("P.E.T")                

            self._display_surf = pygame.display.set_mode(self.size, pygame.DOUBLEBUF | pygame.HWSURFACE)
            #self._display_surf = pygame.display.set_mode(self.size, pygame.FULLSCREEN)

            self.currentBackground = GFX.Background(self._display_surf, 'ressources/backgrounds/bg01.png',[0,0])
            self.loadGUI()
                
            self._running = True
            
            self.exitButton = GUI.Button('button.png',[0,0])
            self.exitButton.onPress = self.exitButtonPressed        
            
        def onEvent(self, event):
            
            if event.type == pygame.QUIT:
                self._running = False
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == K_ESCAPE:
                    pygame.quit()
                    
        def onLoop(self):
            pass

        ''' Process all rendering operations '''
        def onRender(self):
            self.currentBackground.onRender()
            self.screen.blit(self.rockman,(20,self.height - self.rockman.get_rect().height))
            
            
            for renderable in self.otherRenderables:
                renderable.onRender()
                        
            for renderable in self.guiRenderables:
                renderable.onRender()
                
            if (self.exitButton):
                self.exitButton.onRender(self._display_surf)
            
            pygame.display.flip()

        ''' Cleaning up before quitting the application '''
        def onCleanup(self):
            pygame.quit()

        ''' Lifecycle '''
        def onExecute(self):
            
            if self.onInit() == False:
                self._running = False

            clock = pygame.time.Clock()
            
            #    Process the main-loop
            while (self._running):
                
                #    Lock the game to 30 FPS
                clock.tick(30)
                
                for event in pygame.event.get():
                    self.onEvent(event)

                    if (self.exitButton):
                        self.exitButton.onEvent(event)
                
                self.onLoop()
                self.onRender()
                
                #DEBUG - Print FPS
                print(clock.get_fps())
                    
            self.onCleanup()
                
        def loadGUI(self):
            #Load the Clock
            guiClock = GUI.Clock(self._display_surf)
            guiClock.x = 32
            guiClock.y = 44
                
            self.guiRenderables.append(guiClock)

if __name__ == "__main__" :
        theApp = App()
        theApp.onExecute()
