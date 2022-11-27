import pygame, sys
from pygame.locals import *
from hangman import *
#width and height variables
WIDTH, HEIGHT = 575, 600
#variable that stored the width and height
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#creating and displaying the name of our game
pygame.display.set_caption("Hangman game!")
#variable that holds the color
BLACK = (255, 0, 0)
#variable that holds the color white
WHITE = (255, 255, 255)
#variable that will hold elemnts of the border
BORDER = pygame.Rect(HEIGHT, 0, 10, WIDTH)
#frame per second
FPS = 960
#velocity
VEL = 1
#uploading the background image
CORN_IMAGE = pygame.image.load("scary_image.jpg")
#creating the size of the image
CORN_IMAGE = pygame.transform.scale(CORN_IMAGE, (525, 280))



#Shape of head,stick(body),2 sticks(legs), MAYBE A STICK NECK
#postaduim + the rope 
#pygame.draw.shape_name(parameters)
pygame.init()
#surface=10
#Line below is not working 
#pygame.draw.circle(surface,color,center,radi,width)
#window = surface
#surface for passing through its existence, center is location, radi is radius, width is the thickness of circle line
#to use pygames functions
# Importing pygame module

#shapes postoduim and the man (NOT CMPLTE)
# pygame.init()
# Displaysurf = pygame.display.set_mode((300,300))
# pygame.display.set_caption('SECOND PROGRAM SHAPES')

# black = (0,0,0)
# blue = (255,255,255)
# red = (255,0,0)
# yellow = (0,255,0)
# purple = (0,0,225)
# white = (300,200,100)
# Displaysurf.fill(white)

# pygame.draw.circle(Displaysurf,blue,((150,0),(300,150),(253,532)))
# pygame.draw.line(Displaysurf,red,((150,0),(300,150),(253,532)))

# pygame.display.update()

# while True:
#   for event in pygame.event.get():
#     if event.type == QUIT:
#       pygame.quit()
#       sys.exit()
#   pygame.display.update()






#function that draws the window
    #fill in the window with the color white
    #fill in the window with the color white
    #pasting the image
WIN.blit(CORN_IMAGE, (0, 0))
    #draw the rectangle
pygame.draw.rect(WIN, BLACK, BORDER)
    #display the whole rectangle
    #display the whole rectangle
pygame.display.update()

#begin the main function

#begin the main function
gamestart()
clock = pygame.time.Clock()
flag = True
while flag:
  clock.tick(FPS)
  for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

keys_pressed = pygame.key.get_pressed()
pygame.quit()
draw_window()

pygame.quit()
main()
