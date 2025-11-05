import os
import random
from typing import List, Tuple, Optional

BOARD_SIZE = 30
ALL_COORDS = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)]
MINE_POSITIONS = []





def place_mines(n_mines: int, first_move: Optional[Tuple[int:int]] = None) -> List[List[str]]:

    global ALL_COORDS, MINE_POSITIONS

    # Creiamo la griglia vuota
    board = [[-2 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

     # Se presente, escludi la prima mossa
    if first_move:
        ALL_COORDS.remove(first_move)

    # Scegliamo casulamente n_mines posizioni
    MINE_POSITIONS = random.sample(ALL_COORDS, n_mines)

    for r, c in MINE_POSITIONS:
        board[r][c] = -1

    return board




def mine_counter(initial_board, position):
    mines = 0
    rows = len(initial_board)
    cols = len(initial_board[0])

    row = position[0]
    col = position[1]

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = row + dr, col + dc
            # controlla che sia all’interno della griglia
            if 0 <= nr < rows and 0 <= nc < cols:
                if initial_board[nr][nc] == -1:
                    mines += 1
    return mines




def cell_clicker(initial_board, game_board, position):
    
    global ALL_COORDS

    rows, cols = len(game_board), len(game_board[0])
    r, c = position

    # sicurezza: ignora posizioni fuori griglia
    if not (0 <= r < rows and 0 <= c < cols):
        return

    # scopri la cella se è coperta e non è una bandierina
    if game_board[r][c] == -2:
        game_board[r][c] = mine_counter(initial_board, (r, c))
        if position in ALL_COORDS:
            ALL_COORDS.remove(position)


    # se la cella è 0, espandi nei dintorni
    if game_board[r][c] == 0:
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # evita di riaprire celle già scoperte o bandierine
                    if game_board[nr][nc] == -2:
                        if (nr, nc) in ALL_COORDS:
                            ALL_COORDS.remove((nr, nc))
                        cell_clicker(initial_board, game_board, (nr, nc))




def process_move(initial_board, game_board, move):
    
    (r, c) = move
    game_board[r][c] = mine_counter(initial_board, move)
    cell_clicker(initial_board, game_board, move)









def analyze_cell(initial_board, game_board, position):

    global ALL_COORDS

    rows, cols = len(game_board), len(game_board[0])
    r, c = position
    val = game_board[r][c]

    # consideriamo solo celle scoperte con numero > 0
    if not isinstance(val, int) or val <= 0:
        return False

    covered = []
    flags = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if game_board[nr][nc] == -2:
                    covered.append((nr, nc))
                elif game_board[nr][nc] == -3:
                    flags += 1

    changed = False

    # CASO 1: tutte le coperte sono mine → piazza bandierine
    if len(covered) > 0 and val - flags == len(covered):
        for (nr, nc) in covered:
            game_board[nr][nc] = -3
            if (nr, nc) in ALL_COORDS:
                ALL_COORDS.remove((nr, nc))
            changed = True

    # CASO 2: tutte le mine già marcate → scopri le restanti
    elif flags == val and len(covered) > 0:
        for (nr, nc) in covered:
            game_board[nr][nc] = mine_counter(initial_board, (nr, nc))
            if (nr, nc) in ALL_COORDS:
                ALL_COORDS.remove((nr, nc))
            if game_board[nr][nc] == 0:
                # espansione ricorsiva tipo cell_clicker
                cell_clicker(initial_board, game_board, (nr, nc))
            changed = True

    return changed
    


def solve_step(initial_board, game_board):
    changed = False
    rows, cols = len(game_board), len(game_board[0])
    for r in range(rows):
        for c in range(cols):
            if isinstance(game_board[r][c], int) and game_board[r][c] >= 0:
                if analyze_cell(initial_board, game_board, (r, c)):
                    changed = True
    return changed




def print_game_board(board):
    os.system("cls")
    for row in board:
        row_str = ""
        for cell in row:
            if cell == -2:
                row_str += "🟪 "
            elif cell == -3:
                row_str += "🚩 "
            elif cell == -1:
                row_str += "💣 "
            else:
                row_str += f"{cell:2} "  # formato con spazio per allineare i numeri
        print(row_str)
    print()  # riga vuota per separare le stampe successive




# Genera una mossa casuale
def generate_move():
    global ALL_COORDS
    return random.sample(ALL_COORDS, 1)[0]

# Genera un mossa sicura
def generate_safe_move():
    global ALL_COORDS, MINE_POSITIONS

    move = random.sample(ALL_COORDS, 1)[0]
    while move in MINE_POSITIONS:
        move = random.sample(ALL_COORDS, 1)[0]
    return move


def save_board(board):
    filename="initial_board.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for row in board:
            f.write(" ".join(str(cell) for cell in row) + "\n")


def game_over(game_board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if game_board[i][j] == -2 or  game_board[i][j] == -1:
                return False
    
    return True

