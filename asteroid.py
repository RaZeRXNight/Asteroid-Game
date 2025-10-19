import pygame;
from constants import *;
from random import uniform;
from circleshape import CircleShape;

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    # Draws the asteroid in the shape of a circle, at the inputted position.
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    # Moves the asteroid foward.
    def update(self, dt):
        self.position+= self.velocity * dt
        
    # Checks if another entity is drawn within the Asteroid.
    def Collision_Check(self, target):
        return (self.position.distance_to(target.position) < (self.radius + target.radius)) and self is not target
    
    # Destroys the current Asteroid, and Splits it into separate entities.
    def split(self):
        self.kill();
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Creating new Asteroids.
        random_angle = self.velocity.rotate(uniform(20, 50))
        random_angle2 = self.velocity.rotate(uniform(70, 110))
        New_Radius = self.radius - ASTEROID_MIN_RADIUS;
        
        # Creates two new Asteroids
        Asteroid(self.position.x, self.position.y, New_Radius).velocity = random_angle * 1.2
        Asteroid(self.position.x, self.position.y, New_Radius).velocity = -random_angle * 1.2
        