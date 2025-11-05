import tkinter as tk
from functions import process_move, generate_move, solve_step, game_over, generate_safe_move
from tkinter import messagebox, simpledialog


CELL_SIZE = 25  # dimensione in pixel di ogni cella
COLORS = {
    -2: "purple",  # celle nascoste
    -3: "red",     # bandierine
    0: "lightgray" # celle vuote
}

class MinesweeperGUI:
    def __init__(self, root, initial_board, game_board):
        self.root = root
        self.initial_board = initial_board
        self.game_board = game_board
        self.rows = len(game_board)
        self.cols = len(game_board[0])
        self.canvas = tk.Canvas(root, width=self.cols * CELL_SIZE, height=self.rows * CELL_SIZE, bg="black")
        self.canvas.pack()
        self.draw_board()
        self.root.after(500, self.solver_step)  # parte il solver dopo mezzo secondo

    def draw_board(self):
        self.canvas.delete("all")
        for r in range(self.rows):
            for c in range(self.cols):
                val = self.game_board[r][c]
                x0, y0 = c * CELL_SIZE, r * CELL_SIZE
                x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE

                color = COLORS.get(val, "white")
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")

                if val > 0:
                    self.canvas.create_text((x0+x1)//2, (y0+y1)//2, text=str(val), font=("Arial", 10, "bold"))

                elif val == -3:
                    self.canvas.create_text((x0+x1)//2, (y0+y1)//2, text="🚩", font=("Arial", 10))

                elif val == -1:
                    self.canvas.create_text((x0+x1)//2, (y0+y1)//2, text="💣", font=("Arial", 10))




    def solver_step(self):
        changed = solve_step(self.initial_board, self.game_board)
        self.draw_board()
        self.root.update()
        choice = ""

        if game_over(self.game_board):
            print("🎉 Game completed successfully!")
            return

        if not changed:
            choice = simpledialog.askstring("No logical moves", "No logical moves found.\nType 'R' for a random move or 'H' for a hint:")
        if not choice:
            self.root.after(300, self.solver_step)
            return
        
        choice = choice.strip().lower()

        if choice == "r":
            move = generate_move()
            r, c = move

            if self.initial_board[r][c] == -1:
                self.game_board[r][c] = -1
                self.draw_board()
                messagebox.showerror("Game Over", "💣 You hit a mine!")
                return
            
            process_move(self.initial_board, self.game_board, move)
            



        elif choice == "h":
            move = generate_safe_move()
            process_move(self.initial_board, self.game_board, move)

        else:
            messagebox.showwarning("Invalid choice", "Please type 'R' or 'H'.")

        
        


        # Qualunque sia la scelta, stampa la schermata
        
        self.root.after(200, self.solver_step)  # continua a risolvere

