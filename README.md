# Snake, Water, Gun Game (Python)

A simple, terminal-based implementation of the classic Snake, Water, Gun game (similar to Rock, Paper, Scissors) built using Python.

## How the Game Works
The rules are straightforward:
* Snake drinks Water (Snake wins)
* Water rusts Gun (Water wins)
* Gun kills Snake (Gun wins)

## Features
* Randomized Opponent: Uses Python's built-in random module to make the computer's choice unpredictable.
* Smart Mapping: Utilizes Python dictionaries to seamlessly map user inputs (s, w, g) to numbers and display the choices back in plain text.
* Clean Logic: Uses conditional statements (if-elif-else) to evaluate the game's outcome accurately.

## How to Run
1. Make sure you have Python 3 installed on your system.
2. Clone this repository or download the source code file.
3. Open your terminal/command prompt, navigate to the project folder, and run:
   ```bash
   python main.py
   ```
4. Enter your choice when prompted: s for Snake, w for Water, or g for Gun.

## Concepts Learned
* Working with Python's random module.
* Using dictionaries for reverse-mapping keys and values.
* Implementing game logic via conditional branching.
