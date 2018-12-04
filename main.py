import pygame
import time

pygame.init()

display_width =800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width=73

# resolution
gamedisplay = pygame.display.set_mode((display_width,display_height))
# change title name
pygame.display.set_caption('A bit Racey')
# in game clock
clock=pygame.time.Clock()
# not crashed

carimg = pygame.image.load('racecar.png')

def text_objects(text,font):
	textsurface=font.render(text,True,black)
	return textsurface,textsurface.get_rect()

def message_display(text):
	largetext=pygame.font.Font('freesansbold.ttf',115)
	textsurf,textrect= text_objects(text,largetext)
	textrect.center = (display_width/2),(display_height/2)
	gamedisplay.blit(textsurf,textrect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def car(x,y):
	gamedisplay.blit(carimg,(x,y))

def crash():
	message_display("You Crashed")

def game_loop():

	x= (display_width * 0.45)
	y= (display_height*0.8)

	x_change=0

	game_exit = False

	while not game_exit:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

			if(event.type == pygame.KEYDOWN):
				if event.key == pygame.K_LEFT:
					x_change=-5
				elif event.key ==pygame.K_RIGHT:
					x_change = 5

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x +=x_change
		gamedisplay.fill(white)
		car(x,y)

		if x<=0 or x>=display_width-car_width :
			crash()

		pygame.display.update()

		clock.tick(60)
game_loop()
pygame.quit()
quit()