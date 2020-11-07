class Board: 
	def __init__(self):
		self.ships: []
		self.moves: []
		self.__init_grid()

	# 10x10 matrix, origin top left
	def __init_grid(self):
		self.grid = []
		for row in range(10):
			cols = []
			for col in range(10):
				cols.insert(col, False)
			self.grid.insert(row, cols)

	def print_grid(self, hide_ships):
		# print 
		header = '  '
		for y in range(10):
			header = header + str.format('{} ', y)
		print(header)
		
		for x in range(10):
			row = str.format('{}', x)
			for y in range(10):
				cell = None
				if hide_ships:
					cell = '~' if self.grid[x][y] is False else 'X'
				# else

				row = row + str.format(' {}', cell)
			print(row)

	def get_ship(self, x, y):
		for ship in self.ships:
			for cell in ship.cells:
				if (cell.x == x and cell.y == y):
					return ship
				else:
					return None

	def is_hit(self, x, y):
		return self.grid[x][y]