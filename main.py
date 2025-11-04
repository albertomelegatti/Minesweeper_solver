import time
from functions import (print_game_board, place_mines, process_move, generate_move, save_board, solve_step, game_over, ALL_COORDS, BOARD_SIZE)

N_MINES = round(BOARD_SIZE * BOARD_SIZE * 0.15)

def main():
    # Prima mossa
    r, c = generate_move()

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
        time.sleep(0.3)

        if not changed:
            move = generate_move()
            r,c = move
            if initial_board[r][c] == -1:
                game_board[r][c] = -1
                print_game_board(game_board)
                print("Game Over, hai trovato una bomba!")
                exit()

            process_move(initial_board, game_board, move)



if __name__ == "__main__":
    main()
