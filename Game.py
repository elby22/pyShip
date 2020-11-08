from Board import Board
from Ship import Destroyer, Submarine, Cruiser, Battleship, Carrier 
from Point import Point
from Exceptions import PlacementError
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Game:

	def __init__(self):
		self.player_board = Board()
		self.ai_board = Board()
		self.Ship_Classes = [Destroyer, Submarine, Cruiser, Battleship, Carrier]


	def start(self, generate_player_board):
		if(generate_player_board):
			self.place_random_ships(self.player_board)
		else:
			self.prompt_player_for_ships()

		self.clear_terminal()
		print('Your board is set:')
		Game.print_board(self.player_board, True)

		print('AI is placing ships: ')
		self.place_random_ships(self.ai_board)
		print('It\'s ready to play!')

	def clear_terminal(self):
		print(chr(27) + "[2J")

	def prompt_player_for_ships(self):
		print('Place your ships:')

		for Ship_Class in self.Ship_Classes:
			is_valid = False
			
			while not is_valid:
				Game.print_board(self.player_board, True)

				prompt = str.format('{} ({}): takes up {} cells.', Ship_Class.name, Ship_Class.code, Ship_Class.size)
				print(prompt)
				start = Game.propt_for_point('Enter the starting position of the ship:')
				end = Game.propt_for_point('Enter the ending position of the ship:')
				
				try:
					new_ship = Ship_Class(start, end)
					self.player_board.place_ship(new_ship)
					is_valid = True

					self.clear_terminal()
				except PlacementError as error: 
					Game.print_error(str(error))

	@staticmethod
	def is_point_valid(point):
		x = point.x
		y = point.y
		if x < 0 or y < 0 or x > 9 or y > 9:
			return False
		else:
			return True

	@staticmethod
	def print_error(text):
		error = str.format('{}{}{}',bcolors.WARNING, text, bcolors.ENDC)
		print(error)

	@staticmethod
	def print_board(board, show_ships):
		header = '  '
		for y in range(10):
			header = header + str.format('{} ', y)
		print(bcolors.HEADER + header + bcolors.ENDC)
		
		for x in range(10):
			row = str.format(bcolors.HEADER + '{}' + bcolors.ENDC, x)
			for y in range(10):
				point = board.grid[x][y]
				cell = None
			
				if point.is_hit == True:
					if point.ship and show_ships:
						cell = 'X'
					else:
						cell = '.'
				else:
					if point.ship and show_ships:
						cell = point.ship.code
					else: 
						cell = '~'

				row = row + str.format(' {}', cell)
			print(row)

	@staticmethod
	def propt_for_point(prompt):
		while True:
			print()
			print(prompt)
			try:
				point = Point.from_terminal()
				if Game.is_point_valid(point):
					return point
				else:
					Game.print_error('Must be in bounds of board')
			except ValueError:
				Game.print_error('Point component must be integer')
			except IndexError: 
				Game.print_error('Where is your comma?')

	def place_random_ships(self, board):
		for Ship_Class in self.Ship_Classes:
			new_ship = Ship_Class.get_random_ship(board)
			board.place_ship(new_ship)
