"""Run the script_profits app."""

import time

import typer
from typing_extensions import Annotated

from sudoku_solver.loaders.puzzle_loader import load_puzzle
from sudoku_solver.solver.sudoku_solver import SudokuSolver

app = typer.Typer()
state = {"verbosity": 0}


@app.command()
def main(
    puzzle: Annotated[str, typer.Option(..., "--puzzle", "-p")],
    verbosity: Annotated[
        int, typer.Option("--verbosity", "-v", count=True)
    ] = 0,
) -> int:
    """Main function to call the script_profit methods."""
    if verbosity > 0:
        print(f"Verbosity: {verbosity}")
        state["verbosity"] = verbosity
    start_time = time.time()
    # Load puzzle as grid here.
    puzzle_grid = load_puzzle(puzzle)
    print(f"Puzzle: {puzzle_grid}")
    solver = SudokuSolver()
    if solution := solver.solve(puzzle_grid):
        print(f"Solved puzzle: {solution}")
    else:
        print("No solution exists.")
    print(f"Total solution time: {(time.time()-start_time)} s")
    return 0


# @app.callback()
# def verbosity_level(
#     ctx: typer.Context,
#     #verbosity: Annotated[Optional[List[bool]], typer.Option(...,"--verbosity","-v")] = [False],
#     verbosity: Annotated[Optional[int], typer.Option("--verbosity","-v",count=True)]
# ) -> int:
#     """
#     Manage users in the awesome CLI app.
#     """
#     #level = sum(verbosity)
#     level = verbosity
#     if level > 0:
#         print(f"Verbosity: {level}")
#         state["verbosity"] = level
#     if ctx.invoked_subcommand is not None:
#         ctx.invoke(typer.main.get_command(app).get_command(ctx, "main"))
#     return 0


def run() -> None:
    """Entrypoint for poetry."""
    app()


if __name__ == "__main__":
    app()
