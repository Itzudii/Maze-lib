# Maze Generator & Solver

A Python project that generates and solves mazes with a visual interface using Pygame. The maze is created using the Hunt-and-Kill algorithm and solved using a DFS-inspired approach.

### Features

- Generate random mazes of any size.

- Solve the maze automatically and visualize the solution.

- Display walls, paths, and solution routes with different colors.

- Fully interactive Pygame window showing generation and solving in real time.

### Installation

Clone the repository:

git clone <your-repo-url>
cd <repo-folder>

### Install dependencies:

pip install pygame
###  Usage
```
from MAZESOLVER import MAZE
import pygame

# Initialize pygame
pygame.init()

# Create a maze of size 20x20
maze = MAZE(20)

# Run the visualization
maze.run()
```
### Class Overview
### MAZE(column)

### Parameters:

column: Number of columns/rows in the maze (maze is square).

Main Methods:

create_maze(): Generates the maze and returns a dictionary representing walls.

solvemap(mapData): Solves the maze using the generated maze data. Returns a list of tuples representing the solution path.

run(): Starts the Pygame window, generates the maze, solves it, and visualizes it.

Visualization Colors:

Walls: Black

Current solving path: Red

Branch paths: Green

Final solution: Yellow

###  Example
```
from MAZESOLVER import MAZE
import pygame

pygame.init()
maze = MAZE(10)
data = maze.create_maze()
solution = maze.solvemap(data)

print(solution)

maze.run()
```
### Dependencies

- Python 3.x

- Pygame

### Notes

Maze size affects performance; very large mazes may slow down visualization.

The run() method creates a continuous Pygame loop; close the window to stop the program.
