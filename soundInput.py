import pygame
import time

from pygame.locals import *

pygame.init()

sound = pygame.mixer.Sound("scream.wav")
sound.play ()
time.sleep(1)
