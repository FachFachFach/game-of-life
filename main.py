"""
gol - John Conway's game of life

1. add documentation
"""




import pygame as pg
from sys import exit
from math import floor
from itertools import chain

# pygame initialization

#RGB colors
white = (255, 255, 255)
black = (0, 0, 0)

clock = pg.time.Clock()
tick = 4
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
		self.game_state = {}
		self.grid = self.get_grid()
		
		# initialize game_state dict
		for i in self.grid:
			self.game_state[i] = Cell(i[0], i[1], self)

		# initialize drawing board

	def get_grid(self):
	# in this case y is goes down (like -y)
		grid_list = [[(x,y) for x in range(self.num_cul)] for y in range(self.num_row)]
		# merging lists in coordinates_list(s)
		grid = list(chain.from_iterable(grid_list))

		return grid

	def update(self):
		l = []

		for i in self.game_state.keys():
			cell = self.game_state.get(i)
			live_neighbors = cell.get_neighbors()
			s = cell.state

			# cell update rules
			if s == 1:
				# underpopulation or overpopulation
				# cell dies
				if (live_neighbors < 2) or (live_neighbors > 3):
					l.append(cell)
				# stable
				elif (live_neighbors == 2) or (live_neighbors == 3):
					continue
				
			elif s == 0:
				# ressurect dead cell
				if live_neighbors == 3:
					l.append(cell)
			
		for i in l:
			i.update_state()
		
	


class Cell:
	def __init__(self, x, y, cls):
		self.x = x
		self.y = y
		self.state = 0
		self.game_state = cls.game_state
		# draw cell on the board
		self.rect = pg.draw.rect(gameDisplay, white, (cul_size*self.x, row_size*self.y, cul_size, row_size))

	def update_state(self):
		self.state = (self.state + 1) % 2 #ie. [0, 1] as possible states
		if self.state == 1:
		# fill with black
			color = black
	
		elif self.state == 0:
			# fill with white
			color = white

		gameDisplay.fill(color, self.rect) # color, surface
		#print('cell rect after filling with color:', (color,self.rect))

	@staticmethod
	def get_floor_pos(x,y):
		xf, yf = floor(x), floor(y)
		
		if x == xf:
			xf = x-1
		if y == yf:
			yf = y-1
	
		return xf,yf
	
	def get_neighbors(self):
		#print('x, y:', self.x,self.y)
		"""
		returns an integer representing the number of live neighbors around a cell.
		"""
		neighbors_list = [
		(self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1), # top row : top-left, top, top-right
		(self.x - 1, self.y), (self.x + 1, self.y), # mid row : right, left
		(self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y + 1)# bottom row : bottom-left, bottom, bottom-right
		]
		
		live_neighbors = 0

		for i in neighbors_list:
			value = self.game_state.get(i)
			if value == None:
				continue
			else:
				value = value.state
				if value == 1:
					live_neighbors += 1
		return live_neighbors



class Game:
	def __init__(self):
		self.board = Board(cul_size, row_size, num_cul, num_row)
		pg.init()
		self.game_intro()
		self.game_loop()

	def game_intro(self):
		running = True
		while running:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					running = False
					pg.quit()
					exit()
			
				if event.type == pg.MOUSEBUTTONUP:
					xmpos, ympos = pg.mouse.get_pos()
					print('clicked at :', (xmpos,ympos))

				# update game_state
					x, y = Cell.get_floor_pos(xmpos/cul_size, ympos/row_size)
					cell_obj = self.board.game_state.get((x,y))
					cell_obj.update_state()
			
				if event.type == pg.KEYUP:
					if event.key == pg.K_SPACE:
						running = False
						# move to the game loop
		
			pg.display.update()
			clock.tick(tick)


	def game_loop(self):
		running = True
		while running:
			
			for event in pg.event.get():        
				if event.type == pg.QUIT:
					running = False
					pg.quit()
					exit()
			
			self.board.update()
			pg.display.update()
			clock.tick(tick)


def main():
	game = Game()


if __name__ == '__main__':
	main()
