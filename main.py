import pygame
import os
import time
import random

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

 # Load Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

 # Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

 # Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.ping"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.ping"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.ping"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.ping"))

 # Background
BG = RED_LASER = pygame.image.load(os.path.join("assets", "background-black.png"))
