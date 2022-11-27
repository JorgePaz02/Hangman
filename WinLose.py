
import pygame
import sys
import os
pygame.font.init()
font = pygame.font.Font("Sono.ttf", 20)
screen = pygame.display.set_mode((400,400))
WHITE= (255,255,255,1)
BLACK=(0,0,0,0)
YELLOW= (0,255,255,0)
RED=(255,0,0,0)

def winEndgame():
  screen.fill(BLACK)
  pygame.font.init()
  font = pygame.font.Font("Sono.ttf", 50)
  text = font.render("WINNER", True, YELLOW)
  text_rect = text.get_rect()
  text_rect.center = (200,200)
  screen.blit(text, text_rect)
  pygame.display.update()
  pygame.quit

def Gameover():
  screen.fill(BLACK)
  pygame.font.init()
  font = pygame.font.Font("Sono.ttf", 50)
  text = font.render("GAME OVER", True, RED)
  text_rect = text.get_rect()
  text_rect.center = (200,200)
  screen.blit(text, text_rect)
  pygame.display.update()
  pygame.quit