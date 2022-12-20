import pygame, random
from fish import Fish

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
clock.tick(60)

# Set the window size
window_size = (900, 720)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Aquarium Simulator")

# Load the background image
background_image = pygame.image.load("assets/Aquarium.png")

# Load the fish image
fish_image = pygame.image.load("assets/Betta.png")

# Create a list to store the fish
fish_list = []

# Add some initial fish to the list
for i in range(20):
    x = random.uniform(0, window_size[0])
    y = random.uniform(0, window_size[1])
    fish_list.append(Fish(x, y, fish_image))

# Set the background color
background_color = (0, 0, 255)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the positions of the fish
    for fish in fish_list:
        fish.move()

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the fish
    for fish in fish_list:
        screen.blit(fish.image, (fish.x, fish.y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()