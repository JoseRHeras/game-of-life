import tkinter as tk
from src.widgets import GameVisualizer, ControlBar


class Game:
    def __init__(self) -> None:
        self._initialize_graphical_window()
        self._build_widgets()

    def _initialize_graphical_window(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title(string="Conway's Game Of Life")
        self.root.config( padx=10, pady=5 )

    def _build_widgets(self) -> None:
        self.cell_container: GameVisualizer = GameVisualizer(master=self.root)
        self.control_bar: ControlBar = ControlBar(
            master=self.root, target=self.cell_container
        )

    def run(self) -> None:
        self.root.mainloop()

