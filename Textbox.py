
import pygame
import sys
import os
pygame.font.init()
font = pygame.font.Font("Sono.ttf", 20)
screen = pygame.display.set_mode((400,400))

def text():
  clock = pygame.time.Clock()
# it will display on screen 
# basic font for user typed
  base_font = pygame.font.Font("Sono.ttf", 32)

# create rectangle
  input_rect = pygame.Rect(250, 250, 100, 32)
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
  color_active = pygame.Color('lightskyblue3')
# color_passive store color(chartreuse4) which is
# color of input box.
  color_passive = pygame.Color('chartreuse4')
  color = color_passive
  active = False
  user_text = ''
  while True:
      for event in pygame.event.get():
      # if user types QUIT then the screen will close
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
          if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False  
          if event.type == pygame.KEYDOWN:  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:  
                user_text = user_text[:-1] 
            elif event.key == pygame.K_RETURN:
              return user_text
            else:
                user_text += event.unicode   

            
      if active:
        color = color_active
      else:
        color = color_passive          
      pygame.draw.rect(screen, color, input_rect)
      text_surface = base_font.render(user_text, True, (255, 255, 255))
      screen.blit(text_surface, (input_rect.x, input_rect.y))
      input_rect.w = max(100, text_surface.get_width()+10)
      pygame.display.flip()
      clock.tick(60)
  