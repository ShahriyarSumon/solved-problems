# IDDFS Maze Solver

## Description
This Python program implements the **Iterative Deepening Depth-First Search (IDDFS)** algorithm to determine whether a valid path exists in a 2D maze. The maze consists of empty spaces (0) and walls (1). The user provides input for the maze structure, starting position, and target position. The program attempts to find a path within a maximum depth of 6.

## Features
- Uses IDDFS to explore paths efficiently
- Accepts user input for maze size and layout
- Finds and displays the traversal order if a path exists
- Stops searching when the maximum depth of 6 is reached

## How to Run
1. Ensure you have Python installed (Python 3 recommended).
2. Copy the script and save it as `iddfs_maze_solver.py`.
3. Run the script using:
   ```bash
   python iddfs_maze_solver.py
   ```
4. Provide the input in the following format:
   ```
   4 4  # Number of rows and columns
   0 0 1 0
   1 0 1 0
   0 0 0 0
   1 1 0 1
   Enter start position (row col): 0 0
   Enter target position (row col): 2 3
   ```

## Example Output
### Case 1 (Path Found)
**Input:**
```
4 4
0 0 1 0
1 0 1 0
0 0 0 0
1 1 0 1
Start: 0 0
Target: 2 3
```
**Output:**
```
Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (1,0), (1,1), (0,1), (2,1), (2,2), (2,3)]
```

### Case 2 (No Path Found)
**Input:**
```
3 3
0 1 0
0 1 0
0 1 0
Start: 0 0
Target: 2 2
```
**Output:**
```
Path not found at max depth 6 using IDDFS
```

## Contributions
Feel free to contribute by modifying the depth limit, improving the algorithm, or optimizing memory usage. Pull requests are welcome!

## License
This project is open-source and available under the MIT License.
