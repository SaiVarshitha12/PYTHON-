import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Trail Cursor 🎨")

# Clock
clock = pygame.time.Clock()

# Particle class
class Particle:
    def __init__(self, pos):
        self.x, self.y = pos
        self.radius = random.randint(5, 15)
        self.color = random.choice([
            (255, 100, 100),  # red
            (100, 255, 100),  # green
            (100, 100, 255),  # blue
            (255, 255, 100),  # yellow
            (255, 100, 255),  # magenta
            (100, 255, 255),  # cyan
        ])
        self.alpha = 255
        self.surf = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
    
    def update(self):
        self.alpha -= 5
        self.radius -= 0.3
        if self.radius < 0: self.radius = 0
        self.surf.fill((0, 0, 0, 0))
        pygame.draw.circle(self.surf, (*self.color, self.alpha), (self.radius, self.radius), int(self.radius))
    
    def draw(self, target):
        target.blit(self.surf, (self.x - self.radius, self.y - self.radius))

particles = []

# Main loop
while True:
    screen.fill((0, 0, 0))  # black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Add new particle
    particles.append(Particle(mouse_pos))

    # Update and draw particles
    for p in particles[:]:
        p.update()
        p.draw(screen)
        if p.alpha <= 0:
            particles.remove(p)

    pygame.display.update()
    clock.tick(60)
