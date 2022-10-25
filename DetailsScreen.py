# import sys module
import pygame
import sys

pygame.init()

# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''

# create rectangle
input_rect = pygame.Rect(260, 153, 140, 32)
input_rect2 = pygame.Rect(200, 403, 140, 32)

color = pygame.Color('chartreuse4')

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 800
Y = 800

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Show Text')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
title_text = font.render('Enter Your Details:', True, green, blue)
organ_text = font.render('Organ/Blood:', True, blue, green)
name_text = font.render('First Name:', True, blue, green)
id_text = font.render('ID:', True, blue, green)
age_text = font.render('Age:', True, blue, green)
gender_text = font.render('Gender:', True, blue, green)
bloodType_text = font.render('Blood Type:', True, blue, green)
address_text = font.render('Address:', True, blue, green)
# create a rectangular object for the
# text surface object
title_textRect = title_text.get_rect()
organ_textRect = organ_text.get_rect()
name_textRect = organ_text.get_rect()
id_textRect = organ_text.get_rect()
age_textRect = organ_text.get_rect()
gender_textRect = organ_text.get_rect()
bloodType_textRect = organ_text.get_rect()
address_textRect = organ_text.get_rect()

# set the center of the rectangular object.
title_textRect.center = (400, 60)
organ_textRect.center = (150, 120)
name_textRect.center = (150, 170)
id_textRect.center = (150, 220)
age_textRect.center = (150, 270)
gender_textRect.center = (150, 320)
bloodType_textRect.center = (150, 370)
address_textRect.center = (150, 420)

# infinite loop
while True:

    # completely fill the surface object
    # with white color
    display_surface.fill(white)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(title_text, title_textRect)
    display_surface.blit(organ_text, organ_textRect)
    display_surface.blit(name_text, name_textRect)
    display_surface.blit(id_text, id_textRect)
    display_surface.blit(age_text, age_textRect)
    display_surface.blit(gender_text, gender_textRect)
    display_surface.blit(bloodType_text, bloodType_textRect)
    display_surface.blit(address_text, address_textRect)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()
        if event.type == pygame.KEYDOWN:

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode

        # Draws the surface object to the screen.
        pygame.display.update()

    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(display_surface, color, input_rect)
    pygame.draw.rect(display_surface, color, input_rect2)

    text_surface = base_font.render(user_text, True, (255, 255, 255))
    text_surface2 = base_font.render(user_text, True, (255, 255, 255))
    # render at position stated in arguments
    display_surface.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    display_surface.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)
    input_rect2.w = max(100, text_surface2.get_width() + 10)

    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
