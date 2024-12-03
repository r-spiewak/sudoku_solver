"""This file contains fixtures for the tests for the sudoku_solver module."""

import pytest

from sudoku_solver.solver.sudoku_solver import SudokuSolver


@pytest.fixture
def solver():
    """Fixture to create a fresh SudokuSolver instance for each test."""
    return SudokuSolver()
