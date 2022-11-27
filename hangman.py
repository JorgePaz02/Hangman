from Textbox import *
import pygame
import sys
import os
import random
pygame.font.init()
font = pygame.font.Font("Sono.ttf", 20)
WHITE= (255,255,255,1)
BLACK=(0,0,0,0)
YELLOW= (0,255,255,0)
RED=(255,0,0,0)
#GLOBAL VARIABLES- OUR MAIN LISTS
word = []  #ORIGINAL WORD
answer = []  #FILLED WITH _ TILL GUESS CORRECT
screen = pygame.display.set_mode((400,400))


def gamestart():  #BEGINS THE GAME
  screen.fill(BLACK)
    
  statement = font.render("Are you ready to play?", True, WHITE)
  statement_rect = statement.get_rect()
  statement_rect.center = (200,200)
  screen.blit(statement, statement_rect)
  pygame.display.update()
  
  choice = text()
  choice = choice.upper()
  if choice == 'Y':
        difficulty()
        #do we call this here or not
        #wordset()
  else:
        print("Oh, ok bye then.")
        pygame.quit()
  gamebegin()


'''

'''


def wordset(fileName):  #SETS UP THE WORD FOR THE GAME. MAY BE UPDATED WITH RANDOMIZER
    list = readfile(fileName)

    #generate a random selection from txt file
    randWord = random.choice(list)
    #add letters of the random word into word array to store answer, skipping spaces
    for item in randWord:
        if (item == " "):
            continue
        else:
            word.append(item)
    #test outputs
    print(randWord)
    print(word)
    i = 0
    for item in word:
        answer.insert(i, '_')
        i = i + 1


#
'''
#this is previous wordset function
for item in list[0]:
    word.insert(i, item)
    i= i+1
  i=0
  for item in word:
    answer.insert(i, '_')
    i= i+1
'''


def difficulty():
  screen.fill(BLACK)
    
  statement = font.render("What level of difficulty will you like? ", True, WHITE)
  statement_rect = statement.get_rect()
  statement_rect.center = (260,200)
  screen.blit(statement, statement_rect)

      
  statement2 = font.render("E for easy, M for medium, H for hard ", True, WHITE)
  statement2_rect = statement2.get_rect()
  statement2_rect.center = (250,220)
  screen.blit(statement2, statement2_rect)
  
  pygame.display.update()
  answer = text()
  answer = answer.upper()
    #EASY CATEGORIES
    #FIXME: Still need to fill files with potential answers
  if answer == 'E':  #easy
      screen.fill(BLACK)
      statement2 = font.render("Please pick a category: ", True, WHITE)
      statement2_rect = statement2.get_rect()
      statement2_rect.center = (250,200)
      screen.blit(statement2, statement2_rect)
    
      statement = font.render("food, transportation, or colors ", True, WHITE)
      statement_rect = statement.get_rect()
      statement_rect.center = (250,220)
      screen.blit(statement, statement_rect)
    
      cat = text()
      cat = cat.upper()
      if cat == 'FOOD':
        wordset('WordLists/Easy/FoodEasy.txt')
      elif cat == 'TRANSPORTATION':
        wordset('WordLists/Easy/TransportationMethodsEasy.txt')
      elif cat == 'COLORS':
        wordset('WordLists/Easy/ColorsEasy.txt')

    #MEDIUM CATEGORIES
  elif answer == 'M':
      screen.fill(BLACK)
      statement2 = font.render("Please pick a category: ", True, WHITE)
      statement2_rect = statement2.get_rect()
      statement2_rect.center = (250,200)
      screen.blit(statement2, statement2_rect)

      statement = font.render("food, colors, or clothing ", True, WHITE)
      statement_rect = statement.get_rect()
      statement_rect.center = (250,220)
      screen.blit(statement, statement_rect)
      cat = text()
      cat = cat.upper()
      if cat == 'FOOD':
        wordset('WordLists/Medium/FoodMedium.txt')
      elif cat == 'COLORS':
        wordset('WordLists/Medium/ColorsMedium.txt')
      elif cat == 'CLOTHING':
        wordset('WordLists/Medium/ClothingMedium.txt')
    # wordset(mediumfile)

    #HARD CATEGORIES
  if answer == 'H':
      statement2 = font.render("Please pick a category: ", True, WHITE)
      statement2_rect = statement2.get_rect()
      statement2_rect.center = (250,200)
      screen.blit(statement2, statement2_rect)
    
      statement = font.render("food or colors", True, WHITE)
      statement_rect = statement.get_rect()
      statement_rect.center = (250,220)
      screen.blit(statement, statement_rect)#FIXME: update categories
    
      cat = text()
      cat = cat.upper()
      if cat == 'FOOD':
        wordset('WordLists/Hard/FoodHard.txt')
      elif cat == 'COLORS':
        wordset('WordLists/Hard/ColorsHard.txt')
      elif cat == 'option3':
        print("FIXME")

#END of difficulty function

def readfile(filename):  #READS FILE AND RETURNS LIST OF ALL WORDS
    with open(filename, 'r') as f:
        myText = f.read().splitlines()

    return myText


def xcheck(x):  #CHECKS GUESS FROM USER
    i = 0
    e = 0
    for item in word:  #Goes through array to find guess in chosen word
        if x == item:
            answer[e] = item
            i = i + 1
        e = e + 1
    if i != 0:
        return 1
    else:
        return 0


def gamebegin():  #MAIN GAME LOOP
    incorrect = 0
    while incorrect < 6:
      texts(str(6-incorrect))
      x = text()
      if xcheck(x) == 0:
          incorrect = incorrect + 1
      if wincheck() == 1:
          break
    if incorrect < 6:
      winEndgame()
    else:
      Gameover()


def texts(lives):
  pygame.font.init()
  font = pygame.font.Font("Sono.ttf", 20)
  text = font.render(str(answer), False, WHITE)
  text_rect = text.get_rect()
  text_rect.center = (220,200)
  life = font.render(str("Lives left:"+lives), False, WHITE)
  life_rect = text.get_rect()
  life_rect.center = (220,150)
  screen.fill(BLACK)
  screen.blit(text, text_rect)
  screen.blit(life, life_rect)
  pygame.display.update()


def wincheck():
  x=0
  y=0
  correct=0
  for i in word:
    if word[x] == answer[x]:
      y=y+1
    x=x+1
    correct=correct+1
  if correct == y:
    return 1
  else:
    return 0
 
  



    
  