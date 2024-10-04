import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangle Sprite Control")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create rectangles
rect1 = pygame.Rect(100, 100, 50, 50)  # Sprite 1
rect2 = pygame.Rect(300, 300, 50, 50)  # Sprite 2

# Define movement speed for controlled sprite
move_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move rect1 based on arrow keys
    if keys[pygame.K_LEFT]:
        rect1.x -= move_speed
    if keys[pygame.K_RIGHT]:
        rect1.x += move_speed
    if keys[pygame.K_UP]:
        rect1.y -= move_speed
    if keys[pygame.K_DOWN]:
        rect1.y += move_speed

    # Fill screen with white
    screen.fill(WHITE)

    # Draw rectangles
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
