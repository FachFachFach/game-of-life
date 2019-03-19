"""
gol - John Conway's game of life


tasks:
1.split board class to a new board class and a cell class
1.5. try making cell.get_neighbors a class method
2.add the consequent of the game logic - ie. modification of the game state and such
3.create a drawing intro - watch the sentdex video of pygame car example
4. add documentation
5. write tests
"""




import pygame as pg
from sys import exit
from math import floor
from itertools import chain

#RGB colors
white = (255, 255, 255)
black = (0, 0, 0)

clock = pg.time.Clock()
tick = 20
window_title = pg.display.set_caption('gol')
dw = 1000 # display width
dh = 1000 # display height

gameDisplay = pg.display.set_mode((dw, dh))


num_cul = 40
num_row = 40

cul_size = dw / num_cul
row_size = dh/ num_row


class Board:
	def __init__(self, cul_size, row_size, num_cul, num_row):
		self.cul_size = cul_size
		self.row_size = row_size
		self.num_cul = num_cul
		self.num_row = num_row
		#game_state dictionary
		self.game_state = {}
		grid = self.get_grid()
		
		# initialize game_state dict
		for i in grid:
			self.game_state[i] = Cell(i[0], i[1], self)

		# initialize drawing board

	def get_grid(self):
	# in this case y is goes down (like -y)
		grid_list = [[(x,y) for x in range(self.num_cul)] for y in range(self.num_row)]
		# merging lists in coordinates_list(s)
		grid = list(chain.from_iterable(grid_list))

		return grid

	
	

	def save(self):
		# build a save/load seed prompt
		pass

	def update(self):

		# update rules
		# update the game state dictionary

		for i in self.game_state.keys():
			cell = self.game_state(i)
			live_neighbors = self.get_neighbors(i[0], i[1])
			print('number of neighbors: ', num_neighbors)
			
			# apply logic!

			# underpopulation
			if s == 1 and live_neighbors < 2:
				# the cell dies
				pass
			# stable
			elif s == 1 and ((live_neighbors == 2) or (live_neighbors == 3)):
				# leave the cell state unchanged
				pass
			# overpolpulation
			elif s == 1 and live_neighbors > 3:
				# cell dies
				pass

			elif s == 0 and live_neighbors == 3:
				# ressurect dead cell
				pass

		# update the self.game_state dictionary with the new values


class Cell:
	def __init__(self, x, y, cls):
		self.x = x
		self.y = y
		self.state = 0
		self.game_state = cls.game_state
		# draw cell on the board
		self.rect = pg.draw.rect(gameDisplay, white, (cul_size*x, row_size*y, cul_size, row_size))

	def update_state(self):
		# normalize the points
		#x, y = self.get_floor_pos(self.x/cul_size, self.y/row_size )
		# WTF DO I DO ABOUT THIS BOARD. ...
		self.state = (self.state + 1) % 2 #ie. [0, 1] as possible states
		if self.state == 1:
		# fill with gray
			color = black

			#rect.fill(gray)
	
		elif self.state == 0:
			# fill with white
			color = white
			#print('{} is white!'.format((x,y)))
			#rect.fill(white)

		gameDisplay.fill(color, self.rect) # color, surface
		print('cell rect after filling with color:', (color,self.rect))

	@staticmethod
	def get_floor_pos(x,y):
		xf, yf = floor(x), floor(y)
		
		if x == xf:
			xf = x-1
		if y == yf:
			yf = y-1
	
		return xf,yf

	# this method needs to be thought out compeletely, in addition to solving - 
	# the reference to the game_state(grid) dictionary
	@classmethod
	def get_neighbors(x, y):
		# game state
		gs = self.game_state
		"""
		return a list of lists of the neighbors of a given point
		"""
		
		neighbors_list = [
		gs(cul_size*(x - 1), row_size*(y + 1)).state, gs(cul_size*x, row_size*(y + 1)).state, gs(cul_size*(x + 1), row_size*(y + 1)).state, # up-left, up, up-right
		gs(cul_size*(x - 1), row_size*y).state,                                                     gs(self.cul_size*(x + 1), self.row_size*(y)).state, # left,right
		gs(cul_size*(x - 1), row_size*(y-1)).state, gs(cul_size*x, row_size*(y-1)).state,    gs(cul_size*(x+1), row_size*(y-1)).state # down-left, down, down-right
		]
		# for coordinate in coordinates: self.game_state.get(coordinate(s))
		print('neightbor list: ', neighbors_list)
		num_neighbors = 0
		for i in neighbors_list:
			if i == 1:
				num_neighbors += 1
		return num_neighbors
	





def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


def game_intro():
	intro = True
	#1. add the text rect thingy
	#2. add logic to when the rect thingy is clicked
	intro_board = Board(cul_size, row_size, num_cul, num_row)
	while intro:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				intro = False
				pg.quit()
				exit()
			
			if event.type == pg.MOUSEBUTTONUP:
				
				xmpos, ympos = pg.mouse.get_pos()
				print('clicked at :', (xmpos,ympos))

				# update game_state
				x, y = Cell.get_floor_pos(xmpos/cul_size, ympos/row_size)
				cell_obj = intro_board.game_state.get((x,y))
				cell_obj.update_state()
				
				# handle "starting" the game
		
		pg.display.update()
		clock.tick(tick)
	return intro_board


def game_loop(intro_board):
	board = intro_board
	running = True
	
	while running:
		#gameDisplay.fill(white)
		for event in pg.event.get():        
			if event.type == pg.QUIT:
				running = False
				pg.quit()
				exit()
			
			
		
		board.update()

		pg.display.update()
		clock.tick(tick)

	


if __name__ == '__main__':
	pg.init()
	intro_board = game_intro()
	game_loop(intro_board)
