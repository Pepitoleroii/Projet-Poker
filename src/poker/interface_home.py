import pygame as pg
from pygame.locals import *

from interface_elements import *
        
class GUI_homepage:
    def __init__(self):
        pg.init()
        #create the window :
        self.homepage = pg.display.set_mode([640, 480])
        pg.display.set_caption('Welcome to Centrale Poker')
        
        #background : https://www.casino-saint-julien.com/les-differents-types-de-poker/
        my_bg=pg.image.load('backgrounds/poker_background.jpg')
        self.bg = pg.transform.scale(my_bg, (640, 480))
        
        #create name entry box :
        self.input_name = InputBox(100, 400, 300, 32,
                                   text='name',
                                   centered=True)
        
        #create playstart button :
        self.play_button = Button(200, 150, 125, 50, text= "Jouer !")
        
    def mainloop(self):
        clock = pg.time.Clock()
        input_boxes = [self.input_name]
        input_buttons = [self.play_button]
        done = False

        while not done:
            self.homepage.blit(self.bg,(0,0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event)
                for button in input_buttons :
                    button.handle_event(event)
            
            for box in input_boxes:
                box.draw(self.homepage)
            for button in input_buttons : 
                button.draw(self.homepage)
                
            if self.play_button.CurrentState:
                self.play_button.CurrentState = False
                pg.quit()
                return "WAITING"
            pg.display.flip()
            clock.tick(30)
        pg.quit()
        return ""

