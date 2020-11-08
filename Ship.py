from Point import Point
from Exceptions import PlacementError
import random
class AbstractShip:
	# Override Static
	size = 0
	name = ''
	code = ''

	def __init__(self, start, end):
		self.points = []
		self.__set_points(start, end)
		self.is_sunk = False

	def hit_ship(self, target):
		total_points_hit = 0
		for point in self.points:
			if target == point:
				target.has_been_targeted = True
			if point.has_been_targeted:
				total_points_hit = total_points_hit + 1
				if total_points_hit == len(self.points):
					self.is_sunk = True
	
	# check size
	# Must insert left to right or top to bottom
	# Must not be diag
	# Delta must be size of ship
	def __set_points(self, start, end):
		is_horizontal = False
		is_vertical = False
		delta = 0

		if end.x > start.x:
			is_horizontal = True
			delta = end.x - start.x
		
		if end.y > start.y: 
			is_vertical = True
			delta = end.y - start.y
		
		if is_horizontal and is_vertical:
			raise PlacementError('Cannot place diagonally')

		if delta != self.size - 1:
			raise PlacementError('Incorrect size. Place from left to right or top to bottom')

		for i in range(self.size):
			x = start.x
			y = start.y
			if is_horizontal: 
				x = x + i
			else:
				y = y + i
			
			point = Point(x, y)
			point.ship = self
			self.points.append(point)

	@classmethod
	def get_random_ship(cls, board):
		# Get random bool

		start_cells = []
		start_index = None
		use_row = False

		while len(start_cells) == 0:
			use_row = bool(random.getrandbits(1))
			start_index = random.randint(0, 9)
			start_cells = cls.get_free_cells(board, use_row, start_index)

		start = random.choice(start_cells)
		end = start + cls.get_step()

		start_point = None
		end_point = None
		if use_row:
			start_point = Point(start_index, start)
			end_point = Point(start_index, end)
		else:
			start_point = Point(start, start_index)
			end_point = Point(end, start_index)	

		return cls(start_point, end_point)

	@classmethod
	def get_free_cells(cls, board, use_row, start_index):
		free_cells = []
		start_cells = []
		# Account for ship size and max init cols
		# WAY EASIER TO DO WITH FOR LOOPS IMO
		for end_index in range(0, 10 - cls.size):
			# if using row, set x to be invariant
			x = end_index
			y = start_index
			if use_row:
				x = start_index
				y = end_index

			point = board.get_point(x, y)
			if not point.ship:
				free_cells.append(end_index)

		for i in range(len(free_cells) - cls.get_step()):
			start = free_cells[i]
			end = free_cells[i + cls.get_step()]
			if((end - start) == cls.get_step()):
				start_cells.append(start)
		
		return start_cells
	
	@classmethod
	def get_step(cls):
		return cls.size - 1	

class Destroyer(AbstractShip):
	size = 2
	name = 'Destroyer'
	code = 'D'

class Submarine(AbstractShip):
	size = 3
	name = 'Submarine'
	code = 'S'

class Cruiser(AbstractShip):
	size = 3
	name = 'Cruiser'
	code = 'c'

class Battleship(AbstractShip):
	size = 4
	name = 'Battleship'
	code = 'B'

class Carrier(AbstractShip):
	size = 5
	name = 'Carrier'
	code = 'C'
