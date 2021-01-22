"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sourav Pandya
ID:      170228640
Email:   pand8640@mylaurier.ca
__updated__ = "2021-01-07"
-------------------------------------------------------
"""

def sudoku_layout(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(sudoku[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")
    
    
    
def isValid(sudoku, row, col, number):
    
    for i in range(0, 9):
        if sudoku[row][i] == number:
            return False
    for j in range(0, 9):
        if sudoku[j][col] == number:
            return False  
    
    block_row = (row//3)*3
    block_col = (col//3)*3
    
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[block_row+i][block_col+j] == number:
                return False
    
    return True

def solve(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if isValid(sudoku, row, col, num):
                        sudoku[row][col] = num
                        solve(sudoku)
                        sudoku[row][col] = 0
                return
    sudoku_layout(sudoku)
                
    
    