from Exceptions import PlacementError
from Point import Point
class Board: 
	def __init__(self):
		self.ships = []
		self.moves = []
		self.__init_grid()

	# 10x10 matrix, origin top left
	def __init_grid(self):
		self.grid = []
		for x in range(10):
			self.grid.insert(x, [])
			for y in range(10):
				point = Point(x, y)
				self.grid[x].insert(y, point)

	def get_point(self, x, y):
		return self.grid[x][y]

	def place_ship(self, ship):
		for point in ship.points:
			board_point = self.get_point(point.x, point.y)
			if(board_point.ship):
				raise PlacementError('You cannot place a ship on top of another ship')

		for point in ship.points:
			self.grid[point.x][point.y] = point

		self.ships.append(ship)

