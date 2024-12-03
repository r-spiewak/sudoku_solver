"""This file contains the actual SudokuSolver class."""

from z3 import And, Distinct, Int, Solver, sat

from sudoku_solver.constants import PUZZLE_LARGEST_INT


class SudokuSolver:  # pylint: disable=too-few-public-methods
    """SudokuSolver class for solving sudoku puzzles."""

    def __init__(self):
        """Initialize the solver with a grid and base constraints."""
        self.solver = Solver()
        self.grid = [
            [Int(f"cell_{i}_{j}") for j in range(9)] for i in range(9)
        ]
        self._add_base_constraints()

    def _add_base_constraints(self):
        """Add base constraints for the Sudoku game."""
        # Each cell contains a number between 1 and 9, inclusive:
        for i in range(9):
            for j in range(9):
                self.solver.add(
                    And(
                        self.grid[i][j] >= 1,
                        self.grid[i][j] <= PUZZLE_LARGEST_INT,
                    )
                )

        # Rows and columns must ahve distinctvalues:
        for i in range(9):
            # Row uniqueness:
            self.solver.add(Distinct(self.grid[i]))
            # Column uniqueness:
            self.solver.add(Distinct([self.grid[j][i] for j in range(9)]))

        # 3x3 subgrid "boxes" have distinct values:
        for subgrid_row in range(3):
            for subgrid_col in range(3):
                subgrid = [
                    self.grid[3 * subgrid_row + i][3 * subgrid_col + j]
                    for i in range(3)
                    for j in range(3)
                ]
                self.solver.add(Distinct(subgrid))

    def solve(self, puzzle: list[list[int]]) -> list[list[int]] | None:
        """Solves the given sudoku puzzle.

        Args:
            puzzle (list[list[int]]): A 9x9 grid
                (as a list of lists of integers),
                with 0 for empty cells.

        Returns:
            list[list[int]] | None: The solved puzzle,
                or None if unsolvable.
        """
        # Apply the puzzle as constraints tot he solver:
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0:
                    if not isinstance(puzzle[i][j], int):
                        raise TypeError(
                            f"Element {puzzle[i][j]} (type: "
                            f"{type(puzzle[i][j])}) is not of type int."
                        )
                    self.solver.add(self.grid[i][j] == puzzle[i][j])

        # Check for a solution:
        if self.solver.check() == sat:
            model = self.solver.model()
            solved_grid = [
                [model.evaluate(self.grid[i][j]).as_long() for j in range(9)]
                for i in range(9)
            ]
            return solved_grid
        return None
