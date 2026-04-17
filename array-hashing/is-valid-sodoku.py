from collections import defaultdict
from typing import List

def is_valid_sodoku(board: List[List[str]]):
    col_set = defaultdict(set)
    row_set = defaultdict(set)
    sub = defaultdict(set)

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '.':
                continue
            if board[row][col] in row_set[row] or board[row][col] in col_set[col] or board[row][col] in sub[(row // 3, col //3)]:
                return False
            col_set[col].add(board[row][col])
            row_set[row].add(board[row][col])
            sub[(row // 3, col // 3)].add(board[row][col])
    return True



