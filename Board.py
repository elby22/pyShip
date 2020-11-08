from Exceptions import PlacementError
from Point import Point
class Board: 
	def __init__(self):
		self.ships = []
		self.moves = []
		self.target_map = set()
		self.grid = None
		self.grid_map = None
		self.__init_grid()
		

	# 10x10 matrix, origin top left
	def __init_grid(self):
		self.grid = []
		self.grid_map = set()
		for x in range(10):
			self.grid.insert(x, [])
			for y in range(10):
				point = Point(x, y)
				self.grid[x].insert(y, point)
				self.grid_map.add(point)

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

	def place_shot(self, x, y):
		point = self.get_point(x, y)
		if point.has_been_targeted:
			raise PlacementError('You cannot hit the same spot twice')
		
		move = Move(self, point)
		self.moves.append(move)
		self.target_map.add(point)

		return move

	def are_all_ships_sunk(self):
		for ship in self.ships:
			if not ship.is_sunk:
				return False
		return True
		
class Move:
	def __init__(self, grid, point):
		self.point = point
		self.is_hit = False
		self.is_sink = False
		self.point.has_been_targeted = True

		if point.ship:
			point.ship.hit_ship(point)
			self.is_hit = True
			if point.ship.is_sunk:
				self.is_sink = True

		self.is_win = grid.are_all_ships_sunk()
		
		
