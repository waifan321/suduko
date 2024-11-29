import random

def pattern(r, c):
    return (3 * (r % 3) + r // 3 + c) % 9

def shuffle(s):
    return random.sample(s, len(s))

def generate_sudoku():
    rBase = range(3)
    rows  = [g * 3 + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols  = [g * 3 + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums  = shuffle(range(1, 10))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = 81
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // 9][p % 9] = 0

    return board

def generate_sudoku_with_difficulty(level='medium'):
    difficulty = {'easy': 1, 'medium': 0.75, 'hard': 0.5}
    if level not in difficulty:
        raise ValueError("Invalid difficulty level. Choose from 'easy', 'medium', 'hard'.")

    board = generate_sudoku()
    squares = 81
    empties = int(squares * (1 - difficulty[level]))
    for p in random.sample(range(squares), empties):
        board[p // 9][p % 9] = 0

    return board

def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

if __name__ == "__main__":
    level = input("Choose difficulty level (easy, medium, hard): ").strip().lower()
    sudoku_board = generate_sudoku_with_difficulty(level)
    print_sudoku(sudoku_board)
