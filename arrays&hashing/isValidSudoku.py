import collections

class Solution(object):
    # my first approach idea: solves cases 1 and 2, but not the box case (crucial component)

# def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         prev_rows = set()
#         prev_columns = set()
#         box_squares = set()

#         column_increment = 0
#         row_increment = 0

#         box_index = 0
#         box_value = 0

#         for row in range(len(board)):
#             if row == prev_rows:
#                 row_increment += 1
#                 prev_rows.add(row)
      
#             for column in range(len(board)):

#                 if board[row][column] == ".":
#                     continue
#                 if (column == prev_columns):
#                     column_increment += 1
#                     prev_columns.add(column)

#         if row_increment > 0:
#             return False

#         if column_increment > 0:
#             return False

#         if row_increment == 0 and column_increment == 0:
#             return True 


# better approach: O(9^2)

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True 


