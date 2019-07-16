import pygame
import time


pygame.init()
music = pygame.mixer.Sound('ba.ogg')
music.play()
time.sleep(10)
print('end')

