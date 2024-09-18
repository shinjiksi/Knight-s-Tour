import random

# declare a board size
n = 8

#counter for the number of move


# cThe function first checks if the given coordinates (x, y) are 
# within the bounds of the chessboard. 
# If not, it returns False. Then, it checks if the position is empty 
# (i.e., board[x][y] == -1). If both conditions are satisfied, t
# he function returns True, indicating that the knight can be placed 
# at the given position. Otherwise, it returns False.
def isSafe(x, y, board):
    if (x >=0 and x < n and y >= 0 and y < n and board[x][y] == -1):
        return True
    return False

# Inside the printSolution function, 
# a nested loop is used to iterate over each cell of the chessboard. 
# For each cell, the value at that position in the board list is printed. 
# The end=" " argument in the print function ensures that 
# the values are printed in the same line, separated by a space. 
# After printing all the values in a row, a newline character is p
# rinted using the print function without any arguments.
def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

# function to solve Knight Tour problem using backtracking
# The selected code within the open file is the solveKT function, 
# which is responsible for solving the Knight's Tour problem using backtracking. 
def solveKT(n):
    # Initializing a board matrix
    # The function initializes a board matrix of size n x n with all cells set to -1. 
    # This matrix will be used to keep track of the knight's movements.
    board = [[-1 for _ in range(n)] for _ in range(n)]

    # initializes the x and y coordinates of the knight's possible moves.
    #  The move_x list contains the horizontal movements, 
    # while the move_y list contains the vertical movements.
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # The starting coordinates of the knight are set to (0, 0) on the board, 
    # and the first move is marked with 0.
    board[0][0] = 0

    # A counter pos is initialized to keep track of the number of moves made
    pos = 1

    # checks if the next move is available by calling the solveKTUtil function. 
    # If the next move is not available, 
    # it prints "Solution does not exist" and returns False.
    if not solveKTUtil(n, board, 0, 0, move_x, move_y, pos):
        print("Solution does not exist")
        return False
    # If the next move is available, the function calls the printSolution 
    # function to print the final solution, and returns True
    else:
        printSolution(n, board)
        return True

# resursive call to solve the Knight Tour problem
def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, pos):
    # check if all n*n cells have been visited
    if pos == n*n:
        return True
    
    for i in range(n):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]

        # check if this move is valid
        if isSafe(new_x, new_y, board):
            # mark this move
            board[new_x][new_y] = pos

            # make a recursive call for the next move
            if solveKTUtil(n, board, new_x, new_y, move_x, move_y, pos+1):
                return True

            # if the above move was not successful, then remove this move
            board[new_x][new_y] = -1

# Driver Code
if __name__ == "__main__":
    solveKT(n)


