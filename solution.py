from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        count = 0
        max_count = (len(matrix) * len(matrix[0])) / 2
        print(max_count)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):       
                temp = matrix[i][j]
                print(i, j)
                print(j, (len(matrix) - 1))
                print("")
                matrix[i][j] = matrix[j][(len(matrix) - 1) - i]
                matrix[j][(len(matrix) - 1) - i] = temp
                count += 1
                if count > max_count:
                    break
            if count > max_count:
                break
