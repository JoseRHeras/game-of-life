import random
import numpy as np
import tkinter as tk


class GameOfLife:
    def __init__(self, size: int = 10) -> None:
        self.size: int = size
        self._built_initial_setup()

    def _built_initial_setup(self) -> None:
        # self.table: List = [['']*self.size for _ in range(self.size)]
        self.table: np.array = np.zeros((self.size, self.size))
        self._populate_initial_table()

    def _populate_initial_table(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                key = random.randint(0, 1)
                self.table[i, j] = 1 if key == 1 else 0

    def _evaluate_cell_for_live_neighbors(self, row: int, col: int) -> bool:
        # Cell survives if it has 2 or 3 live neighbors Return True
        # Cell dies if number of neighbors 2 > n ,  n > 3   Return False
        number_of_neightbors = self._count_number_of_neightbors(row=row, col=col)
        return True if number_of_neightbors == 2 or number_of_neightbors == 3 else False

    def _evaluate_cell_for_revival_conditions(self, row: int, col: int) -> bool:
        # Return True only if there are exactly three neighbors
        # Otherwise return False
        return (
            True if self._count_number_of_neightbors(row=row, col=col) == 3 else False
        )

    def _count_number_of_neightbors(self, row: int, col: int) -> int:
        count = 0
        row_index = row - 1
        for _ in range(3):
            if row_index >= 0 and row_index < self.size:
                col_index = col - 1
                for _ in range(3):
                    if col_index >= 0 and col_index < self.size:
                        if col_index != col or row_index != row:
                            count += 1 if self.table[row_index, col_index] == 1 else 0
                    col_index += 1
            row_index += 1

        return count

    def mutate_table_to_next_stage(self) -> None:
        new_stage_table = np.zeros((self.size, self.size))

        for i in range(self.size):
            for j in range(self.size):
                if self.table[i, j] == 1:
                    new_stage_table[i, j] = (
                        1 if self._evaluate_cell_for_live_neighbors(row=i, col=j) else 0
                    )
                else:
                    new_stage_table[i, j] = (
                        1
                        if self._evaluate_cell_for_revival_conditions(row=i, col=j)
                        else 0
                    )

        self.table = new_stage_table

    def discard_table_and_generate_new_one(self) -> None:
        self._populate_initial_table()

    def is_cell_alive(self, row: int, col: int) -> bool:
        return True if self.table[row, col] == 1 else False

    def get_table(self) -> np.array:
        return self.table


class CellContainer:
    
    def __init__(self, master: tk.Tk) -> None:
        self.master: tk.Tk = master
        self.game_of_life: GameOfLife = GameOfLife(size=80)
        self._initialize_canvas()
        self._populate_container()


    def _initialize_canvas(self) -> None:
        self.cell_size = 10
        canvas_size = self.game_of_life.size * self.cell_size

        self.canvas = tk.Canvas(master=self.master, width=canvas_size, height=canvas_size, bg="white")
        self.canvas.pack()

    def _populate_container(self) -> None:
        self.canvas.delete("all")
        sample_size = self.game_of_life.size
        
        coordinate_y1, coordinate_y2 = 0, self.cell_size
         
        for row in range(sample_size):
            coordinate_x1, coordinate_x2 = 0, self.cell_size
            for col in range(sample_size):
                color = "Black" if self.game_of_life.is_cell_alive(row, col) else "White"
                self.canvas.create_rectangle(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2, fill=color)
                coordinate_x1 += self.cell_size
                coordinate_x2 += self.cell_size

            coordinate_y1 += self.cell_size
            coordinate_y2 += self.cell_size

    def reset_container(self) -> None:
        self.game_of_life.discard_table_and_generate_new_one()
        self._populate_container()

    def evolve_and_update_container(self) -> None:
        self.game_of_life.mutate_table_to_next_stage()
        self._populate_container()