__name__ = 'B. Joel'
"""
constants
June 16, 2023
Separate file for constants used throughout files
"""

import pygame
pygame.init

# colours
black = (0, 0, 0)
white = (255, 255, 255)
purple = (128, 0, 128)
grey = (128, 128, 128)
sky = (0, 0, 220)
blue = (85, 206, 255)
orange = (255, 127, 80)
red = (200, 0, 0)
light_red = (255, 0, 0)
green = (0, 200, 0)
light_green = (0, 255, 0)
# Puts colour codes in list to be called on in Accuracy Forge
colors = [black, grey, purple, sky, blue, orange, red, light_red, green, light_green]

count = 0

# Set the width and height of the screen (you can adjust these values)
screen_width = 1600
screen_height = 900

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Precision Pro")

# Set up font
font = pygame.font.init()
font = pygame.font.Font(None, 40)

img = pygame.image.load("bg.jpg")
img = pygame.transform.scale(img, (screen_width, screen_height))

# Set up button sizes
button_width = 300
button_height = 50

# Set up button positions
button1_pos = (screen_width // 2 - button_width // 2, 200)
button2_pos = (screen_width // 2 - button_width // 2, 300)
button3_pos = (screen_width // 2 - button_width // 2, 400)

menu_button_pos = (screen_width // 2 - button_width // 2, 70)

# Draw buttons
button1_rect = pygame.draw.rect(screen, red, (button1_pos[0], button1_pos[1], button_width, button_height))
button2_rect = pygame.draw.rect(screen, green, (button2_pos[0], button2_pos[1], button_width, button_height))
button3_rect = pygame.draw.rect(screen, blue, (button3_pos[0], button3_pos[1], button_width, button_height))