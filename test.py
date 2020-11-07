import Board
from Ship.Destroyer import Destroyer 

b = Board.Board()

# b.print_grid(True)

cells = Destroyer.get_cells(0, 0, 0, 1)
print(cells)
# Test ships
# print(b.grid)