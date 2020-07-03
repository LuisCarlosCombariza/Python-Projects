# Luis Combariza - July 1 2020
# This game is the start of a series of projects in order to practice
# fundamental coding and git skills.

import pygame
import os
import time
import random

# Game window
# -----------------------------------------------------------------------------------------
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SpaceInvaders")

# Load Images
# ----------------------------------------------------------------------------------------- #
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

# Background
BACK_GROUND = pygame.image.load(os.path.join("background-black.png"))


