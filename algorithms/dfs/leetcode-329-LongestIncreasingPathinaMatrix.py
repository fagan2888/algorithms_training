'''
329. Longest Increasing Path in a Matrix
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

329. 矩阵中的最长递增路径
给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
'''


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        if not matrix:
            return 0

        self.res_map = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        self.max_val = 1

        def dfs(i, j):
            if self.res_map[i][j] != 0:
                return self.res_map[i][j]
            add_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            res = 1
            for add_i, add_j in add_list:
                x = i + add_i
                y = j + add_j
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                    tmp = dfs(x, y) + 1 if matrix[x][y] > matrix[i][j] else 1
                    if tmp > res:
                        res = tmp
            if res > self.max_val:
                self.max_val = res
            self.res_map[i][j] = res
            return res

        res = 1

        return max(dfs(i, j) for j in range(len(matrix[0])) for i in range(len(matrix)))
