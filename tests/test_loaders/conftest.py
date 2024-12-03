"""This file contains fixtures for the tests for the puzzle_loader module."""

import json

import pytest


@pytest.fixture
def list_puzzle():
    """A valid puzzle as a list of lists of ints."""
    return [
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


@pytest.fixture
def json_puzzle(list_puzzle):
    """A valid puzzle in valid JSON format (a dict)."""
    return {"puzzle": list_puzzle}


@pytest.fixture
def valid_json_str(json_puzzle):
    """A valid puzzle in a valid JSON string."""
    return json.dumps(json_puzzle)


@pytest.fixture
def invalid_json_str():
    """An invalid puzzle in a valid JSON string."""
    return '{"puzzle": [5, 3, 0, 0, 7, 0, 0, 0, 0]}'


@pytest.fixture
def valid_json_file(tmp_path, json_puzzle):
    """A valid puzzle in a valid .json file."""
    file_path = tmp_path / "puzzle.json"
    with open(file_path, "w") as f:
        json.dump(
            json_puzzle,
            f,
        )
    return file_path


# @pytest.fixture
# def invalid_json_file(tmp_path):
#     """An invalid puzzle in a valid .json file."""
#     file_path = tmp_path / "invalid_puzzle.json"
#     with open(file_path, "w") as f:
#         f.write('{"puzzle": "not a puzzle"}')
#     return file_path
