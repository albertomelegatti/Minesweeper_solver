import tkinter as tk
import time
from functions import (print_game_board, place_mines, process_move, generate_move, save_board, solve_step, game_over, ALL_COORDS, BOARD_SIZE)
from gui import MinesweeperGUI


N_MINES = round(BOARD_SIZE * BOARD_SIZE * 0.15)

def main():
    # Prima mossa casuale
    r, c = generate_move()

    # Genera la board con mine (nascosta)
    initial_board = place_mines(N_MINES)
    save_board(initial_board)

    # Board di gioco: tutte le celle coperte (-2)
    game_board = [[-2 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Esegui la prima mossa
    process_move(initial_board, game_board, (r, c))
    #print_game_board(game_board)

    # Avvia la GUI
    root = tk.Tk()
    root.title("Minesweeper Solver")
    app = MinesweeperGUI(root, initial_board, game_board)
    root.mainloop()


if __name__ == "__main__":
    main()
