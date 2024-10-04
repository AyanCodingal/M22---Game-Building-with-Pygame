import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and background color
screen_width, screen_height = 800, 600
background_color = (255, 255, 255)

# Create a Pygame window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Text Display')

# Define colors
text_color = (0, 0, 0)  # Black text

# Load fonts and define font sizes
font1 = pygame.font.SysFont('Arial', 36)
font2 = pygame.font.SysFont('Comic Sans MS', 48)
font3 = pygame.font.SysFont('Courier New', 30)

# Create text surfaces
text_surface1 = font1.render('Hello, this is Arial font!', True, text_color)
text_surface2 = font2.render('This is Comic Sans MS font!', True, text_color)
text_surface3 = font3.render('Using Courier New font here!', True, text_color)

# Text positions
text_rect1 = text_surface1.get_rect(center=(screen_width//2, screen_height//3))
text_rect2 = text_surface2.get_rect(center=(screen_width//2, screen_height//2))
text_rect3 = text_surface3.get_rect(center=(screen_width//2, 2*screen_height//3))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill screen with background color
    screen.fill(background_color)

    # Blit text surfaces onto screen
    screen.blit(text_surface1, text_rect1)
    screen.blit(text_surface2, text_rect2)
    screen.blit(text_surface3, text_rect3)

    # Update display
    pygame.display.flip()
