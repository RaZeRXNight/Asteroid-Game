from circleshape import CircleShape;
from shot import Shot;
from constants import *;
import pygame;

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Draws the player character.
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    # Rotates the player character according to their turn speed and the refresh rate (delta time).
    def rotate(self, dt):
        self.rotation+= PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self, dt):
        Player_Shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        Player_Shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        Player_Shot.velocity*= PLAYER_SHOOT_SPEED
        
    # Moves the player Character 
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
            