import tkinter as tk
from src.game_of_life_logic import GameOfLife


class GameVisualizer:
    
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
        self.game_of_life.discard_and_generate_table()
        self._populate_container()

    def evolve_and_update_container(self) -> None:
        self.game_of_life.mutate_table_to_next_stage()
        self._populate_container()

class ControlBar:
    def __init__(self, master: tk.Tk, target: GameVisualizer) -> None:
        self.master: tk.Tk = master
        self.target: GameVisualizer = target
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


