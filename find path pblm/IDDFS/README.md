# IDDFS Maze Solver

## Description
This project implements the **Iterative Deepening Depth-First Search (IDDFS)** algorithm to solve maze puzzles. IDDFS is a combination of DFS and BFS that guarantees finding the shortest path with memory efficiency. The algorithm performs a depth-limited search, increasing the depth limit iteratively until the goal is found.

## Features
- Solves mazes using IDDFS.
- Memory-efficient compared to BFS.
- Finds the shortest path from start to goal.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iddfs-maze-solver.git
   cd iddfs-maze-solver
   
Usage
Prepare a maze:

The maze should be represented as a 2D grid:

1 represents walls.

0 represents open paths.

The start and goal points are represented by specific coordinates.

Run the IDDFS solver:

The Python script iddfs_solver.py contains the main logic.
You can run it from the terminal:

 git clone https://github.com/yourusername/iddfs-maze-solver.git
   cd iddfs-maze-solver
Results and Discussion
The IDDFS algorithm successfully finds the shortest path in most test cases, with the added benefit of being memory-efficient compared to BFS. However, the time complexity increases as the depth of the solution increases, due to the repeated exploration of nodes at each depth level. The algorithm performs better in terms of memory usage, as it avoids storing large amounts of nodes like BFS does. Despite the increased computational cost, IDDFS is a solid choice for solving mazes, especially when memory is a critical constraint.

Contributing
Contributions are welcome! If you have any improvements, bug fixes, or suggestions, feel free to open an issue or submit a pull request.

Fork the repository.

Create a new branch for your feature (git checkout -b feature-branch).

Make your changes and commit them (git commit -m "Add new feature").

Push to your forked repository (git push origin feature-branch).

Open a pull request to the main repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

### **How to Use This README**

1. **Copy the content above.**
2. **Go to your project directory** and create a new `README.md` file if it doesn't already exist, or edit the existing one.
3. **Paste the content** into the `README.md` file and save it.

This README provides all the necessary information for users and contributors to understand the project, set it up, and contribute effectively. Let me know if you'd like any further adjustments!


