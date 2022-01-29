import tkinter as tk
from game_of_life import GameOfLife

FONT_SIZE = 10

class Board:

    def __init__(self, cells: int) -> None:
        self.game_of_life = GameOfLife()
        self.cells = cells
        self.screen_size = self.calculate_screen_size(cell_count=cells)
        self.initialize(self.screen_size)
        

    def initialize(self, size:str) -> None:
        self.root = tk.Tk()
        self.root.title("Conway Game of Life")
        self.root.geometry(size)
        self._draw_grid()

    def run_loop(self):
        self.root.mainloop()
    
    def calculate_screen_size(self, cell_count:int) -> str:
        height = cell_count * FONT_SIZE + (FONT_SIZE * 2)
        width = cell_count * FONT_SIZE + (FONT_SIZE * 2)
        
        print(f"{height}x{width}")
        return f"{height}x{width}"
        

    def _draw_grid(self):
        grid_frame = tk.Frame(master=self.root, background="grey")
        grid_frame.pack(fill=tk.BOTH, expand=True, padx=FONT_SIZE, pady=FONT_SIZE)
        self.root.update()


        for i in range(self.cells):
            for j in range(self.cells):
                frame = tk.Frame(
                    master=grid_frame
                )

                frame.grid(row=i, column=j)
                label = tk.Label(bg= "black" if j % 2 == 0 else "white", master=frame, width=1, height=1, font=("Arial", 5))
                label.pack()
                frame.update()
                print(label.winfo_height())



class Game:
    pass