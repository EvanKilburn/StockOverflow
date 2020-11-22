import numpy as np
import matplotlib
import pygame
from pygame.locals import *

matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
import pylab

#global variables
app_close = []
app_date = []
x = []
white = (255,255,255) #background colour
black = (0, 0, 0)
ticker = ""
        
#GETTING DATA
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def straight_line(x, y):
    w, b = np.polyfit(x, y, deg=1)
    line = w*x + b
    return line

def textbox(screen):
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(200, 500, 140, 32)
    color_inactive = pygame.Color('black')
    color_active = pygame.Color('black')
    color = color_inactive
    active = False
    text = ''
    done = False
    data = []

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        test = get_data(screen, text)
                        if(isinstance(test, str)):
                            print("")
                        else:
                            data = get_data(screen, text)
                        tickerTitle = font.render("ticker is: "+text, True, black)
                        screen.blit(tickerTitle, (450, 40))
                        #text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(white)
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        label = font.render("Enter a stock ticker: ", True, black)
        screen.blit(label, (200, 440))
        title = font.render("Stock Analysis", True, black)
        screen.blit(title, (350, 30))
        
        if(data != []):
            plot_graph(screen, data[0], data[1])

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


def get_data(screen, text):
        url = ("https://financialmodelingprep.com/api/v3/historical-price-full/" + text + "?serietype=line&apikey=2618eafe6f83519eb9c6b013dcfc46c1")
        apple_dict = get_jsonparsed_data(url)

        if(apple_dict == { }):
            return "Please enter a valid stock ticker!"
        
        app_close.clear()
        app_date.clear()

        for i in range(365):
            app_close.append(apple_dict["historical"][365-i]["close"])
            app_date.append(apple_dict["historical"][365-i]["date"])
    
        y = np.array(app_close)
        x = np.arange(y.shape[0])
        return x, y, text

    

def plot_graph(screen, x, y):
    #GRAPHING DATA
    graph_size = 150
    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", 
              "Aug", "Sept", "Oct", "Nov", "Dec"]
    x_axis = [350, 300, 250, 200, 150, 100, 50, 0]

    line =  straight_line(x, y)
    fig = pylab.figure(figsize=[6, 2],dpi=graph_size)
    ax = fig.gca()
    ax.plot(y, color = 'darkblue', 
           alpha = 0.3) #data points entered
    
    ax.plot(x, line, 'r--')
    
    ax.set(title = ticker,
           xlabel = "Month",
           ylabel = "Close Price")

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    
    size = canvas.get_width_height()

    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (50, 100))

def main():
    window = pygame.display.set_mode((1000, 700), DOUBLEBUF)
    window.fill(white)
    screen = pygame.display.get_surface()
    
    textbox(screen)

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Enter a stock ticker: ", True, black)
    gameDisplay.blit(text, (200, 440))
    title = font.render("Stock Analysis", True, black)
    screen.blit(title, (350, 30))
    

    pygame.display.flip()
    crashed = False

    while not crashed:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            crashed = True

