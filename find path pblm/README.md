
Overview

This specific Python program generates a random N×N grid (where N is between 4 and 7) with a source and goal position. It then performs Depth-First Search (DFS) to find a path from the source to the goal and outputs the generated grid, source, goal, DFS path, and the topological order of node traversal.

**Features**

Random grid generation with obstacles (#) and walkable paths (.).

Random selection of source and goal ensuring they are not obstacles.

DFS implementation to find a path between source and goal.

Prints the grid, path found (if any), and node traversal order.

**Installation**

**Clone this repository:**

git clone https://github.com/your-username/dfs-grid-path.git
cd dfs-grid-path

Ensure you have Python installed (Python 3.6+ recommended).

Usage

**Run the script with:**

python dfs_grid_path.py

**Example Output**

Generated Grid:
. . # .
# . . #
. # . .
. . # .

Source: (0, 0)
Goal: (2, 3)

DFS Path:
[(0, 0), (1, 1), (2, 2), (2, 3)]

Topological Order of Node Traversal:
[(0, 0), (1, 1), (2, 2), (2, 3)]

**License**

This project is licensed under the MIT License.

**Contributing**

Feel free to fork the repository and submit pull requests for improvements!
