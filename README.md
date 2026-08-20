# kamisado_2

A small Python/[pygame](https://www.pygame.org/) implementation of a board game called Kamisado,
played locally by two people on the same computer with mouse input.

## Status

Early-stage personal project. All development happened over a couple of days in February 2025
(commits `v0.1`–`v0.3`); the repository has not been actively developed since. Code, comments,
and in-game text are in Italian.

## What's here

- `main.py` — entry point: creates the game and GUI and starts the main loop.
- `game_logic.py` — board state and rules: an 8x8 board of colored cells, two players with
  colored towers, diagonal moves in a straight line until blocked, a "next mover" constraint
  based on the color of the cell just landed on, and a win condition for reaching the opposite
  back row.
- `gui.py` — pygame rendering of the board and towers, turn/active-color display, and mouse
  click handling for selecting and moving pieces.
- `constants.py` — board color layout and window/cell size constants.
- `tutorial.py` — a separate lesson/tutorial module; it is not imported by `main.py`.

## Running it

Requires Python 3 and the packages listed in `requirements.txt`:

```
pip install -r requirements.txt
python main.py
```

## License

No LICENSE file is included in this repository.
