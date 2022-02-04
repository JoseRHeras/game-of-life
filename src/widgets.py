import tkinter as tk
from src.game_of_life_logic import GameOfLife


class GameVisualizer:
    
    POPULATION_SIZE: dict = {"Small": 20, "Medium": 30, "Large": 50}

    def __init__(self, master: tk.Tk) -> None:
        self.master: tk.Tk = master
        self.cell_size: int = 20
        self.pop_size: int = self.POPULATION_SIZE["Small"]

        self._initialize_components()
        self._apply_configuration()
        self._draw_graph()

    def _initialize_components(self) -> None:
        self.game_of_life: GameOfLife = GameOfLife(size=self.pop_size)
        self.canvas: tk.Canvas = tk.Canvas(master=self.master, bg="white")
        self.canvas.pack()

    def _apply_configuration(self) -> None:
        self.game_of_life.update_size(size=self.pop_size)
        canvas_size = self.pop_size * self.cell_size
        self.canvas.config(width=canvas_size, height=canvas_size)
        

    def _draw_graph(self) -> None:
        self.canvas.delete("all")
        coordinate_y1, coordinate_y2 = 0, self.cell_size

        for row in range(self.pop_size):
            coordinate_x1, coordinate_x2 = 0, self.cell_size
            for col in range(self.pop_size):
                color = (
                    "Black" if self.game_of_life.is_cell_alive(row, col) else "White"
                )
                self.canvas.create_rectangle(
                    coordinate_x1,
                    coordinate_y1,
                    coordinate_x2,
                    coordinate_y2,
                    fill=color,
                )
                coordinate_x1 += self.cell_size
                coordinate_x2 += self.cell_size

            coordinate_y1 += self.cell_size
            coordinate_y2 += self.cell_size

    def reset_container(self) -> None:
        self.game_of_life.discard_and_generate_table()
        self._draw_graph()

    def evolve_and_update_container(self) -> None:
        self.game_of_life.mutate_table_to_next_stage()
        self._draw_graph()

    def update_population_size(self, size: str) -> None:
        self.pop_size = self.POPULATION_SIZE[size]
        self._apply_configuration()


class ControlBar:
    def __init__(self, master: tk.Tk, target: GameVisualizer) -> None:
        self.master: tk.Tk = master
        self.target: GameVisualizer = target
        self._build_graphical_component()

    def _build_graphical_component(self) -> None:
        self.component_frame = tk.Frame(master=self.master)

        self.start_button = self._create_button(command=self._start_animation, name="Start")
        self.stop_button = self._create_button(command=self._stop_animation, name="Stop", state=tk.DISABLED)
        self.reset_button = self._create_button(command=self._reset, name="Reset", state=tk.DISABLED)
        self.dropdown_menu = self._build_dropdown_menu(command=self._change_population_size)

        self._insert_components_to_grid(components=[self.start_button, self.stop_button, self.reset_button,self.dropdown_menu])
        self.component_frame.pack(fill=tk.BOTH, expand=True, pady=7)

    def _create_button(self,command, name:str, state=tk.NORMAL) -> tk.Button:
        return tk.Button(
            master=self.component_frame,
            text=name,
            command=command,
            state=state
        )
        
    def _build_dropdown_menu(self, command) -> None:
        available_sizes = list(self.target.POPULATION_SIZE.keys())

        dpm_variable = tk.StringVar(value=available_sizes[0])
        return tk.OptionMenu(
            self.component_frame,
            dpm_variable,
            *available_sizes,
            command=command
        )

    def _insert_components_to_grid(self, components: list) -> None:
        for col, element in enumerate(components):
            element.grid(row=1, column=col+1, padx=3)
           
    def _modify_button_state(self, start=None, stop=None, reset=None, dropmenu=None) -> None:
        if start != None: self.start_button.config(state=start)
        if stop != None: self.stop_button.config(state=stop)
        if reset != None: self.reset_button.config(state=reset)
        if dropmenu != None: self.dropdown_menu.config(state=dropmenu)

    def _change_population_size(self, variable: str) -> None:
        self.target.update_population_size(variable)
        self.target.reset_container()

    def _start_animation(self) -> None:
        self._modify_button_state(start=tk.DISABLED, stop=tk.NORMAL, reset=tk.DISABLED, dropmenu=tk.DISABLED)
        
        self.target.evolve_and_update_container()
        self.animation_id = self.component_frame.after(1500, self._start_animation)

    def _stop_animation(self) -> None:
        self._modify_button_state(stop=tk.DISABLED, start=tk.NORMAL, reset=tk.NORMAL, dropmenu=tk.NORMAL)
        self.component_frame.after_cancel(self.animation_id)

    def _reset(self) -> None:
        self._modify_button_state(reset=tk.DISABLED, start=tk.NORMAL)
        self.target.reset_container()
