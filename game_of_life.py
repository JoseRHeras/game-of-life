import random
from typing import List
from xmlrpc.client import Boolean

class GameOfLife:

    def __init__(self, size:int = 10) -> None:
        self.size: int = size
        self._built_initial_setup()

    def _built_initial_setup(self) -> None:
        self.table: List = [['']*self.size for _ in range(self.size)]
        self._populate_initial_table()

    def _populate_initial_table(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                key = random.randint(0, 1)
                self.table[i][j] = 1 if key == 1 else 0
    
    def _evaluate_cell_for_live_neighbors(self, row:int, col:int) -> bool:
        # Cell survives if it has 2 or 3 live neighbors Return True
        # Cell dies if number of neighbors 2 > n ,  n > 3   Return False
        number_of_neightbors = self._count_number_of_neightbors(row=row, col=col)
        return True if number_of_neightbors == 2 or number_of_neightbors == 3 else False

    def _evaluate_cell_for_revival_conditions(self, row:int, col:int) -> bool:
        # Return True only if there are exactly three neighbors
        # Otherwise return False  
        return True if self._count_number_of_neightbors(row=row, col=col) == 3 else False

    def _count_number_of_neightbors(self, row:int, col:int) -> int:
        count = 0
        row_index = row - 1
        for _ in range(3):
            if row_index >= 0 and row_index < self.size:
                col_index = col - 1
                for _ in range(3):
                    if col_index >= 0 and col_index < self.size: 
                        if col_index != col or row_index != row:
                            count += 1 if self.table[row_index][col_index] == 1 else 0
                    col_index += 1
            row_index += 1
        
        return count

    def mutate_table_to_next_stage(self) -> None:
        new_stage_table = [[''] * self.size for _ in range(self.size)]

        for i in range(self.size):
            for j in range(self.size):
                if self.table[i][j] == 1:
                    new_stage_table[i][j] = 1 if self._evaluate_cell_for_live_neighbors(row=i, col=j) else 0
                else:
                    new_stage_table[i][j] = 1 if self._evaluate_cell_for_revival_conditions(row=i, col=j) else 0

        self.table = new_stage_table

    def get_table(self) -> List:
        return self.table

    
