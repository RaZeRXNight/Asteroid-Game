import pygame;
from constants import *;
from player import Player;
from asteroid import Asteroid;
from asteroidfield import AsteroidField;
from shot import Shot;

def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)); # Sets the pygame's screen width and height.
    GAME_CLOCK = pygame.time.Clock();
    
    # Grouping Measures to make Drawing and Updating Easier, and lessens clutter in the code.
    Updatable = pygame.sprite.Group()
    Drawable = pygame.sprite.Group()
    Asteroids = pygame.sprite.Group()
    Shots = pygame.sprite.Group()
    
    Player.containers = (Updatable, Drawable); # A class variable which adds the Player Class to the specified Containers/Groups.
    Asteroid.containers = (Asteroids, Updatable, Drawable); # Adds Asteroid Class to the specified Containers/Groups.
    AsteroidField.containers = (Updatable); 
    Shot.containers = (Updatable, Drawable); 
    
    Field = AsteroidField();
    PLAYER_1 = Player(SCREEN_WIDTH/2 + 50, SCREEN_HEIGHT/2);
    
    dt = 0;
    
    Game_State = True # Control Variable
    
    # Main Loop for the Game.
    while Game_State:
        # Checks for the quit game event, and if triggered, will quit the game and close the program.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit()
        
        SCREEN.fill("black") # Fills the background with the color black.
        
        # Loops through every Updatable entity and updates them
        for i in Updatable:
            i.update(dt)
        
        # Loops through every drawable entity and draws them
        for i in Drawable:
            i.draw(SCREEN)
            if i.Collision_Check(PLAYER_1) == True:
                print("Game Over!")
                pygame.quit()
            
        
        pygame.display.flip() # Refreshes the Screen
        
        dt = GAME_CLOCK.tick(60) / 1000 # Freezes the game for 1/60th of a second and assigns the delta time (time passed since last loop).
        
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()