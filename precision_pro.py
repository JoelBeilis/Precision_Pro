__name__ = 'B. Joel'
"""
precision_pro
June 16, 2023

Applications runs 3 simulators to check user's reactions

After launching the program there will be 3 buttons present that will play the 3 different simulators

The first one is using the mouse to click as many circles as possible in the timeframe

The second one is using the mouse to click anywhere on the screen as fast as possible to calculate your clicks/second

The third one is using the mouse, by clicking on the screen the program begins. Then the screen tells you when to click 
again and will print in milliseconds how long it took for you to react in milliseconds
"""

import pygame
import math
import time
import random
from constants import *
from menu import *

# Initialize Pygame
pygame.init()

# Loop for introduction screen
running = True
while running:
    screen.fill(black)
    # prints welcome text
    welcome_text = font.render('Welcome To Precision Pro', True, white)
    screen.blit(welcome_text, (screen_width/2-200, screen_height/2-100))
    pygame.display.update()
    # wait so the loading screen stays long enough for viewer to see
    pygame.time.wait(2000)
    running = False

# Loop to keep whole program running
while True:
    menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            """
            Runs the first simulator using your mouse click the circles that appear on the screen
            """
            if button1_rect.collidepoint(mouse_pos):
                start_time = time.time()
                duration = 61  # Countdown duration in seconds set to 61 so printing starts at 60
                clock = pygame.time.Clock()  # To set the frame rate
                clicked_circle = 0
                total_clicks = -1 # starts at -1 to cancel the first click when starting the game
                screen.fill(white)

                # Draws the first circle when program loads
                row_x = random.randint(75, screen_width - 150)
                col_y = random.randint(300, screen_height - 150)
                width_of_circle = random.randint(25, 35)
                pygame.draw.circle(screen, random.choice(colors), (row_x, col_y), width_of_circle)

                # Main loop
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit()
                        # increases count of total_clicks everytime mouse pressed for later calculations
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            total_clicks += 1

                    # timer logic
                    if time.time() - start_time >= duration:
                        break

                    # Draw the countdown text
                    timer = int(duration - (time.time() - start_time))
                    timer_text = font.render("Time left: {}".format(timer), True, black)

                    # Drawing Rectangle and timer. Rectangle resets timer so it does not print over itself
                    pygame.draw.rect(screen, white, pygame.Rect(0, 0, 200, 60))
                    screen.blit(timer_text, (10, 10))

                    # Variables used to get position of circle based off x-axis and y-axis
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    click = pygame.mouse.get_pressed()

                    # using circle formula to draw to make clicks more precise
                    squared_x = (x - row_x) ** 2
                    squared_y = (y - col_y) ** 2

                    # Increases count of click, and resets so another circle can spawn after clicked
                    if math.sqrt(squared_x + squared_y) < width_of_circle and click[0] == 1:
                        screen.fill(white)  # Reset the screen
                        # Continuously draws circles
                        row_x = random.randint(75, screen_width - 150)
                        col_y = random.randint(300, screen_height - 150)
                        width_of_circle = random.randint(25, 35)
                        pygame.draw.circle(screen, random.choice(colors), (row_x, col_y), width_of_circle)
                        clicked_circle += 1

                    screen.blit(timer_text, (10, 10))
                    menu_button = pygame.draw.rect(screen, green,
                                                   (menu_button_pos[0], menu_button_pos[1], button_width,
                                                    button_height))
                    menu_button_text = font.render("Return to Menu", True, white)

                    screen.blit(menu_button_text,
                                (button2_pos[0] + button_width // 2 - menu_button_text.get_width() // 2, button2_pos[1] + button_height // 2 - menu_button_text.get_height() // 2 - 230))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if menu_button.collidepoint(mouse_pos):
                            print('menu button clicked. returning')
                            break
                            menu()

                    pygame.display.flip()
                    clock.tick()

                screen.fill(white)
                score_text = font.render("Total circles clicked: {}".format(clicked_circle), True, black)
                screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 - score_text.get_height() // 2 - 25))

                if total_clicks != 0:
                    avg_score_text = font.render(
                        "Accuracy Percentage: {}%".format(round((clicked_circle / total_clicks) * 100, 2)), True, black)
                    screen.blit(avg_score_text, (
                    screen_width // 2 - avg_score_text.get_width() // 2,
                    screen_height // 2 - avg_score_text.get_height() // 2 - 100))
                else:
                    avg_score_text = font.render("Accuracy Percentage: You clicked 0 times", True, black)
                    screen.blit(avg_score_text, (screen_width // 2 - avg_score_text.get_width() // 2, screen_height // 2 - avg_score_text.get_height() // 2 - 100))

                # updates the screen and waits before sending user back to menu
                pygame.display.flip()
                pygame.time.wait(2000)

            elif button2_rect.collidepoint(mouse_pos):
                """
                Runs second program, user uses mouse to click anywhere on the screen until time runs out.
                """
                start_time = time.time()
                duration = 5  # Countdown duration in seconds
                count = 0

                while True:
                    # Update the screen
                    screen.fill(green)

                    # Check if the countdown has reached 0
                    if time.time() - start_time >= duration:
                        break

                    # Draw the countdown text
                    countdown = int(duration - (time.time() - start_time))
                    countdown_text = font.render("Time left: {}".format(countdown), True, white)
                    screen.blit(countdown_text, (10, 10))

                    button_pos = (screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2)
                    cps_button = pygame.draw.rect(screen, green, (button_pos[0], button_pos[1], button_width, button_height))
                    cps_button_text = font.render("Click Anywhere! Clicks: {}".format(count), True, white)
                    screen.blit(cps_button_text, (button_pos[0] + button_width // 2 - cps_button_text.get_width() // 2, button_pos[1] + button_height // 2 - cps_button_text.get_height() // 2))

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        # if screen was clicked the count will increase
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            count += 1

                    pygame.display.flip()
                    pygame.display.update()

                """
                New screen. Shows the final score after the countdown ends
                """
                screen.fill(green)
                score_text = font.render("Final score: {}".format(count), True, white)
                screen.blit(score_text, (
                screen_width // 2 - score_text.get_width() // 2, screen_height // 2 - score_text.get_height() // 2 - 25))

                # Calculates your clicks per second and uses round function to round to 2 decimal places
                cps_text = font.render("Your clicks per second: {}".format(round(count/5, 2)), True, white)
                screen.blit(cps_text, (screen_width // 2 - cps_text.get_width() // 2, screen_height // 2 - cps_text.get_height() // 2 + 25))

                # Updates and waits for a short time before quitting
                pygame.display.flip()
                pygame.time.wait(2000)

            elif button3_rect.collidepoint(mouse_pos):
                """
                Runs simulator 3, user uses the mouse to start the program. After a random amount of time quickly press the left mouse button when prompted. 
                """
                explanation_text = font.render("PRESS LEFT MOUSE BUTTON TO START TEST", 0, white)
                start_text = font.render("PRESS LEFT MOUSE BUTTON", 0, black)

                reaction = None
                average_reaction = None
                simulator = "start"
                start_time = 0
                average_time = 0
                count = 0

                while True:
                    current_time = pygame.time.get_ticks()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit()

                        # Calculations when mouse is pressed
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if simulator == "start":
                                simulator = "wait"
                                # Uses random function to make when user must click unpredictable
                                # Multiplied by 1000 so that the count is in seconds
                                start_time = current_time + (random.randint(1, 4)*1000)
                            if simulator == "wait_for_press":
                                simulator = "wait"
                                # Calculates reaction time
                                reaction_time = (current_time - start_time) / 1000
                                start_time = current_time + (random.randint(1, 4)*1000)
                                count += 1
                                average_time = (average_time * (count - 1) + reaction_time) / count
                                reaction = font.render(f"REACTION TIME: {reaction_time:.03f}", 0, white)
                                average_reaction = font.render(f"AVERAGE REACTION TIME IS: {average_time:.03f}", 0, white)

                    if simulator == "wait":
                        if current_time >= start_time:
                            simulator = "wait_for_press"

                    # Does all outputs through text
                    screen.fill(blue)
                    center = screen.get_rect().center

                    if simulator == "start":
                        screen.blit(explanation_text, explanation_text.get_rect(center=center))
                    if simulator == "wait_for_press":
                        screen.blit(start_text, start_text.get_rect(center=center))
                    if reaction:
                        screen.blit(reaction, reaction.get_rect(center=(center[0], 350)))
                    if average_reaction:
                        screen.blit(average_reaction, average_reaction.get_rect(center=(center[0], 400)))

                    """
                    Allows user to click a button to return to the main menu if they wish not to continue playing (must use mouse)
                    """
                    menu_button = pygame.draw.rect(screen, green, (menu_button_pos[0], menu_button_pos[1], button_width, button_height))
                    menu_button_text = font.render("Return to Menu", True, white)

                    screen.blit(menu_button_text, (button2_pos[0] + button_width // 2 - menu_button_text.get_width() // 2, button2_pos[1] + button_height // 2 - menu_button_text.get_height() // 2 - 230))

                    # Checks mouse position to check if the menu was clicked or screen
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if menu_button.collidepoint(mouse_pos):
                            print('menu button clicked. returning')
                            break
                            #runs function to reset menu from another file
                            menu()

                    pygame.display.update()


"""
Algorithm:

running = True
while running:
    screen.fill(black)
    welcome_text = font.render('Welcome To Precision Pro', True, white)
    screen.blit(welcome_text, (screen_width/2-200, screen_height/2-100))
    pygame.display.update()
    pygame.time.wait(2000)
    running = False
end loop

while True:
    menu()
    end menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button1_rect.collidepoint(mouse_pos):
                start_time = time.time()
                duration = 61  
                clock = pygame.time.Clock()  
                clicked_circle = 0
                total_clicks = -1 
                screen.fill(white)

                row_x = random.randint(75, screen_width - 150)
                col_y = random.randint(300, screen_height - 150)
                width_of_circle = random.randint(25, 35)
                pygame.draw.circle(screen, random.choice(colors), (row_x, col_y), width_of_circle)

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            total_clicks += 1

                    if time.time() - start_time >= duration:
                        break

                    timer = int(duration - (time.time() - start_time))
                    timer_text = font.render("Time left: {}".format(timer), True, black)

                    pygame.draw.rect(screen, white, pygame.Rect(0, 0, 200, 60))
                    screen.blit(timer_text, (10, 10))

                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    click = pygame.mouse.get_pressed()

                    squared_x = (x - row_x) ** 2
                    squared_y = (y - col_y) ** 2

                    if math.sqrt(squared_x + squared_y) < width_of_circle and click[0] == 1:
                        screen.fill(white)  # Reset the screen
                        row_x = random.randint(75, screen_width - 150)
                        col_y = random.randint(300, screen_height - 150)
                        width_of_circle = random.randint(25, 35)
                        pygame.draw.circle(screen, random.choice(colors), (row_x, col_y), width_of_circle)
                        clicked_circle += 1

                    screen.blit(timer_text, (10, 10))
                    menu_button = pygame.draw.rect(screen, green,
                                                   (menu_button_pos[0], menu_button_pos[1], button_width,
                                                    button_height))
                    menu_button_text = font.render("Return to Menu", True, white)

                    screen.blit(menu_button_text,
                                (button2_pos[0] + button_width // 2 - menu_button_text.get_width() // 2, button2_pos[1] + button_height // 2 - menu_button_text.get_height() // 2 - 230))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if menu_button.collidepoint(mouse_pos):
                            print('menu button clicked. returning')
                            break
                            menu()

                    pygame.display.flip()
                    clock.tick()

                screen.fill(white)
                score_text = font.render("Total circles clicked: {}".format(clicked_circle), True, black)
                screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 - score_text.get_height() // 2 - 25))

                if total_clicks != 0:
                    avg_score_text = font.render(
                        "Accuracy Percentage: {}%".format(round((clicked_circle / total_clicks) * 100, 2)), True, black)
                    screen.blit(avg_score_text, (screen_width // 2 - avg_score_text.get_width() // 2, screen_height // 2 - avg_score_text.get_height() // 2 - 100))
                else:
                    avg_score_text = font.render("Accuracy Percentage: You clicked 0 times", True, black)
                    screen.blit(avg_score_text, (screen_width // 2 - avg_score_text.get_width() // 2, screen_height // 2 - avg_score_text.get_height() // 2 - 100))

                pygame.display.flip()
                pygame.time.wait(2000)
            end if button1
            end loop
            
            elif button2_rect.collidepoint(mouse_pos):
                start_time = time.time()
                duration = 5 
                count = 0

                while True:
                    screen.fill(green)

                    if time.time() - start_time >= duration:
                        break

                    countdown = int(duration - (time.time() - start_time))
                    countdown_text = font.render("Time left: {}".format(countdown), True, white)
                    screen.blit(countdown_text, (10, 10))

                    button_pos = (screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2)
                    cps_button = pygame.draw.rect(screen, green, (button_pos[0], button_pos[1], button_width, button_height))
                    cps_button_text = font.render("Click Anywhere! Clicks: {}".format(count), True, white)
                    screen.blit(cps_button_text, (button_pos[0] + button_width // 2 - cps_button_text.get_width() // 2, button_pos[1] + button_height // 2 - cps_button_text.get_height() // 2))

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            count += 1

                    pygame.display.flip()
                    pygame.display.update()
                end loop

                screen.fill(green)
                score_text = font.render("Final score: {}".format(count), True, white)
                screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 - score_text.get_height() // 2 - 25))

                cps_text = font.render("Your clicks per second: {}".format(round(count/5, 2)), True, white)
                screen.blit(cps_text, (screen_width // 2 - cps_text.get_width() // 2, screen_height // 2 - cps_text.get_height() // 2 + 25))

                pygame.display.flip()
                pygame.time.wait(2000)
            end elif button2

            elif button3_rect.collidepoint(mouse_pos):
                explanation_text = font.render("PRESS LEFT MOUSE BUTTON TO START TEST", 0, white)
                start_text = font.render("PRESS LEFT MOUSE BUTTON", 0, black)

                reaction = None
                average_reaction = None
                simulator = "start"
                start_time = 0
                average_time = 0
                count = 0

                while True:
                    current_time = pygame.time.get_ticks()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if simulator == "start":
                                simulator = "wait"
                                start_time = current_time + (random.randint(1, 4)*1000)
                            if simulator == "wait_for_press":
                                simulator = "wait"
                                reaction_time = (current_time - start_time) / 1000
                                start_time = current_time + (random.randint(1, 4)*1000)
                                count += 1
                                average_time = (average_time * (count - 1) + reaction_time) / count
                                reaction = font.render(f"REACTION TIME: {reaction_time:.03f}", 0, white)
                                average_reaction = font.render(f"AVERAGE REACTION TIME IS: {average_time:.03f}", 0, white)

                    if simulator == "wait":
                        if current_time >= start_time:
                            simulator = "wait_for_press"

                    screen.fill(blue)
                    center = screen.get_rect().center

                    if simulator == "start":
                        screen.blit(explanation_text, explanation_text.get_rect(center=center))
                    if simulator == "wait_for_press":
                        screen.blit(start_text, start_text.get_rect(center=center))
                    if reaction:
                        screen.blit(reaction, reaction.get_rect(center=(center[0], 350)))
                    if average_reaction:
                        screen.blit(average_reaction, average_reaction.get_rect(center=(center[0], 400)))

                    menu_button = pygame.draw.rect(screen, green, (menu_button_pos[0], menu_button_pos[1], button_width, button_height))
                    menu_button_text = font.render("Return to Menu", True, white)

                    screen.blit(menu_button_text, (button2_pos[0] + button_width // 2 - menu_button_text.get_width() // 2, button2_pos[1] + button_height // 2 - menu_button_text.get_height() // 2 - 230))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if menu_button.collidepoint(mouse_pos):
                            print('menu button clicked. returning')
                            break
                            #runs function to reset menu from another file
                            menu()

                    pygame.display.update()
                    
                end loop
            end elif button 3
"""