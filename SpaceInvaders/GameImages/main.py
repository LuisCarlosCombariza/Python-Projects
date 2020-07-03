# Luis Combariza - July 1 2020
# This game is the start of a series of projects in order to practice
# fundamental coding and git skills.

import pygame
import os
import time
import random
pygame.init()

# Game window
# -----------------------------------------------------------------------------------------
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("-SpaceInvaders-")

# Load Images
# -----------------------------------------------------------------------------------------
# Enemy Ships:
RED_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_blue_small.png"))
# Player Ship:
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("pixel_ship_yellow.png"))

# Lasers:
RED_LASER = pygame.image.load(os.path.join("pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("pixel_laser_blue.png"))
BLUE_LASER = pygame.image.load(os.path.join("pixel_laser_green.png"))
YELLOW_LASER = pygame.image.load(os.path.join("pixel_laser_green.png"))

# Scaled - Background
BACK_GROUND = pygame.transform.scale(pygame.image.load(os.path.join("background-black.png")),(WIDTH,HEIGHT))


# Game object classes
# ------------------------------------------------------------------------------------------
class Ship:
    def __init__(self, location_x, location_y, health= 100):
        self.location_x = location_x
        self.location_y = location_y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self,window):
        pygame.draw.rect(window,(255,0,0),(self.location_x,self.location_y, 50,50),0)



# Even Main Loop
# ------------------------------------------------------------------------------------------
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans",50)
    clock  = pygame.time.Clock()
    ship = Ship(300,650)

    def redraw_window():
        # Adding the background image at coordinate (0,0)
        WINDOW.blit(BACK_GROUND, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives:{lives}",1,(250,0,0))
        level_label = main_font.render(f"Level:{level}",1,(255,255,255))

        # Game labels
        WINDOW.blit(lives_label,(10,10))
        WINDOW.blit(level_label,(WIDTH - level_label.get_width() - 10,10))

        ship.draw(WINDOW)

        pygame.display.update()

    while run:
        # setting clock speed to 60fps to make sure game runs smoothly in all devices
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

main()
