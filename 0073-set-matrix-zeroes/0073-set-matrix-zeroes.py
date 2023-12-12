class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_zeros, col_zeros = [], []

        for i in range(m):
            row_zeros.append(False)

        for i in range(n):
            col_zeros.append(False)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_zeros[i] = True
                    col_zeros[j] = True

        for i in range(m):
            for j in range(n):
                if row_zeros[i] == True or col_zeros[j] == True:
                    matrix[i][j] = 0
