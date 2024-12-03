#%%
import os

class DataFile():
    def __init__(self,day:int, dtype = True, path = None) -> None:
        if path is not None:
            self.path = f"../data/day{day}.txt"
        else:
            self.path = path

        self.dtype = dtype
        if os.path.exists(self.path):
            self.lines = self.parse()

    def parse(self):
        with open(self.path) as file:
            if self.dtype.isinstance(int):
                return [[int(var) for var in line.split()] for line in  file.readlines()]
            elif self.dtype.isinstance(str):
                return file.read()
            
# %%
