IDDFS Maze Solver
Description
This repository contains the implementation of the Iterative Deepening Depth-First Search (IDDFS) algorithm to solve maze puzzles. IDDFS is a hybrid of the Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms. It performs DFS with increasing depth limits until the solution is found, combining the memory efficiency of DFS with the optimality of BFS. This maze solver ensures the shortest path from a start point to a goal point in a given maze.

Features
Implements the IDDFS algorithm to solve mazes.

Supports a 2D grid representation of mazes with walls and open paths.

Finds the shortest path from the start position to the goal position.

Memory-efficient compared to BFS.

The algorithm guarantees finding the shortest path if one exists.

Objective
Implement IDDFS for maze solving.

Analyze the efficiency of IDDFS in comparison to DFS and BFS.

Find the shortest path from the start to the goal in various maze configurations.

Prerequisites
Python 3.x or higher.

Pygame library for visual representation (optional).

Any text editor or IDE to modify and run the Python script.

Installation
To use the IDDFS maze solver, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/iddfs-maze-solver.git
Navigate into the project directory:

bash
Copy
Edit
cd iddfs-maze-solver
Install the required libraries: You can install the required libraries using pip. If Pygame is used for visualization, you can install it with:

bash
Copy
Edit
pip install pygame
Usage
Prepare a maze:

The maze should be represented as a 2D grid, where:

1 represents walls.

0 represents open paths.

The starting point and goal are defined by specific coordinates.

Run the IDDFS solver:

The Python script iddfs_solver.py contains the main logic. Run it from the terminal:

bash
Copy
Edit
python iddfs_solver.py
Input:

The maze grid will be passed as input to the solver.

You can modify the maze grid in the script or input it dynamically.

Output:

The program will output the shortest path from the start to the goal if found.

If no solution exists, it will print a message indicating that the goal is unreachable.

Example
Here’s an example of how a simple maze might be represented:

python
Copy
Edit
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start = (0, 0)  # Starting point
goal = (4, 4)   # Goal point
The IDDFS algorithm will try to find the shortest path from (0, 0) to (4, 4).

Results and Discussion
The IDDFS algorithm guarantees finding the shortest path if a solution exists, while being memory-efficient compared to BFS.

However, its time complexity can be higher than BFS in certain cases, especially when the solution is deep in the maze, as IDDFS explores nodes multiple times.

It is effective for large mazes, where memory consumption is a concern, but can be slower than BFS for shallow solutions.

Contributing
Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or submit a pull request.

Fork the repository.

Create a new branch for your feature or fix.

Make your changes and commit them.

Push to your forked repository.

Open a pull request to the main repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.
