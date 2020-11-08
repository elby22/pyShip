class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.is_hit = False
		self.ship = None

	def __str__(self):
		return str.format('{},{}', self.x, self.y)

	# def __hash__(self):
	# 	return hash(self.__str__)

	@staticmethod
	def from_terminal():
		line = input()
		line = line.split(',')
		x = int(line[0])
		y = int(line[1])

		return Point(x, y)

	