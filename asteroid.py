from circleshape import * 
from constants import *
import random 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        if self.radius >= ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 50)
            vector1 = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.2
            vector2 = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = vector1
            asteroid_2.velocity = vector2
        self.kill()
       


