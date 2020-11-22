import pygame
import textwrap
import os
from script import *

#from pygame.locals import *
display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
navy = (13, 8, 79)
pink = (255,192,203)

gameDisplay = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('')

counter = 0
quitting = False

from itertools import chain

stonk_pics = [os.path.abspath("images/stonks.png"), os.path.abspath("images/stonks2.png"), os.path.abspath("images/stonks3.png")]
cat_pics = [os.path.abspath("images/cat.png"), os.path.abspath("images/cat2.png"), os.path.abspath("images/cat3.png")]
educate = False
intro = True

def stonks_talk(counter):
    gameDisplay.fill(white)
    if(counter == 2):
        stonks = pygame.image.load(os.path.abspath(stonk_pics[1]))
    elif(counter == 3):
        stonks = pygame.image.load(os.path.abspath(stonk_pics[1]))
    elif(counter == 5):
        stonks = pygame.image.load(os.path.abspath(stonk_pics[2]))
    elif(counter == 7):
        stonks = pygame.image.load(os.path.abspath(stonk_pics[1]))
    elif(counter == 11):
        stonks = pygame.image.load(os.path.abspath(stonk_pics[1]))
    else:
       stonks = pygame.image.load(os.path.abspath(stonk_pics[0])) 
        
    stonks = pygame.transform.scale(stonks, (500, 500))
    gameDisplay.blit(stonks, (-50, 200))
    textArr = []
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    if(isinstance(stonks_script[counter], list)):
        for i in range(len(stonks_script[counter])):
           textArr.append(font.render(stonks_script[counter][i], True, black))
    else:
        text = font.render(stonks_script[counter], True, black)
        gameDisplay.blit(text, (400, 300))

    for i in range(len(textArr)):
        gameDisplay.blit(textArr[i], (400, 300+(i*30)))
    pygame.display.flip()

def stonks_talk_board(counter):
    gameDisplay.fill(white)

    if(counter == 3 or counter == 6 or counter == 9 or counter == 17 or counter == 21 or  counter == 5):
        stonks = pygame.image.load(os.path.abspath(stonk_pics[1]))
    elif(counter == 11 or counter == 15 or counter == 22):
        stonks = pygame.image.load(os.path.abspath(stonk_pics[2]))
    else:
        stonks = pygame.image.load(os.path.abspath(stonk_pics[0]))

    board = pygame.image.load(os.path.abspath("images/blackboard.png"))
    board = pygame.transform.scale(board, (600, 850))
    gameDisplay.blit(board, (350, -100))

    stonks = pygame.transform.scale(stonks, (500, 500))
    gameDisplay.blit(stonks, (-50, 200))
    textArr = []
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    if(isinstance(stonks_second_script[counter], list)):
        for i in range(len(stonks_second_script[counter])):
           textArr.append(font.render(stonks_second_script[counter][i], True, white))
    else:
        text = font.render(stonks_second_script[counter], True, white)
        gameDisplay.blit(text, (400, 150))

    for i in range(len(textArr)):
        gameDisplay.blit(textArr[i], (400, 150+(i*30)))
    pygame.display.flip()

def cat_talk(counter):
    gameDisplay.fill(white)
    if(counter == 0):
        stonks = pygame.image.load(stonk_pics[1])
        cat = pygame.image.load(cat_pics[1])
    elif(counter == 1):
        cat = pygame.image.load(cat_pics[2])
        stonks = pygame.image.load(stonk_pics[0])
    elif(counter == 3):
        stonks = pygame.image.load(stonk_pics[2])
        cat = pygame.image.load(cat_pics[0])
    else:
       stonks = pygame.image.load(stonk_pics[0])
       cat = pygame.image.load(cat_pics[0])
        
    stonks = pygame.transform.scale(stonks, (500, 500))
    gameDisplay.blit(stonks, (-50, 200))
    
    cat = pygame.transform.scale(cat, (500, 500))
    gameDisplay.blit(cat, (500, 200))
    textArr = []
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    if(isinstance(cat_script[counter], list)):
        for i in range(len(cat_script[counter])):
           textArr.append(font.render(cat_script[counter][i], True, navy))
    else:
        text = font.render(cat_script[counter], True, navy)
        gameDisplay.blit(text, (400, 300))

    for i in range(len(textArr)):
        gameDisplay.blit(textArr[i], (400, 300+(i*30)))
    pygame.display.flip()

