import sys
import pygame

def run_game():
	#initialize game & create a screen object
	pygame.init()
	screen=pygame.display.set_mode((1366,768))
	pygame.display.set_caption("Alien Invasion")
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
	pygame.display.flip()
run_game()