import pygame
import script
import gameCopy
import graphing
from graphing import *
import time
import os

def quizPage(screen, question, answer, explanation, buttonState):
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(400, 500, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    data = []
    errorMessage = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                elif (mouseX >= 450) and (mouseX <= 550) and (mouseY >= 575) and (mouseY <= 625):
                        buttonState += 1
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return(text)
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        
        screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 32)
        display_surface.fill(white)
        
        #header
        textScreen = font.render('Quiz!', True, black, white)
        textRect = textScreen.get_rect()
        textRect.center = (X // 2, 40)
        display_surface.blit(textScreen, textRect)

        font = pygame.font.Font('freesansbold.ttf', 16)
        
        #question
        textScreen = font.render(question, True, black, white)
        textRect = (20, 90)
        display_surface.blit(textScreen, textRect)

        #button
        button = pygame.draw.rect(display_surface,(150,220,150),(450, 575,100,50));
        buttonText = font.render('Check/Next', True, black, None)
        buttonTextRect = buttonText.get_rect()
        buttonTextRect.center = (X // 2, 600)
        display_surface.blit(buttonText, buttonTextRect)

        #answer
        if buttonState == 1:
            if (text.upper() != 'T') and (text.upper() != 'F'):
                errorMessage = True
                buttonState = 0
            else:
                errorMessage = False
                textScreen = font.render('Answer: '+answer, True, black, white)
                textRect = (20, 200)
                display_surface.blit(textScreen, textRect)
                textScreen = font.render('Explanation: '+explanation, True, black, white)
                textRect = (20, 400)
                display_surface.blit(textScreen, textRect)

        if errorMessage:
            textScreen = font.render('Answer must be in format \'T\' or \'F\'', True, black, white)
            textRect = (20, 300)
            display_surface.blit(textScreen, textRect)
        

        elif buttonState == 2:
            errorMessage = False
            return(text)
            
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

def homePage():
    font = pygame.font.Font('freesansbold.ttf', 32)
    display_surface.fill((64,224,208))
    
    #header as image
    titlePath = os.path.abspath("images/newLogo.png")
    titleImage = pygame.image.load(r''+titlePath)
    display_surface.blit(titleImage, ((X // 2) - (titleImage.get_width()//2), 50))

    #button
    font = pygame.font.Font('freesansbold.ttf', 20)
    start_button = pygame.draw.rect(display_surface,(90,250,235),(425, 550,150,50));
    start_text = font.render('Start Game', True, black, None)
    startTextRect = start_text.get_rect()
    startTextRect.center = (X // 2, 575)
    display_surface.blit(start_text, startTextRect)

    #image
    stonkPath = os.path.abspath("images/stonkGuy.jpg")
    stonkImage = pygame.image.load(r''+stonkPath)
    display_surface.blit(stonkImage, ((X // 2) - (stonkImage.get_width()//2), 150))

    #image
    corp = os.path.abspath("images/corpSmall.png")
    corpPic = pygame.image.load(r''+corp)
    display_surface.blit(corpPic, ((50, 650)))

def quizSummaryPage(score):
    start_time = time.time()
    seconds = 4

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        font = pygame.font.Font('freesansbold.ttf', 32)
        display_surface.fill(white)
            
        #header
        textScreen = font.render('Quiz Summary', True, black, white)
        textRect = textScreen.get_rect()
        textRect.center = (X // 2, 40)
        display_surface.blit(textScreen, textRect)

        #question
        font = pygame.font.Font('freesansbold.ttf', 16)  
        textScreen = font.render("Your score is: "+str(score)+"/15", True, black, white)
        textRect = (80, 90)
        display_surface.blit(textScreen, textRect)

        pygame.display.update()
        
        if elapsed_time > seconds:
            graphing.main()

def gameLoop(X, Y):
    homePageStatus = True
    quizPageStatus = False
    stockPageStatus = False
    question = ['1. Compound interest earns more exponentially over time (T/F)'
                ,'2. Growth stocks are more safe investment than blue chip stocks (T/F)?'
                ,'3. You can open a TFSA at age 16 (T/F)?'
                ,'4. The TFSA contribution limit for 2020 is $6000 (T/F)?'
                ,'5. A dividend is paid by the stock market (T/F)?'
                ,'6. A dividend yield is the percent of the anual dividend price per share in comparison to the share price (T/F)?'
                ,'7. P/E ratio helps to determine whether a company is over or undervalued (T/F)?'
                ,'8. Blue chip stocks are considered a risky investment (T/F)?'
                ,'9. Beginning to invest earlier in your life can allow you to retire wealthy (T/F)?'
                ,'10. Buying a stock in a company is equivalent to buying equity in it (T/F)?'
                ,'11. An exchange-traded fund allows you to buy individual companies (T/F)?'
                ,'12. Stocks only go up (T/F)?'
                ,'13. Long term inverstors shouldn\'t worry about the one poor performance day (T/F)?'
                ,'14. Invest in markets that use your country\'s currency as this will avoid foreign exchange fees (T/F)?'
                ,'15. You can open up a TFSA at most financial institutions such as RBC, Scotia Bank and Sun Life Financial (T/F)?']
    explanation = ['Compound interest builds ontop of itself causing an exponential increase.'
                   ,'Growth stocks are more risky as they don\'t have the retutation and dividends like blue chip stocks.'
                   ,'You must 18 or older to open a TFSA.'
                   ,'The TFSA contribution limit for 2020 is $6000'
                   ,'A dividend is paid by the company issuing the it, as they are sharing a percentage of the profits with you.'
                   ,'A dividend yield is ((annual dividends per share) / (current share price)) x100.'
                   ,'P/E rations can be used to compare companies and determine their relative values.'
                   ,'Blue chip stocks are considered relatively safe as they have a reputation of operation mied conditions.'
                   ,'The sooner you start investing the greater the effect of compound interest.'
                   ,'When you buy a stock, you are technically buying equity in the company.'
                   ,'An ETF allows only allows you to buy baskets of companies that are related by industry or common attribute.'
                   ,'Stocks and go up, down and to zero. Stocks are a gamble as you can never certainly predict the future.'
                   ,'One bad day in the scope of a decade means nothing to a long term investor.'
                   ,'By investing in your country\'s stock market you do not have to convert the currency when you withdraw it.'
                   ,'Almost every financial institutio offers TFSAs which you can open a self direct investing accoun in.']
    answer = ['T','F','F','T','F','T','T','F','T','T','F','F','T','T','T']
    questionNumber = 0
    buttonState = 0
    score = 0
    #game loop
    while True :
        if homePageStatus:
            homePage()

        elif animePageStatus:
            gameCopy.main()
            quizPageStatus = True
            animePageStatus = False
            homePageStatus = False

        elif quizPageStatus:
            text = quizPage(display_surface, question[questionNumber], answer[questionNumber], explanation[questionNumber], buttonState)
            if(text.upper()==answer[questionNumber]):
                score += 1
                if questionNumber >= 14:
                    quizSummaryPage(score)
                    quizPageStatus = False
                    animePageStatus = False
                    homePageStatus = False
            
            questionNumber += 1
            buttonState = 0
        
        # iterate over the list of Event objects that was returned by pygame.event.get() method. 
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN:
                #events for homePage
                if homePageStatus:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    if (mouseX >= 425) and (mouseX <= 575) and (mouseY >= 550) and (mouseY <= 600):
                        quizPageStatus = False
                        animePageStatus = True
                        homePageStatus = False
                    

            # if event object type is QUIT then quitting the pygame and program both. 
            if event.type == pygame.QUIT : 
              
                # deactivates the pygame library 
                pygame.quit() 
      
                # quit the program. 
                quit() 
      
            # Draws the surface object to the screen.   
            pygame.display.update()
            
pygame.init()
pygame.display.set_caption('Stock Simulator')
#colours
white = (255, 255, 255) 
green = (0, 255, 0)
black = (0, 0, 0)
blue = (0, 0, 128) 
# display dimensions
X = 1000
Y = 700
display_surface = pygame.display.set_mode((X, Y ))
gameLoop(X, Y)
