# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A:  If unit contains 2 naked twins (pair of boxes with the same 2-digit value), other boxes in this unit can't contain any of these 2 digits.
So if there are naked twins in unit, we delete these 2 digits from other boxes in this unit. It helps us to reduce a number of possible values in other boxes in the unit, so it will make us easier to find right values in these boxes. And it will reduce space of search later.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We have new constraint: in diagonal elements the same values can't be repeated.
So I create additional units to diagonal elements. And then solve sudoku with additional constraint - that when element is diagonal it has additional peers from diagonal unit, it will also helps to reduce the number of possible values of elements in each box.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.