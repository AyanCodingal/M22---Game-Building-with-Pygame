import pygame
import sys
import random
#bash 
#pip install pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Color Change Event")

# Define colors
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]  # List of colors

# Custom event for changing sprite color
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Change color every 2000 milliseconds (2 seconds)

# Sprite class
class RectangleSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        self.color = random.choice(COLORS)
        self.image.fill(self.color)

# Create two sprites
sprite1 = RectangleSprite(COLORS[0], 100, 100, 150, 200)
sprite2 = RectangleSprite(COLORS[1], 100, 100, 400, 200)

# Create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Fill screen with white
    screen.fill((255, 255, 255))

    # Draw all sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
