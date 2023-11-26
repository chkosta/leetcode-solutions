class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(lst):
            tmp_lst = []
            for item in lst:
                if item != "." and item in tmp_lst:
                    return False
                tmp_lst.append(item)
            return True

        for row in board:
            if not isValid(row):
                return False

        for col in zip(*board):
            if not isValid(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not isValid(sub_box):
                    return False

        return True
        