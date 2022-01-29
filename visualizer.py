import tkinter as tk
from game_of_life import GameOfLife

FONT_SIZE = 10


class Board:

    def __init__(self, cells: int) -> None:
        self.game_of_life = GameOfLife()
        self.cells = cells
        self.screen_size = self.calculate_screen_size(cell_count=cells)
        self.initialize(self.screen_size)

    def initialize(self, size: str) -> None:
        self.root = tk.Tk()
        self.root.title("Conway Game of Life")
        self.root.geometry(size)
        self._draw_grid()

    def run_loop(self):
        self.root.mainloop()

    def calculate_screen_size(self, cell_count: int) -> str:
        height = cell_count * FONT_SIZE + (FONT_SIZE * 2)
        width = cell_count * FONT_SIZE + (FONT_SIZE * 2)

        print(f"{height}x{width}")
        return f"{height}x{width}"

    def _draw_grid(self):
        grid_frame = tk.Frame(master=self.root, background="grey")
        grid_frame.pack(fill=tk.BOTH,
                        expand=True,
                        padx=FONT_SIZE,
                        pady=FONT_SIZE)
        self.root.update()

        for i in range(self.cells):
            for j in range(self.cells):
                frame = tk.Frame(master=grid_frame)

                frame.grid(row=i, column=j)
                label = tk.Label(bg="black" if j % 2 == 0 else "white",
                                 master=frame,
                                 width=1,
                                 height=1,
                                 font=("Arial", 5))
                label.pack()
                frame.update()
                print(label.winfo_height())


class Game:

    def __init__(self) -> None:
        self._initialize_graphical_window()
        self._build_widgets()

    def _initialize_graphical_window(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title = "Conway Game Of Life"

    def _build_widgets(self) -> None:
        self.control_bar: ControlBar = ControlBar(master=self.root)

    def run(self) -> None:
        self.root.mainloop()


class ControlBar:

    def __init__(self, master: tk.Tk) -> None:
        self.master: tk.Tk = master
        self._build_graphical_component()

    def _build_graphical_component(self) -> None:
        component_frame = tk.Frame(master=self.master)

        start_button = tk.Button(master=component_frame,
                                 text="Start Animation",
                                 command=self._start_animation)
        stop_button = tk.Button(master=component_frame,
                                text="Stop Animation",
                                command=self._stop_animation)

        start_button.grid(row=1, column=1, padx=3, pady=2)
        stop_button.grid(row=1, column=2, padx=3, pady=2)
        component_frame.pack(fill=tk.BOTH, expand=True)
        

    def _start_animation(self) -> None:
        pass

    def _stop_animation(self) -> None:
        pass


class CellContainer:
    
    def __init__(self) -> None:
        pass

