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
gray = (47, 79, 79)

clock = pg.time.Clock()
window_title = pg.display.set_caption('gol')
dw = 1000 # display width
dh = 1000 # display height

gameDisplay = pg.display.set_mode((dw, dh))


num_cul = 30
num_row = 30

cul_size = dw / num_cul
row_size = dh / num_row


class Board:
	def __init__(self, cul_size, row_size, num_cul, num_row):
		self.cul_size = cul_size
		self.row_size = row_size
		self.num_cul = num_cul
		self.num_row = num_row
		#game_state dictionary
		self.game_state = {}
		coordinates = self.get_coordinates()
		
		# initialize game_state dict
		for i in coordinates:
			self.game_state[i] = Cell(x, y)

		# initialize drawing board

	def get_coordinates(self):
	# in this case y is goes down (like -y)
		coordinates_list = [[(x,y) for x in range(self.num_cul)] for y in range(self.num_row)]
		# merging lists in coordinates_list(s)
		coordinates = list(chain.from_iterable(coordinates_list))

		return coordinates

	
	

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
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.state = 0
		# draw cell on the board


	def __repr__(self):
		pass


	def update(self):
		# normalize the points
		x, y = self.get_floor_pos(self.x/cul_size, self.y/row_size )
		# WTF DO I DO ABOUT THIS BOARD. ...
		value = .game_state.get((x,y))
		s, rect = , value[1]
		print(s)
		updated_state = (s + 1) % 2
		print('rect:', rect)
		if updated_state == 1:
		# fill with gray
			color = black

			#rect.fill(gray)
	@staticmethod
	def get_floor_pos(x,y):
		xf, yf = floor(x), floor(y)
		
		if x == xf:
			xf = x-1
		if y == yf:
			yf = y-1
	
		return xf,yf
	
	@classmethod
	def get_neighbors(cls, x, y):
		# game state
		gs = cls.game_state  
		"""
		return a list of lists of the neighbors of a given point
		"""
		
		neighbors_list = [
		gs(cul_size*(x - 1), row_size*(y + 1))[0], gs(cul_size*x, row_size*(y + 1))[0], gs(cul_size*(x + 1), row_size*(y + 1))[0], # up-left, up, up-right
		gs(cul_size*(x - 1), row_size*y)[0],                                                     gs(self.cul_size*(x + 1), self.row_size*(y))[0], # left,right
		gs(cul_size*(x - 1), row_size*(y-1))[0], gs(cul_size*x, row_size*(y-1))[0],    gs(cul_size*(x+1), row_size*(y-1))[0] # down-left, down, down-right
		]
		# for coordinate in coordinates: self.game_state.get(coordinate(s))
		print('neightbor list: ', neighbors_list)
		num_neighbors = 0
		for i in neighbors_list:
			if i == 1:
				num_neighbors += 1
		return num_neighbors
	
	
		elif updated_state == 0:
			# fill with white
			color = white
			#print('{} is white!'.format((x,y)))
			#rect.fill(white)


		cls.game_state[(x,y)] = (updated_state, rect)
		x = gameDisplay.fill(color, rect)
		print(x)
		print('created rect!: ', rect, color)

def board_setup():
	running = True
	
	for event in pg.event.get
def game_loop():
	running = True
	pg.init()
	board = Board(cul_size, row_size, num_cul, num_row)
	
	while running:
		#gameDisplay.fill(white)
		for event in pg.event.get():        
			if event.type == pg.QUIT:
				running = False
				pg.quit()
				exit()
			
			if event.type == pg.MOUSEBUTTONUP:
				
				xmpos, ympos = pg.mouse.get_pos()
				print('clicked at :', (xmpos,ympos))
				# call function to handle all this shit.
				board.draw(xmpos, ympos)
				
		
		#pg.update()

		pg.display.update()
		clock.tick(20)

	


if __name__ == '__main__':
	game_loop()
