"""Test the CLI app."""

from typer.testing import CliRunner

from sudoku_solver.run import app

runner = CliRunner()


def test_app(capsys):
    """Test the cli app invocation."""
    result = runner.invoke(
        app, ["--puzzle", "tests/test_objects/test_puzzle.json"]
    )
    with capsys.disabled():
        print("stdout:")
        print(result.stdout)
        # print("stderr:")
        # print(result.stderr)
        # Need to capture stderr separately.
        # Otherwise it's bundled in with stdout.
    it_worked = "Solved"
    assert result.exit_code == 0
    assert it_worked in result.stdout
    # assert "Let's have a coffee in Berlin" in result.stdout


def test_app_bad_puzzle(capsys):
    """Test the cli app invocation for unsolvable puzzle."""
    result = runner.invoke(
        app, ["--puzzle", "tests/test_objects/test_bad_puzzle.json"]
    )
    with capsys.disabled():
        print("stdout:")
        print(result.stdout)
    it_worked = "No solution"
    assert result.exit_code == 0
    assert it_worked in result.stdout
