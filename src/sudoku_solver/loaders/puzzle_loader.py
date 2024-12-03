"""This file contains a method for loading grid puzzles, and its dependencies."""

import json
import os
from typing import Any

from sudoku_solver.constants import PUZZLE_COLUMNS, PUZZLE_ROWS


def is_filename(string: str) -> bool:
    """This function checks if a string is likely a
    filename.

    Args:
        string(str): String to check.

    Returns:
        bool: Whether the string is liekly a
            filename (True) or not (False).
    """
    return os.path.isfile(string)


def is_json_str(string: str) -> bool:
    """This function checks if a string is a valid
    JSON object.

    Args:
        string(str): String to check.

    Returns:
        bool: Whether the string is a valid
            JSON object (True) or not (False).
    """
    try:
        json.loads(string)
    except json.JSONDecodeError:
        return False
    return True


def load_from_str(puzzle_str: str) -> Any:
    """This function loads a puzzle from a JSON string.

    Args:
        puzzle_str (str): JSON string from which to
            load puzzle.

    Returns:
        Any: The puzzle loaded from JSON string.
    """
    puzzle_obj = json.loads(puzzle_str)
    return puzzle_from_json(puzzle_obj)


def puzzle_from_json(puzzle_json: Any) -> Any:
    """This function loads a puzzle from a JSON object.
    The object must contain exactly one entry, which is
    the puzzle.

    Args:
        puzzle_json (Any): The JSON-loaded puzzle object.

    Returns:
        Any: The puzzle from the JSON object.

    Raises:
        ValueError: If there are the wrong number of
            elements in the JSON object (i.e., != 1).
    """
    if len(puzzle_json) == 1:
        for _, val in puzzle_json.items():
            return val
    else:
        raise ValueError(f"{len(puzzle_json)} elements in JSON; expected 1.")


def load_from_file(puzzle_file: str) -> Any:
    """This function loads a puzzle from a JSON file.

    Args:
        puzzle_file (str): Filename from which to
            load puzzle.

    Returns:
        Any: The puzzle loaded from puzzle_file.

    Raises:
        ValueError: If the filename does not have
            the .json extension.
    """
    if not puzzle_file.endswith("json"):
        raise ValueError(f"{puzzle_file} is not a .json file.")
    with open(puzzle_file, "r", encoding="utf8") as file:
        puzzle_obj = json.load(file)
    return puzzle_from_json(puzzle_obj)


def load_puzzle(puzzle_obj: str) -> list[list[int]]:
    """This functon loads and validates a sudoku puzzle
    from a JSON string or .json file.

    Args:
        puzzle_obj (str): The object from which to
            load the puzzle.

    Returns:
        list[list[int]]: The loaded and validated puzzle.

    Raises:
        TypeError: If puzzle_obj is not a
            correctly-formatted JSON object or a .json file.
        ValueError: If the input puzzle is not correctly
            formed.
    """
    if is_filename(puzzle_obj):
        puzzle = load_from_file(puzzle_obj)
    elif is_json_str(puzzle_obj):
        puzzle = load_from_str(puzzle_obj)
    else:
        raise TypeError(f"{puzzle_obj} input is not yet implemented.")
    if validate_puzzle(puzzle):
        return puzzle
    raise ValueError(f"Input puzzle {puzzle} not correctly formed.")


def validate_puzzle(puzzle: Any) -> bool:
    """This function validates that a puzzle conforms
    to the expected data types and shapes.

    Args:
        puzzle (Any): The puzzle object to validate.

    Returns:
        bool: Whether the puzzle object meets the type and
            shape requirements for sudoku puzzles (True) or
            not (False).
    """
    if not isinstance(puzzle, list) | len(puzzle) == PUZZLE_ROWS:
        return False
    return all(
        isinstance(row, list) | len(row)
        == PUZZLE_COLUMNS | all(isinstance(elem, int) for elem in row)
        for row in puzzle
    )
