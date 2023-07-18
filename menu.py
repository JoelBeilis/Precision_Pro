__name__ = 'B. Joel'
"""
menu
June 16, 2023
Separate file for a menu function that will be called multiple times to reset program
"""

import pygame
from constants import *
pygame.init()

def menu():
    # Clear the screen and prints background image
    screen.fill(white)
    screen.blit(img, (0, 0))

    button1_rect = pygame.draw.rect(screen, red, (button1_pos[0], button1_pos[1], button_width, button_height))
    button2_rect = pygame.draw.rect(screen, green, (button2_pos[0], button2_pos[1], button_width, button_height))
    button3_rect = pygame.draw.rect(screen, blue, (button3_pos[0], button3_pos[1], button_width, button_height))

    # Add text to buttons
    button1_text = font.render("Accuracy Forge", True, white)
    button2_text = font.render("Speed Click", True, white)
    button3_text = font.render("Quick React", True, white)

    # Prints the 3 buttons for the user
    screen.blit(button1_text, (button1_pos[0] + button_width // 2 - button1_text.get_width() // 2,
                               button1_pos[1] + button_height // 2 - button1_text.get_height() // 2))

    screen.blit(button2_text, (button2_pos[0] + button_width // 2 - button2_text.get_width() // 2,
                               button2_pos[1] + button_height // 2 - button2_text.get_height() // 2))

    screen.blit(button3_text, (button3_pos[0] + button_width // 2 - button3_text.get_width() // 2,
                               button3_pos[1] + button_height // 2 - button3_text.get_height() // 2))

    # Update the display
    pygame.display.update()

"""
Algorithm:
Functions: menu()

import pygame
from constants import *
pygame.init()

func menu():
    # Clear the screen and prints background image
    screen.fill(white)
    screen.blit(img, (0, 0))

    button1_rect = pygame.draw.rect(screen, red, (button1_pos[0], button1_pos[1], button_width, button_height))
    button2_rect = pygame.draw.rect(screen, green, (button2_pos[0], button2_pos[1], button_width, button_height))
    button3_rect = pygame.draw.rect(screen, blue, (button3_pos[0], button3_pos[1], button_width, button_height))

    # Add text to buttons
    button1_text = font.render("Accuracy Forge", True, white)
    button2_text = font.render("Speed Click", True, white)
    button3_text = font.render("Quick React", True, white)

    # Prints the 3 buttons for the user
    screen.blit(button1_text, (button1_pos[0] + button_width // 2 - button1_text.get_width() // 2,
                               button1_pos[1] + button_height // 2 - button1_text.get_height() // 2))

    screen.blit(button2_text, (button2_pos[0] + button_width // 2 - button2_text.get_width() // 2,
                               button2_pos[1] + button_height // 2 - button2_text.get_height() // 2))

    screen.blit(button3_text, (button3_pos[0] + button_width // 2 - button3_text.get_width() // 2,
                               button3_pos[1] + button_height // 2 - button3_text.get_height() // 2))

    # Update the display
    pygame.display.update()

"""