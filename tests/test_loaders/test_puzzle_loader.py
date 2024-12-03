"""This file contains tests for the puzzle_loader module."""

import json

import pytest

from sudoku_solver.loaders.puzzle_loader import (
    is_filename,
    is_json_str,
    load_from_file,
    load_from_str,
    load_puzzle,
    puzzle_from_json,
    validate_puzzle,
)


# Tests for is_filename
def test_is_filename_with_file(valid_json_file):
    assert is_filename(str(valid_json_file)) is True


def test_is_filename_with_invalid_file():
    assert is_filename("nonexistent_file.json") is False


# Tests for is_json_str
def test_is_json_str_with_valid_json(valid_json_str):
    assert is_json_str(valid_json_str) is True


def test_is_json_str_with_invalid_json(invalid_json_str):
    assert is_json_str(invalid_json_str[:-1]) is False  # Truncated JSON


def test_is_json_str_with_non_json():
    assert is_json_str("random string") is False


# Tests for load_from_str
def test_load_from_str_with_valid_json(valid_json_str, list_puzzle):
    puzzle = load_from_str(valid_json_str)
    assert puzzle == list_puzzle


def test_load_from_str_with_invalid_json():
    with pytest.raises(json.JSONDecodeError):
        load_from_str("{invalid json}")


# Tests for puzzle_from_json
def test_puzzle_from_json_with_valid_data():
    data = {"puzzle": [[5, 3, 0, 0, 7, 0, 0, 0, 0]]}
    puzzle = puzzle_from_json(data)
    assert puzzle == [[5, 3, 0, 0, 7, 0, 0, 0, 0]]


def test_puzzle_from_json_with_invalid_data():
    data = {"puzzle": "not a puzzle", "extra": "invalid"}
    with pytest.raises(ValueError):
        puzzle_from_json(data)


# Tests for load_from_file
def test_load_from_file_with_valid_file(valid_json_file, list_puzzle):
    puzzle = load_from_file(str(valid_json_file))
    assert puzzle == list_puzzle


# This test is unecessary, since it's actually testing the json library, which I don't need to do.
# def test_load_from_file_with_invalid_file(invalid_json_file):
#     with pytest.raises(ValueError):
#         load_from_file(str(invalid_json_file))


def test_load_from_file_with_non_json_extension():
    with pytest.raises(ValueError):
        load_from_file("puzzle.txt")


# Tests for load_puzzle
def test_load_puzzle_with_valid_json_str(valid_json_str, list_puzzle):
    puzzle = load_puzzle(valid_json_str)
    assert puzzle == list_puzzle


def test_load_puzzle_with_invalid_json_str():
    with pytest.raises(TypeError):
        load_puzzle("not a json string")


def test_load_puzzle_with_valid_file(valid_json_file, list_puzzle):
    puzzle = load_puzzle(str(valid_json_file))
    assert puzzle == list_puzzle


# Tests for validate_puzzle
def test_validate_puzzle_with_valid_puzzle(list_puzzle):
    assert validate_puzzle(list_puzzle) is True


def test_validate_puzzle_with_invalid_puzzle():
    puzzle = [
        [5, 3, 0, 0, 7, 0],
        [6, 0, 0, 1, 9],
        [0, 9, 8],
    ]
    assert validate_puzzle(puzzle) is False


def test_validate_puzzle_with_non_list():
    assert validate_puzzle("not a list") is False
