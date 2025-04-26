Modified K-Means Clustering (Manhattan Distance)
This project is a simple Python implementation of a modified K-Means clustering algorithm where the Manhattan distance is used instead of the traditional Euclidean distance.
It also includes a basic 2D matrix visualization using only the print() function.

Features
Random generation of 100 data points and 10 initial cluster centers.

Clustering based on Manhattan distance (|x1 - x2| + |y1 - y2|).

Iterative center updates (fixed number of iterations).

Visualization of the final clusters in a 21x21 grid.

Simple text-based output using symbols for points and centers.

How It Works
Generate random points and cluster centers.

Assign each point to the nearest center based on Manhattan distance.

Update centers to the mean of assigned points.

Repeat the process for a few iterations to improve clustering.

Print a 2D matrix showing the final cluster layout.

Symbols in Output
* → Data points (P(x, y))

0 - 9 → Cluster centers (C(x, y))

Requirements
Python 3.x

No external libraries needed (uses only built-in Python modules like random).

How to Run
bash
Copy
Edit
python your_script_name.py
(Replace your_script_name.py with the name of your Python file.)

Example Output (small part)
python-repl
Copy
Edit
. . . . . * . . 4 . . . * . . * . . . . .
. . . * . . . . . . . . . 8 . . * . . . .
. . . . * . . . . . . . * . . . . 2 . . .
...
Author
Shahriar Sumon

