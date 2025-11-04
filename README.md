# 💣 Minesweeper Solver (Python)

A simple yet fun project where **Python** plays *Minesweeper*!  
This program generates a random board, places mines, and then tries to solve the game automatically using basic logic (and a bit of luck for the uncertain cases 😄).

---

## 🧩 How It Works

The solver follows a straightforward two-step strategy:

1. **Logical Analysis**  
   For each revealed cell, it examines the surrounding tiles:
   - If the number of hidden cells equals the cell’s value → place flags 🚩  
   - If all adjacent mines are already flagged → reveal all remaining covered cells  

2. **Random Guessing**  
   When no logical moves are possible, the solver makes a random move from the list of all possible coordinates (excluding already revealed or flagged ones).


## 🧠 Main Components

- **`place_mines()`** → Randomly distributes mines across the board  
- **`cell_clicker()`** → Recursively reveals empty cells (like Minesweeper’s zero expansion)  
- **`analyze_cell()`** → Applies basic logical rules to mark mines or reveal safe cells  
- **`solve_step()`** → Performs one full logical iteration over the grid  
- **`generate_move()`** → Picks a random safe cell when logic gets stuck  
- **`print_game_board()`** → Displays the current state of the game with emojis and color blocks  

---

## 🕹️ How to Run

Clone the repository and simply run:

```bash
python main.py
