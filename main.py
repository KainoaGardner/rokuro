from settings import *
from rokuro import Rokuro
import math
import pygame

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def main():
    rokuro = Rokuro(TILEAMOUNT)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        display(screen,rokuro) 


def display(screen,rokuro):
    screen.fill(BLACK)
    rokuro.display(screen)
    rokuro.update()
    pygame.display.update()
    clock.tick(FPS)


main()
