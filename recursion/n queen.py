## https://leetcode.com/problems/n-queens/
## -----------------------------------------------------------------------------
## The n-queens puzzle is the problem of placing n queens on an n×n chessboard
## such that no two queens attack each other.
## -----------------------------------------------------------------------------
## Given an integer n, return all distinct solutions to the n-queens puzzle.
## Each solution contains a distinct board configuration of the n-queens' placement,
## where 'Q' and '.' both indicate a queen and an empty space respectively.
## -----------------------------------------------------------------------------

# col 
# 

class Solution:

    ## Extra time complexity is required to check if the current position is valid
    def checkBoard(self,col,row,board):
        originalRow = row
        originalCol = col

        ## diagonal check 
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        
        row = originalRow
        col = originalCol
        ## other diagonal check
        while row < len(board) and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1

        row = originalRow
        col = originalCol
        ## row ✔ 
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1
        return True

    def solveNQueens(self,board,col):

        if col == len(board):
            for x in board:
                print (x)

            print("\n")
            return 

        for row in range(len(board)):
            if self.checkBoard(col,row,board):
                board[row][col] = "Q"
                self.solveNQueens(board,col+1)
                board[row][col] = "."

if __name__ == "__main__":

    n = 5
    board = [['.' for i in range(n)] for j in range(n)]
    s = Solution()
    s.solveNQueens(board,0)
