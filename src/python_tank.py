import pygame
import os
import game_main as game

# define a main function
def main():
    # get path for loading resource from main file
    dir_path = os.path.dirname(os.path.realpath(__file__))

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
    
    # main loop
    game.init()
    
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                running = game.process(event)
    
    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()