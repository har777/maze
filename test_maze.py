import unittest
from maze import get_empty_maze, get_maze_solution_path

class MazeTestCase(unittest.TestCase):
    """Tests for `maze.py`."""

    def test_get_empty_maze(self):
        """Check if generation of empty mazes are correct."""
        generated_maze = get_empty_maze(3, 4)
        expected_maze = [
            [0, 0, 0], 
            [0, 0, 0], 
            [0, 0, 0], 
            [0, 0, 0]
        ]
        self.assertEqual(
            generated_maze,
            expected_maze,
            msg='Generated empty mazes did not match expected output.'
        )

    def test_solution_path(self):
        """Check if generated solution path given a perfect maze is correct."""
        maze = [
            [2, 6, 14, 10, 2],
            [3, 1, 3, 3, 3],
            [3, 6, 9, 3, 3],
            [3, 5, 10, 5, 11],
            [5, 12, 9, 4, 9]
        ]
        '''
        The above maze looks like:
         _________
        | |     | |
        | |_| | | |
        | |  _| | |
        | |_  |_  |
        |_____|___|
        '''
        generated_solution_path = get_maze_solution_path(maze, 0, 0, 4, 4)
        expected_solution_path = [
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
            (4, 1), (4, 2), (3, 2), (3, 1), (2, 1),
            (2, 2), (1, 2), (0, 2), (0, 3), (1, 3),
            (2, 3), (3, 3), (3, 4), (4, 4)
        ]
        self.assertEqual(
            generated_solution_path,
            expected_solution_path,
            msg='Generated maze solution path did not match expected output.'
        )


if __name__ == '__main__':
    unittest.main()
