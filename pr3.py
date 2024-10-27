import numpy as np
import matplotlib.pyplot as plt
import random
import os
import sys
import matplotlib  

n = 50  
blue_ratio = 0.45  
red_ratio = 0.45   
empty_ratio = 0.1  
num_steps = 10  

def initialize_grid(n, blue_ratio, red_ratio, empty_ratio):
    grid = np.random.choice([0, 1, 2], size=(n, n), p=[empty_ratio, blue_ratio, red_ratio])
    return grid

def is_happy(grid, x, y):
    if grid[x, y] == 0:
        return True
    color = grid[x, y]
    neighbors = [
        grid[i % n, j % n]
        for i in range(x - 1, x + 2)
        for j in range(y - 1, y + 2)
        if (i != x or j != y) and (0 <= i < n) and (0 <= j < n)
    ]
    return neighbors.count(color) >= 2

def step(grid):
    unhappy = [(i, j) for i in range(n) for j in range(n) if grid[i, j] != 0 and not is_happy(grid, i, j)]
    empty_cells = [(i, j) for i in range(n) for j in range(n) if grid[i, j] == 0]
    
    random.shuffle(unhappy)
    
    for (i, j) in unhappy:
        if empty_cells:
            new_pos = random.choice(empty_cells)
            empty_cells.remove(new_pos)
            grid[new_pos], grid[i, j] = grid[i, j], 0

def plot_grid(grid, step_num):
    plt.imshow(grid, cmap='bwr', interpolation='nearest')
    plt.title(f'Шаг {step_num}')
    plt.axis('off')
    plt.show()

def run_simulation(num_steps):
    grid = initialize_grid(n, blue_ratio, red_ratio, empty_ratio)
    for step_num in range(num_steps):
        plot_grid(grid, step_num)
        step(grid)

def is_running_in_colab():
    try:
        import google.colab
        return True
    except ImportError:
        return False

if is_running_in_colab():
    matplotlib.use('module://matplotlib_inline.backend_inline')
else:
    if os.environ.get('DISPLAY') is None and sys.platform != 'win32':
        matplotlib.use('Agg')  
    else:
        try:
            import PyQt5
            matplotlib.use('Qt5Agg')  
        except ImportError:
            matplotlib.use('TkAgg')  

if __name__ == "__main__":
    run_simulation(num_steps)
