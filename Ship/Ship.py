class Ship:
	# Override Static
	size = 0
	name = ''
	code = ''

	def __init__(self, cells):
		self.cells = []
		self.is_sunk = False

	@staticmethod
	def can_insert(board, cells):
		# Must not overlap with other ships
		for cell in cells:
			if board.get_ship(cell['x'], cell['y']):
				return False
		
		return True

	# check size
	# Must insert left to right or top to bottom
	# Must not be diag
	# Delta must be size of ship
	@classmethod
	def get_cells(cls, x1, y1, x2, y2):
		is_horizontal = False
		is_vertical = False
		delta = 0
		cells = []

		if x2 > x1:
			is_horizontal = True
			delta = x2 - x1
		
		if y2 > y1: 
			is_vertical = True
			delta = y2 - y1
		
		if is_horizontal and is_vertical:
			print('Cannot place diagonally')
			return None

		if delta != cls.size - 1:
			print(cls.size)
			print(delta)
			print('Incorrect size. Place from left to right or top to bottom')
			return None

		if x1 < 0 or y1 < 0 or x2 > 9 or y2 > 9:
			print('Must be in bounds of board')

		x = x1 
		y = y1
		for i in range(cls.size):
			if is_horizontal: 
				x = x + i
			else:
				y = y + i

			cells.append({
				'x': x,
				'y': y
			})

		return cells
