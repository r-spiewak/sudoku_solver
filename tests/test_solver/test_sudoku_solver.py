"""This file contains tests for the sudoku_solver module."""

import pytest


def test_solve_valid_puzzle(solver):
    """Test solving a valid Sudoku puzzle."""
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    solution = solver.solve(puzzle)
    assert solution is not None
    # Validate the solution (rows, columns, and 3x3 grids are valid)
    for i in range(9):
        assert sorted(solution[i]) == list(range(1, 10))
        assert sorted([solution[j][i] for j in range(9)]) == list(range(1, 10))
    for box_row in range(3):
        for box_col in range(3):
            subgrid = [
                solution[3 * box_row + i][3 * box_col + j]
                for i in range(3)
                for j in range(3)
            ]
            assert sorted(subgrid) == list(range(1, 10))


def test_unsolvable_puzzle(solver):
    """Test that the solver correctly identifies an unsolvable puzzle."""
    puzzle = [
        [1, 1, 0, 0, 7, 0, 0, 0, 0],  # Duplicate 1 in the first row
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    assert solver.solve(puzzle) is None


def test_empty_puzzle(solver):
    """Test solving an empty puzzle (all zeros)."""
    puzzle = [[0 for _ in range(9)] for _ in range(9)]
    solution = solver.solve(puzzle)
    # assert solution is None
    assert solution is not None
    # Validate the solution (rows, columns, and 3x3 grids are valid)
    for i in range(9):
        assert sorted(solution[i]) == list(range(1, 10))
        assert sorted([solution[j][i] for j in range(9)]) == list(range(1, 10))


def test_already_solved_puzzle(solver):
    """Test a puzzle that is already solved."""
    puzzle = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
    solution = solver.solve(puzzle)
    assert solution == puzzle  # The solution should be identical to the input


def test_invalid_grid_size(solver):
    """Test a puzzle with an invalid grid size."""
    puzzle = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    with pytest.raises(Exception):
        solver.solve(puzzle)


def test_non_integer_values(solver):
    """Test a puzzle with non-integer values."""
    puzzle = [
        [5, 3, 0, 0, "7", 0, 0, 0, 0],  # '7' is a string, not an integer
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    with pytest.raises(TypeError):
        solver.solve(puzzle)
