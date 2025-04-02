import unittest
from solution import Solution  # Import the Solution class from solution.py

class TestRotateImage(unittest.TestCase):
    def test_basic_case(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        Solution().rotate(matrix)
        expected = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        self.assertEqual(matrix, expected)

    def test_small_matrix(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        Solution().rotate(matrix)
        expected = [
            [3, 1],
            [4, 2]
        ]
        self.assertEqual(matrix, expected)

    def test_large_matrix(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        Solution().rotate(matrix)
        expected = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
        self.assertEqual(matrix, expected)

    def test_single_element_matrix(self):
        matrix = [[1]]
        Solution().rotate(matrix)
        expected = [[1]]
        self.assertEqual(matrix, expected)

    def test_empty_matrix(self):
        matrix = []
        Solution().rotate(matrix)
        expected = []
        self.assertEqual(matrix, expected)

if __name__ == "__main__":
    unittest.main()