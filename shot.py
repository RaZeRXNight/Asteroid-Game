from circleshape import CircleShape;
import pygame;



class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    # Draws the asteroid in the shape of a circle, at the inputted position.
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    # Moves the asteroid foward.
    def update(self, dt):
        self.position+= self.velocity * dt
        
    