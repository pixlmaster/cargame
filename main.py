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

def button(text,font,color1,color2,rectx,recty,rectw,recth,action=None):
	click= pygame.mouse.get_pressed()
	if mouse_display(rectx,recty,rectw,recth):
		pygame.draw.rect(gamedisplay,color2, (rectx,recty,rectw,recth))
		if click[0]==1:
			if action == "play":
				game_loop()
			elif action == "exit":
				pygame.quit()
				quit()

			
	else:
		pygame.draw.rect(gamedisplay, color1, (rectx,recty,rectw,recth))
	textsurf, textrect = text_objects(text,smalltext)
	textrect.center= (rectx + (rectw)/2, recty +(recth)/2)
	gamedisplay.blit(textsurf,textrect) 

def game_intro():
	intro =True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gamedisplay.fill(white)
		largetext= pygame.font.Font('freesansbold.ttf',115)
		textsurf,textrect= text_objects('A Bit Racey',largetext)
		textrect.center = (display_width/2),(display_height/2)		
		gamedisplay.blit(textsurf, textrect)

		button("GO!",smalltext,green,bright_green,125,400,200,100,"play")
		button("Exit",smalltext,red,bright_red,475,400,200,100,"exit")

		pygame.display.update()
		clock.tick(15)


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
		

		#crash condition
		if x<=0 or x>=display_width-car_width :
			crash()
		

		#when block passes bottom boundary
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx=random.randrange(0,display_width)
			dodged+=1
			if thing_speed<11:
				thing_speed+=1
			thing_width=random.randrange(100,300)
			thing_height=random.randrange(100,200)
			block_color = (random.randrange(0,200),random.randrange(0,200),random.randrange(0,200))
		

		# to prevent crashing when car is on top of block
		if y<thing_starty+ thing_height and thing_starty<y+car_height:
			if x +car_width> thing_startx and x<thing_startx+thing_width:
				crash()
		

		#update display
		pygame.display.update()

		clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()