import pygame
import time
import random
from constants import *

# resolution
gamedisplay = pygame.display.set_mode((display_width,display_height))
# change title name
pygame.display.set_caption('A bit Racey')
# in game clock
clock=pygame.time.Clock()
#load image of car
carimg = pygame.image.load('racecar.png')

def things_dodged(count):
	#displays dodge count
	font = pygame.font.SysFont(None, 25)
	text= font.render("Dodged: "+str(count), True, black)
	gamedisplay.blit(text,(0,0))


def things(thingx,thingy,thingw, thingh, color):
	#draw rectangle
	#thingx, thingy = (x,y)
	pygame.draw.rect(gamedisplay,color ,[thingx, thingy,thingw,thingh])

def text_objects(text,font):
	#renders text with particular font and returns it
	textsurface=font.render(text,True,black)
	return textsurface,textsurface.get_rect()

def car(x,y):
	#display car on screen
	gamedisplay.blit(carimg,(x,y))

def crash():
	#message on crashing
	message_display("You Crashed")