def cat_talk_board(counter):
    gameDisplay.fill(white)
    stonks = pygame.image.load(stonk_pics[0])
    cat = pygame.image.load(cat_pics[0])
       
    board = pygame.image.load(os.path.abspath("images/blackboard.png"))
    board = pygame.transform.scale(board, (600, 850))
    gameDisplay.blit(board, (350, -100))
        
    stonks = pygame.transform.scale(stonks, (500, 500))
    gameDisplay.blit(stonks, (-50, 200))
    
    cat = pygame.transform.scale(cat, (500, 500))
    gameDisplay.blit(cat, (650, 375))
    textArr = []
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    if(isinstance(cat_script_two[counter], list)):
        for i in range(len(cat_script_two[counter])):
            if(counter == 1):
               textArr.append(font.render(cat_script_two[counter][i], True, pink))
            else:
                textArr.append(font.render(cat_script_two[counter][i], True, navy))
    else:
        text = font.render(cat_script_two[counter], True, navy)
        gameDisplay.blit(text, (400, 580))

    if(counter == 1):
        for i in range(len(textArr)):
            gameDisplay.blit(textArr[i], (400, 150+(i*30)))
    else:
        for i in range(len(textArr)):
            gameDisplay.blit(textArr[i], (400, 580+(i*30)))
    pygame.display.flip()

def slide():
    stonks = pygame.image.load(stonk_pics[0])
    stonks = pygame.transform.scale(stonks, (500, 500))
    gameDisplay.blit(stonks, (-50, 200))
    
    fpsClock = pygame.time.Clock()
    imageX= -50; # x coordnate of image
    imageY= 200; # y coordinate of image
    running = True
    
    while(imageX < 1200):
        imageX += 20 ;
        gameDisplay.fill(white) # clear screen 
        gameDisplay.blit(stonks , (imageX, imageY) ) # paint to screen
    
        pygame.display.update()
        fpsClock.tick(20)
    quitting = True

def education(counter):
    gameDisplay.fill(white)
    board = pygame.image.load(os.path.abspath("images/blackboard.png"))
    board = pygame.transform.scale(board, (600, 850))
    gameDisplay.blit(board, (350, -100))
    
    stonks = pygame.image.load(stonk_pics[0])
    stonks = pygame.transform.scale(stonks, (500, 500))
    gameDisplay.blit(stonks, (-50, 200))

    stonks_talk_board(counter)

    pygame.display.update()
    
def main():
    quitting = False
    intro = True
    educate = False
    scounter = 0
    ccounter = 0
    ecounter = 0
    icounter = 0
    stonks_talk(counter)
    run = True
    while run:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if(intro):
                        if(ccounter == 0):
                            cat_talk(ccounter)
                            ccounter = ccounter + 1
                            scounter = 1
                        elif(scounter == 0 or scounter == 1 or scounter == 2 or scounter == 3):
                            stonks_talk(scounter)
                            scounter = scounter + 1
                        elif(ccounter == 1):
                            cat_talk(ccounter)
                            ccounter = ccounter + 1
                        elif(scounter == 3 or scounter == 4 or scounter == 5 or scounter == 6 or scounter == 7 or scounter == 8):
                            stonks_talk(scounter)
                            scounter = scounter + 1
                        elif(ccounter == 2):
                            cat_talk(ccounter)
                            ccounter = ccounter + 1
                        elif(scounter == 9):
                            stonks_talk(scounter)
                            scounter = scounter + 1
                        elif(ccounter == 3):
                            cat_talk(ccounter)
                            ccounter = ccounter + 1
                        elif((scounter == 10) or (scounter == 11)):
                            stonks_talk(scounter)
                            scounter = scounter + 1
                        else:
                            slide()
                            intro = False
                            educate = True
                    if(educate):
                        if(ecounter == 15 or ecounter == 16):
                            cat_talk_board(icounter)
                            icounter += 1
                        elif ecounter==23:
                            run=False
                        else:
                            education(ecounter)
                        ecounter += 1
