import time
from functions import (
    print_board, print_game_board, place_mines,
    process_move, generate_move, save_board, solve_step, game_over
)

BOARD_SIZE = 30
N_MINES = round(BOARD_SIZE * BOARD_SIZE * 0.25)

def main():
    # Prima mossa
    r, c = generate_move(BOARD_SIZE)

    # Genera la board con mine (non visibile al giocatore)
    initial_board = place_mines(N_MINES)
    save_board(initial_board)

    # Board di gioco: tutta coperta (-2)
    game_board = [[-2 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Prima mossa
    process_move(initial_board, game_board, (r, c))
    print_game_board(game_board)

    # Ciclo di gioco
    while not game_over(game_board):
        changed = solve_step(initial_board, game_board)
        print_game_board(game_board)
        time.sleep(0.2)
        if not changed:
            move = generate_move(BOARD_SIZE)
            process_move(initial_board, game_board, move)



if __name__ == "__main__":
    main()
