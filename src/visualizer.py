from cgitb import text
from doctest import master
import tkinter as tk
from src.game_of_life import CellContainer


class Game:
    def __init__(self) -> None:
        self._initialize_graphical_window()
        self._build_widgets()

    def _initialize_graphical_window(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title(string="Conway's Game Of Life")
        self.root.config( padx=10, pady=5 )

    def _build_widgets(self) -> None:
        self.cell_container: CellContainer = CellContainer(master=self.root)
        self.control_bar: ControlBar = ControlBar(
            master=self.root, target=self.cell_container
        )

    def run(self) -> None:
        self.root.mainloop()


class ControlBar:
    def __init__(self, master: tk.Tk, target: CellContainer) -> None:
        self.master: tk.Tk = master
        self.target: CellContainer = target
        self._build_graphical_component()

    def _build_graphical_component(self) -> None:
        self.component_frame = tk.Frame(master=self.master)

        self.start_button = tk.Button(
            master=self.component_frame,
            text="Start Animation",
            command=self._start_animation,
        )
        self.stop_button = tk.Button(
            master=self.component_frame,
            text="Stop Animation",
            command=self._stop_animation,
            state=tk.DISABLED
        )

        self.reset_button = tk.Button(
            master=self.component_frame,
            text="Restart Animation",
            command=self._reset,
            state=tk.DISABLED
        )

        self.start_button.grid(row=1, column=1, padx=3)
        self.stop_button.grid(row=1, column=2, padx=3)
        self.reset_button.grid(row=1, column=3, padx=3)
        self.component_frame.pack(fill=tk.BOTH, expand=True, pady=7)

    def _start_animation(self) -> None:

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

        self.target.evolve_and_update_container()
        self.animation_id = self.component_frame.after(1500, self._start_animation)

    def _stop_animation(self) -> None:
        
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)

        self.component_frame.after_cancel(self.animation_id)

    def _reset(self) -> None:
        self.reset_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.target.reset_container()