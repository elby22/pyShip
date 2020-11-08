from Point import Point
from Exceptions import PlacementError
class AbstractShip:
	# Override Static
	size = 0
	name = ''
	code = ''

	def __init__(self, start, end):
		self.__set_points(start, end)
		self.is_sunk = False

	# This can obviously be done with some lin_alg
	def does_point_intersect(self, target):
		for point in self.points:
			if point.x == target.x and point.y == target.y:
				return True
		return False

	def does_ship_intersect(self, ship):
		for point in ship.points:
			if self.does_point_intersect(point):
				return True
		return False

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

		self.points = []

		for i in range(self.size):
			print(i)
			x = start.x
			y = start.y
			if is_horizontal: 
				x = x + i
			else:
				y = y + i
			
			point = Point(x, y)
			point.ship = self
			self.points.append(point)

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
