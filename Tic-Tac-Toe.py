import random
import tkinter as tk
from tkinter import messagebox

# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

# Tkinter setup
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="black")  # Set background color for window

# Styling constants
BUTTON_COLOR = "White"
TEXT_COLOR = "Purple"
FONT = ('Helvetica', 24, 'bold')

buttons = [[None for _ in range(3)] for _ in range(3)]

def update_board():
    '''Update button text based on board status.'''
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])

def make_move(row, col, player):
    '''Make a move on the board and update the GUI.'''
    if board[row][col] == " ":
        board[row][col] = player
        update_board()
        if check_winner(player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_board()
        elif all(cell != " " for row in board for cell in row):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            if player == "X":
                computer_move()
        return True
    else:
        messagebox.showwarning("Invalid Move", "Position already taken")
        return False

def check_winner(player):
    '''Check if the given player has won.'''
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def find_best_move(player):
    '''AI move logic to find the best move for the computer.'''
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(player):
                    board[row][col] = " "
                    return row, col
                board[row][col] = " "
    opponent = "X" if player == "O" else "O"
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = opponent
                if check_winner(opponent):
                    board[row][col] = " "
                    return row, col
                board[row][col] = " "
    if board[1][1] == " ":
        return 1, 1
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for row, col in corners:
        if board[row][col] == " ":
            return row, col
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return row, col

def computer_move():
    row, col = find_best_move("O")
    make_move(row, col, "O")

def reset_board():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    update_board()

def on_button_click(row, col):
    '''Handle button click for player X.'''
    make_move(row, col, "X")

# Create buttons and grid layout
for i in range(3):
    for j in range(3):
        button = tk.Button(window, text=" ", font=FONT, width=5, height=2,
                           bg=BUTTON_COLOR, fg=TEXT_COLOR, 
                           command=lambda row=i, col=j: on_button_click(row, col))
        button.grid(row=i, column=j, padx=5, pady=5)  # Add padding between buttons
        buttons[i][j] = button

# Center the board
for i in range(3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
window.mainloop()