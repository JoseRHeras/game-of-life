import tkinter as tk
from game_of_life import CellContainer


class Game:

    def __init__(self) -> None:
        self._initialize_graphical_window()
        self._build_widgets()

    def _initialize_graphical_window(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title = "Conway Game Of Life"

    def _build_widgets(self) -> None:
        self.cell_container: CellContainer = CellContainer(master=self.root)
        self.control_bar: ControlBar = ControlBar(master=self.root, target=self.cell_container)

    def run(self) -> None:
        self.root.mainloop()


class ControlBar:

    def __init__(self, master: tk.Tk, target: CellContainer) -> None:
        self.master: tk.Tk = master
        self.target: CellContainer = target
        self._build_graphical_component()

    def _build_graphical_component(self) -> None:
        self.component_frame = tk.Frame(master=self.master)

        start_button = tk.Button(master=self.component_frame,
                                 text="Start Animation",
                                 command=self._start_animation)
        stop_button = tk.Button(master=self.component_frame,
                                text="Stop Animation",
                                command=self._stop_animation)

        start_button.grid(row=1, column=1, padx=3, pady=2)
        stop_button.grid(row=1, column=2, padx=3, pady=2)
        self.component_frame.pack(fill=tk.BOTH, expand=True)
        

    def _start_animation(self) -> None:
        self.target.evolve_and_update_container()
        self.animation_id = self.component_frame.after(500, self._start_animation)

    def _stop_animation(self) -> None:
        self.component_frame.after_cancel(self.animation_id)


