import pygame, sys, math
from pygame.locals import *
from math import *



#constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS_CAP = 121
SQRT2 = sqrt(2)
WALL_WIDTH = 48
AREA_WIDTH = [ WINDOW_WIDTH - WALL_WIDTH, WINDOW_HEIGHT - WALL_WIDTH ]

#starting up the basics
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Swourcery a002")
global_clock = pygame.time.Clock()

#sprites
player_type = "ice_"
player_image_right = pygame.image.load("assets/" + player_type + "player_right.png").convert_alpha()
player_image_left = pygame.image.load("assets/" + player_type + "player_left.png").convert_alpha()
player_image_up = pygame.image.load("assets/" + player_type + "player_up.png").convert_alpha()
player_image_down = pygame.image.load("assets/" + player_type + "player_down.png").convert_alpha()
player_image_current = player_image_down

environ_dungeon = pygame.image.load("assets/environ_dungeon.png").convert()

player_position = \
	[ WINDOW_WIDTH / 2 - player_image_current.get_width() / 2, \
	  WINDOW_HEIGHT / 2 - player_image_current.get_height() / 2]
	 #position = middle of window
player_speed = 2
player_direction = 4
	#0 = straight up, 2 = straight right, 4 = straight down, 6 = straight left, other are transitions

def move_object (coords, speed, direction):
	#directs obj, assuming 4 sprite directions and 8 move directions.
	#remember that you can give a false direction and give "None" to the other args
	diag_speed = speed / SQRT2
	
	if direction == 0:
		use_sprite = "up"
		coords_delta = [0, -speed]
	elif direction == 1:
		use_sprite = "up"
		coords_delta = [diag_speed, -diag_speed]
	elif direction == 2:
		use_sprite = "right"
		coords_delta = [speed, 0]
	elif direction == 3:
		use_sprite = "right"
		coords_delta = [diag_speed, diag_speed]
	elif direction == 4:
		use_sprite = "down"
		coords_delta = [0, speed]
	elif direction == 5:
		use_sprite = "down"
		coords_delta = [-diag_speed, diag_speed]
	elif direction == 6:
		use_sprite = "left"
		coords_delta = [-speed, 0]
	elif direction == 7:
		use_sprite = "left"
		coords_delta = [-diag_speed, diag_speed]
	
	return [coords_delta, coords + coords_delta, use_sprite]
	
def will_collide(sprite_1, position_1, speed_1, sprite_2, position_2):
	#1 is moving, 2 is potential stop
	vert_collision = False
	hor_collision = False
	if position_1[0] + sprite_1.get_width() < position_2[0] - speed_1[0]:
		hor_collision = False
	else:
		hor_collision = True
	if position_1[0] > position_2[0] + sprite_2.get_width() + speed_1[0]:
		hor_collision = False
	else:
		hor_collision = True
	if position_1[1] + sprite_1.get_height() < position_2[1] - speed_1[1]:
		vert_collision = False
	else:
		vert_collision = True
	if position_1[1] > position_2[1] + sprite_2.get_height() + speed_1[1]:
		vert_collision = False
	else:
		vert_collision = True
		
	if hor_collision or vert_collision:
		return True
	else:
		return False
		

while True:
	for event in pygame.event.get():
		#quitting handler
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	keys = pygame.key.get_pressed()
	
	#process key inputs for movement
	
	DISPLAYSURF.blit(environ_dungeon, (0,0))
	DISPLAYSURF.blit(player_image_current, player_position)
	
	pygame.display.update()
	global_clock.tick(FPS_CAP)
