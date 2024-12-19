import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Trigger event every 2 seconds

# Sprite setup
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.color = color

    def change_color(self):
        # Randomly change the color of the sprite
        self.color = [random.randint(0, 255) for _ in range(3)]
        self.image.fill(self.color)

# Create two sprites
sprite1 = Sprite(BLUE, WIDTH // 3, HEIGHT // 2)
sprite2 = Sprite(RED, 2 * WIDTH // 3, HEIGHT // 2)

all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Clear the screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()