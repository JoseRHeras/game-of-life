import numpy as np

class GameOfLife:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.update_population_size: bool = True
        self._built_setup()
        

    def _built_setup(self) -> None:
        if self.update_population_size:
            self.population: np.array = np.zeros((self.size, self.size))

        self._populate_initial_table()
        self.update_population_size = False

    def _populate_initial_table(self) -> None:
        for row in range(self.size):
            for col in range(self.size):
                self.population[row, col] = 1 if np.random.randint(0, 2) == 1 else 0

    def _evaluate_cell_for_live_neighbors(self, row: int, col: int) -> bool:
        # Cell survives if it has 2 or 3 live neighbors Return True
        # Cell dies if number of neighbors 2 > n ,  n > 3   Return False
        number_of_neightbors = self._count_number_of_neightbors(row=row, col=col)
        return True if number_of_neightbors == 2 or number_of_neightbors == 3 else False

    def _evaluate_cell_for_revival_conditions(self, row: int, col: int) -> bool:
        # Return True only if there are exactly three neighbors
        # Otherwise return False
        return True if self._count_number_of_neightbors(row=row, col=col) == 3 else False

    def _count_number_of_neightbors(self, row: int, col: int) -> int:
        count = 0
        row_index = row - 1
        for _ in range(3):
            if row_index >= 0 and row_index < self.size:
                col_index = col - 1
                for _ in range(3):
                    if col_index >= 0 and col_index < self.size:
                        if col_index != col or row_index != row:
                            count += 1 if self.population[row_index, col_index] == 1 else 0
                            if count > 3: return count
                    col_index += 1 
            row_index += 1

        return count

    def mutate_table_to_next_stage(self) -> None:
        new_stage_table = np.zeros((self.size, self.size))

        for row in range(self.size):
            for col in range(self.size):
                if self.population[row, col] == 1:
                    new_stage_table[row, col] = (
                        1 if self._evaluate_cell_for_live_neighbors(row=row, col=col) else 0
                    )
                else:
                    new_stage_table[row, col] = (
                        1
                        if self._evaluate_cell_for_revival_conditions(row=row, col=col)
                        else 0
                    )

        self.population = new_stage_table

    def discard_and_generate_table(self) -> None:
        self._built_setup()

    def is_cell_alive(self, row: int, col: int) -> bool:
        return True if self.population[row, col] == 1 else False

    def update_size(self, size: int) -> None:
        print(size)
        self.size = size
        self.update_population_size = True

