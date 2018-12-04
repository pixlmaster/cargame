import pygame
import time
import random

from constants import *
from functions import *

pygame.init()

def message_display(text):
	#displays a message
	largetext=pygame.font.Font('freesansbold.ttf',115)
	textsurf,textrect= text_objects(text,largetext)
	textrect.center = (display_width/2),(display_height/2)
	gamedisplay.blit(textsurf,textrect)

	pygame.display.update()

	time.sleep(2)

	game_loop()


def crash():
	#message on crashing
	message_display("You Crashed")

def game_loop():
	#starting variables
	x= (display_width * 0.45)
	y= (display_height*0.8)
	block_color = (random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))
	x_change=0
	thing_startx = random.randrange(0,display_width)
	thing_starty = -600
	thing_speed = 4
	thing_width = 100
	thing_height = 100

	dodged=0

	game_exit = False
	#game loop
	while not game_exit:
		#if user presses exit
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			#on pressing left or right key
			if(event.type == pygame.KEYDOWN):
				if event.key == pygame.K_LEFT:
					x_change=-10
				elif event.key ==pygame.K_RIGHT:
					x_change = 10
			#if key is not pressed
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x +=x_change
		gamedisplay.fill(white)
		things(thing_startx,thing_starty, thing_width, thing_height, block_color)
		thing_starty += thing_speed
		things_dodged(dodged)
		car(x,y)

		if x<=0 or x>=display_width-car_width :
			crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx=random.randrange(0,display_width)
			dodged+=1
			if thing_speed<11:
				thing_speed+=1
			thing_width=random.randrange(100,300)
			thing_height=random.randrange(100,200)
			block_color = (random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))

		if y<thing_starty+ thing_height and thing_starty<y+car_height:
			if x +car_width> thing_startx and x<thing_startx+thing_width:
				crash()

		pygame.display.update()

		clock.tick(60)
game_loop()
pygame.quit()
quit()