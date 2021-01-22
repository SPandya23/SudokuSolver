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
from working import sudoku_layout, solve

file = open("sudoku.txt", "r")
f = file.read().splitlines()
sudoku = []
for i in range(len(f)):
    row = []
    for j in range(len(f[i])):
        row.append(int(f[i][j]))
        if row not in sudoku: 
            sudoku.append(row)
            
print("Sudoku to be solved:")
print()
sudoku_layout(sudoku)
print()
print("Sudoku solved:")
print()
solve(sudoku)
