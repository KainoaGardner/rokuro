from settings import *
import pygame
import math
import numpy as np


class Rokuro:
    def __init__(self,size):
        self.board = np.zeros((size,size))
        self.makeCirle()
        self.angle = 0 
        self.speed = 0
        self.brushSize = 1
        self.color = 2

    def makeCirle(self):
        radius = 0
        angle = 0
        while angle < 360:
            while radius < WIDTH // 2 - TILESIZE:
                xDist = math.cos(math.radians(angle)) * radius
                yDist = math.sin(math.radians(angle)) * radius
                radius += TILESIZE // 2
                row = int((HEIGHT // 2 + yDist) // TILESIZE)
                col = int((WIDTH // 2 +  xDist) // TILESIZE)
                self.board[row][col] = 1
            angle += 1
            radius = 0
        
    def drawPos(self):
        if pygame.mouse.get_pressed()[0]:
            mos = pygame.mouse.get_pos()
            xDif = mos[0] - WIDTH // 2
            yDif = HEIGHT // 2 - mos[1]
            distance = math.sqrt(xDif * xDif + yDif * yDif)
            angle = math.degrees(math.atan2(yDif,xDif))
            angle += self.angle
            xSide = math.cos(math.radians(angle)) * distance
            ySide = math.sin(math.radians(angle)) * distance
            if distance < WIDTH // 2:
                xTile = int((WIDTH // 2 + xSide) // TILESIZE)
                yTile = int((HEIGHT // 2 + ySide) // TILESIZE)
                self.draw((xTile,yTile))

    def draw(self,pos):
        if 0 <= pos[0] < TILEAMOUNT and 0 <= pos[1] < TILEAMOUNT:
            for r in range(pos[1] - self.brushSize,pos[1] + self.brushSize + 1):
                for c in range(pos[0] - self.brushSize,pos[0] + self.brushSize + 1):
                    if 0 <= c < TILEAMOUNT and 0 <= r < TILEAMOUNT:
                        if self.board[r][c] != 0:
                            self.board[r][c] = self.color

    def changeSpeed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.speed > - 15:
            self.speed -= 1 / 3
        if keys[pygame.K_RIGHT] and self.speed < 15:
            self.speed += 1 / 3

    def changePenSize(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.brushSize = 0
        if keys[pygame.K_2]:
            self.brushSize = 1
        if keys[pygame.K_3]:
            self.brushSize = 2
        if keys[pygame.K_4]:
            self.brushSize = 3

        if keys[pygame.K_r]:
            self.color = 2
        if keys[pygame.K_g]: 
            self.color = 4
        if keys[pygame.K_b]:
            self.color = 3
        if keys[pygame.K_y]:
            self.color = 5
        if keys[pygame.K_v]:
            self.color = 6
        if keys[pygame.K_e]:
            self.color = 1

    def update(self):
        self.drawPos()
        self.changeSpeed()
        self.changePenSize()
        self.angle += self.speed

    def display(self,screen):
        pygame.draw.circle(screen,WHITE,(WIDTH // 2,HEIGHT // 2),WIDTH // 2)
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                xDif = (c * TILESIZE + TILESIZE // 2) - (WIDTH // 2)
                yDif = (HEIGHT // 2) - (r * TILESIZE + TILESIZE // 2) 
                distance = math.sqrt(xDif * xDif + yDif * yDif)
                angle = math.degrees(math.atan2(yDif,xDif))
                angle += self.angle
                xSide = math.cos(math.radians(angle)) * distance
                ySide = math.sin(math.radians(angle)) * distance

                if self.board[r][c] == 1:
                    pygame.draw.circle(screen,WHITE,(WIDTH // 2 + xSide,HEIGHT // 2 + ySide),TILESIZE//2)
                elif self.board[r][c] == 2:
                    pygame.draw.circle(screen,RED,(WIDTH // 2 + xSide,HEIGHT // 2 + ySide),TILESIZE//2)
                elif self.board[r][c] == 3:
                    pygame.draw.circle(screen,BLUE,(WIDTH // 2 + xSide,HEIGHT // 2 + ySide),TILESIZE//2)
                elif self.board[r][c] == 4:
                    pygame.draw.circle(screen,GREEN,(WIDTH // 2 + xSide,HEIGHT // 2 + ySide),TILESIZE//2)
                elif self.board[r][c] == 5:
                    pygame.draw.circle(screen,YELLOW,(WIDTH // 2 + xSide,HEIGHT // 2 + ySide),TILESIZE//2)
                elif self.board[r][c] == 6:
                    pygame.draw.circle(screen,BLACK,(WIDTH // 2 + xSide,HEIGHT // 2 + ySide),TILESIZE//2)





