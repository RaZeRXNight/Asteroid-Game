import pygame;
from constants import *;

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets the pygame's screen width and height.
    
    Game_State = True # Control Variable
    
    while Game_State:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
        
        screen.fill("black") # Fills the background with the color black.
        pygame.display.flip() # Refreshes the Screen
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()