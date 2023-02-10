from tkinter import *
from tkinter.ttk import *
import pygame
from pygame import mixer
import sys
import os
import random

pygame.font.init()
pygame.display.init()
Blanc = (255, 255, 255)
color_light = (170,170,170)
color_dark = (100,100,100)

play_img = "play.png/"
pause_img = "pause.png/"

    

color = (255,255,255)

window = pygame.display.set_mode((600,100))

path = "Musique/"
file = os.path.join(path, random.choice(os.listdir(path)))
mixer.init()
mixer.music.load(file)
mixer.music.play()

width = window.get_width()
height = window.get_height()

smallfont = pygame.font.SysFont('Corbel',35)
text1 = smallfont.render('pause' , True , color)

text2 = smallfont.render('play' , True , color)

text3 = smallfont.render('précédent' , True, Blanc)

text4 = smallfont.render('suivant' , True, Blanc)  

pygame.display.update()
continuer = True
while continuer:
    
    
    for event in pygame.event.get():
        #window.blit(vibes_image, [100, 0])
        pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN:
                          
            if width/2 <= mouse[0] <= width/2+140 and height/3 <= mouse[1] <= height/2+40:
                mixer.music.pause()
            if width/6 <= mouse[0] <= width/4+160 and height/2 <= mouse[1] <= height/2+12:
                mixer.music.play()

            if width/2 <= mouse[0] <= width/2+240 and height/3 <= mouse[1] <= height/2+12:
                path = "Musique/"
                file = os.path.join(path, random.choice(os.listdir(path)))
                mixer.init()
                mixer.music.load(file)
                mixer.music.play()
            if width/2 <= mouse[0] <= width/160+2 and height/3 <= mouse[1] <= height/2+40:
                mixer.music.stop()    
                
                
                
                
                


    mouse = pygame.mouse.get_pos()
    
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(window,color_light,[width/2,height/2,140,40])

    else:
        pygame.draw.rect(window,color_dark,[width/2,height/2,140,40])
      
    # superimposing the text onto our button
    window.blit(text1 , (width/3+110,height/2))
      
    window.blit(text2 , (width/5+60,height/2))
    
    window.blit(text3 , (width/70+2,height/2))
    
    window.blit(text4 , (width/2+150,height/2))
    
    # updates the frames of the game
    pygame.display.update()