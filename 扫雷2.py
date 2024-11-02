import random
import tkinter as tk
from tkinter import messagebox
import time

class Minesweeper:
    def __init__(self, master, width=16, height=16, mines=40):  # 增加了宽度、高度以及地雷数量
        self.master = master
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.marked = [[False for _ in range(width)] for _ in range(height)]
        self.buttons = [[None for _ in range(width)] for _ in range(height)]
        self.place_mines()
        self.calculate_numbers()
        self.create_widgets()
        self.start_time = None
        self.elapsed_time = 0
        self.timer_label = tk.Label(self.master, text="00:00", font=("Helvetica", 16))
        self.timer_label.grid(row=self.height, column=0, columnspan=self.width)
        self.update_timer()

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] != -1:
                self.board[y][x] = -1
                mines_placed += 1

    def calculate_numbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == -1:
                    continue
                count = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == 0 and dx == 0:
                            continue
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < self.height and 0 <= nx < self.width and self.board[ny][nx] == -1:
                            count += 1
                self.board[y][x] = count

    def create_widgets(self):
        for y in range(self.height):
            for x in range(self.width):
                button = tk.Button(self.master, width=2, height=1)
                button.grid(row=y, column=x)
                button.bind("<Button-1>", lambda event, x=x, y=y: self.reveal(x, y))
                button.bind("<Button-3>", lambda event, x=x, y=y: self.mark(x, y))
                self.buttons[y][x] = button

    def reveal(self, x, y):
        if self.start_time is None:
            self.start_time = time.time()
        if not (0 <= x < self.width and 0 <= y < self.height):
            return
        if self.revealed[y][x] or self.marked[y][x]:
            return
        self.revealed[y][x] = True
        if self.board[y][x] == -1:
            self.buttons[y][x].config(text='*', bg='red')
            messagebox.showinfo("你踩雷了！", "菜")
            self.master.quit()
        else:
            self.buttons[y][x].config(text=str(self.board[y][x]), bg='lightgrey')
            if self.board[y][x] == 0:
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == 0 and dx == 0:
                            continue
                        ny, nx = y + dy, x + dx
                        self.reveal(nx, ny)
        if all(self.revealed[y][x] or self.board[y][x] == -1 for y in range(self.height) for x in range(self.width)):
            messagebox.showinfo("将军德才兼备", "大汉之栋梁也")
            self.master.quit()

    def mark(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return
        if self.revealed[y][x]:
            return
        if self.marked[y][x]:
            self.marked[y][x] = False
            self.buttons[y][x].config(text='')
        else:
            self.marked[y][x] = True
            self.buttons[y][x].config(text='F')  # 使用字母 'F' 代替 🚩

    def update_timer(self):
        if self.start_time is not None:
            self.elapsed_time = int(time.time() - self.start_time)
        minutes, seconds = divmod(self.elapsed_time, 60)
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        self.master.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("扫雷")
    game = Minesweeper(root)
    root.mainloop()



# import random
# import tkinter as tk
# from tkinter import messagebox
# import time

# class Minesweeper:
#     def __init__(self, master, width=10, height=10, mines=10):
#         self.master = master
#         self.width = width
#         self.height = height
#         self.mines = mines
#         self.board = [[0 for _ in range(width)] for _ in range(height)]
#         self.revealed = [[False for _ in range(width)] for _ in range(height)]
#         self.marked = [[False for _ in range(width)] for _ in range(height)]
#         self.buttons = [[None for _ in range(width)] for _ in range(height)]
#         self.place_mines()
#         self.calculate_numbers()
#         self.create_widgets()
#         self.start_time = None
#         self.elapsed_time = 0
#         self.timer_label = tk.Label(self.master, text="00:00", font=("Helvetica", 16))
#         self.timer_label.grid(row=self.height, column=0, columnspan=self.width)
#         self.update_timer()

#     def place_mines(self):
#         mines_placed = 0
#         while mines_placed < self.mines:
#             x = random.randint(0, self.width - 1)
#             y = random.randint(0, self.height - 1)
#             if self.board[y][x] != -1:
#                 self.board[y][x] = -1
#                 mines_placed += 1

#     def calculate_numbers(self):
#         for y in range(self.height):
#             for x in range(self.width):
#                 if self.board[y][x] == -1:
#                     continue
#                 count = 0
#                 for dy in [-1, 0, 1]:
#                     for dx in [-1, 0, 1]:
#                         if dy == 0 and dx == 0:
#                             continue
#                         ny, nx = y + dy, x + dx
#                         if 0 <= ny < self.height and 0 <= nx < self.width and self.board[ny][nx] == -1:
#                             count += 1
#                 self.board[y][x] = count

#     def create_widgets(self):
#         for y in range(self.height):
#             for x in range(self.width):
#                 button = tk.Button(self.master, width=2, height=1)
#                 button.grid(row=y, column=x)
#                 button.bind("<Button-1>", lambda event, x=x, y=y: self.reveal(x, y))
#                 button.bind("<Button-3>", lambda event, x=x, y=y: self.mark(x, y))
#                 self.buttons[y][x] = button

#     def reveal(self, x, y):
#         if self.start_time is None:
#             self.start_time = time.time()
#         if not (0 <= x < self.width and 0 <= y < self.height):
#             return
#         if self.revealed[y][x] or self.marked[y][x]:
#             return
#         self.revealed[y][x] = True
#         if self.board[y][x] == -1:
#             self.buttons[y][x].config(text='*', bg='red')
#             messagebox.showinfo("你踩雷了！", "菜")
#             self.master.quit()
#         else:
#             self.buttons[y][x].config(text=str(self.board[y][x]), bg='lightgrey')
#             if self.board[y][x] == 0:
#                 for dy in [-1, 0, 1]:
#                     for dx in [-1, 0, 1]:
#                         if dy == 0 and dx == 0:
#                             continue
#                         ny, nx = y + dy, x + dx
#                         self.reveal(nx, ny)
#         if all(self.revealed[y][x] or self.board[y][x] == -1 for y in range(self.height) for x in range(self.width)):
#             messagebox.showinfo("将军德才兼备", "大汉之栋梁也")
#             self.master.quit()

#     def mark(self, x, y):
#         if not (0 <= x < self.width and 0 <= y < self.height):
#             return
#         if self.revealed[y][x]:
#             return
#         if self.marked[y][x]:
#             self.marked[y][x] = False
#             self.buttons[y][x].config(text='')
#         else:
#             self.marked[y][x] = True
#             self.buttons[y][x].config(text='🚩')

#     def update_timer(self):
#         if self.start_time is not None:
#             self.elapsed_time = int(time.time() - self.start_time)
#         minutes, seconds = divmod(self.elapsed_time, 60)
#         self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
#         self.master.after(1000, self.update_timer)

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("扫雷")
#     game = Minesweeper(root)
#     root.mainloop()
""" 
import pygame
import random

# 游戏设置
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 16, 16
MINES = 40
CELL_SIZE = WIDTH // COLS

# 颜色
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 初始化Pygame
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("扫雷游戏")

# 字体
FONT = pygame.font.SysFont("comicsans", 30)

def initialize_board(rows, cols):
    board = [['0' for _ in range(cols)] for _ in range(rows)]
    visible_board = [['#' for _ in range(cols)] for _ in range(rows)]
    return board, visible_board

def place_mines(board, mines):
    placed_mines = 0
    while placed_mines < mines:
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLS - 1)
        if board[row][col] != '*':
            board[row][col] = '*'
            placed_mines += 1

def calculate_numbers(board):
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] != '*':
                mine_count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        new_row = i + x
                        new_col = j + y
                        if 0 <= new_row < ROWS and 0 <= new_col < COLS and board[new_row][new_col] == '*':
                            mine_count += 1
                board[i][j] = str(mine_count)

def reveal_cell(board, visible_board, row, col):
    if visible_board[row][col] == '#':
        visible_board[row][col] = board[row][col]
        if board[row][col] == '0':
            for x in range(-1, 2):
                for y in range(-1, 2):
                    new_row = row + x
                    new_col = col + y
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                        reveal_cell(board, visible_board, new_row, new_col)

def draw_board(visible_board):
    WIN.fill(GRAY)
    for i in range(ROWS):
        for j in range(COLS):
            cell = visible_board[i][j]
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(WIN, WHITE, rect)
            pygame.draw.rect(WIN, BLACK, rect, 1)
            if cell != '#':
                text = FONT.render(cell, True, BLACK)
                text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2))
                WIN.blit(text, text_rect)

def main():
    board, visible_board = initialize_board(ROWS, COLS)
    place_mines(board, MINES)
    calculate_numbers(board)

    run = True
    game_over = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                if board[row][col] == '*':
                    visible_board[row][col] = '*'
                    game_over = True
                    print("你踩到雷了！游戏结束！")
                else:
                    reveal_cell(board, visible_board, row, col)

        draw_board(visible_board)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
 """