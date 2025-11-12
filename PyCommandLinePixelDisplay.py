__version__ = "1.1.0"

import time
import os

class PyCommandLinePixelDisplay:
    def __init__(self, width: int, height: int, default_background_value: int = 0):
        self.width = width
        self.height = height
        self.screen = []
        self.levels = {0:"░░", 1:"██"}
        self.clear_type = "fallback"
        self.fallback_amount = 50
        self.pixel_separation = " "

        for i in range(self.height):
            current_row = []
            for j in range(self.width):
                current_row.append(default_background_value)
            self.screen.append(current_row)

    def set_levels(self, levels: dict):
        self.levels = levels

    def update_screen(self):
        self.clear_console(self.clear_type)
        for i in range(self.height):
            current_row = ""
            for j in range(self.width):
                try:
                    current_row += self.levels[self.screen[i][j]] + self.pixel_separation
                except KeyError:
                    print(f"error: Value at {j},{i} is {self.screen[i][j]}: which is not defined")
            print(current_row)

    def set_pixel(self, x: int, y: int, value):
        if isinstance(value, int):
            self.screen[y][x] = value
        elif isinstance(value, str):
            for k in range(len(self.levels)):
                if self.levels[k] == value:
                    self.screen[y][x] = k
                    return
            new_spot = len(self.levels)
            
            self.levels[new_spot] = value
            self.screen[y][x] = new_spot

    def get_pixel(self, x: int, y: int, return_in_int: bool = False):
        if return_in_int == True:
            return self.screen[y][x]
        else:
            return self.levels[self.screen[y][x]]

    def clear_main(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def clear_fallback(self, amount: int = 50):
        print("\n" * amount)

    def set_clear_type(self, type: str): # can use "main" or "fallback" without the quotes
        if type.lower() == "main":
            self.clear_type = "main"
        elif type.lower() == "fallback":
            self.clear_type = "fallback"
        else:
            print("Error: invalid clear type, can only use: main or fallback")

    def clear_console(self, type: str):
        if type.lower() == "main":
            self.clear_main()
        if type.lower() == "fallback":
            self.clear_fallback(self.fallback_amount)

    def set_fallback_line_amount(self, amount: int):
        if isinstance(amount, int):
            self.fallback_amount = amount
        else:
            print("Error: please enter integer for fallback line amount")

    def target_fps(self, fps: float = 10.0):
        time.sleep(1.0/fps)



