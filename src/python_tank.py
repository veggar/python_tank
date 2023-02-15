import sys
import signal
import os

import pygame
import game_main as game
from .display import display

# define a main function
def main():
    # get path for loading resource from main file
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Check if running on pi
    from display.pygamePixelDisplay import PygamePixelDisplay
    display = PygamePixelDisplay(caption="PiTable Emulator",
                                    gridSize=[16, 16],
                                    width=1000,
                                    height=1000,
                                    space=2)
        
    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    logo = pygame.image.load(dir_path+"/../resource/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("pytank")
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((480,320))
    
    # define a variable to control the main loop
    running = True
    
    # for initialize
    game.init()

    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                running = game.process(event)
    
    # for exit
    display.fill([0, 0, 0])
    display.show()

    # Quit game and close window
    game.quit()
    pygame.quit()
    sys.exit(0)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()