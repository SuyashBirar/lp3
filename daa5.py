
N = 8

# Check whether placing a queen is safe
def is_safe(board, row, col):

    # Check left side of the row
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


# Solve using backtracking
def solve(board, col):

    if col >= N:
        return True

    for row in range(N):

        if is_safe(board, row, col):

            board[row][col] = 1

            if solve(board, col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main program
board = [[0 for _ in range(N)] for _ in range(N)]

# Place first queen at row 0, column 0
board[0][0] = 1

print("Initial Board:")
for row in board:
    print(row)

if solve(board, 1):

    print("\nFinal 8-Queens Matrix:")
    for row in board:
        print(row)

else:
    print("Solution does not exist")
