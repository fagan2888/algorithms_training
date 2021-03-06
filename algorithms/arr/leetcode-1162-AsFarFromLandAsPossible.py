
'''
1162. 地图分析
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。

我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。

如果我们的地图上只有陆地或者海洋，请返回 -1。

 

示例 1：



输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释： 
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
示例 2：



输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释： 
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
 

提示：

1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1

1162. As Far from Land as Possible
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:



Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:



Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1
'''




class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_len = len(grid)
        col_len = len(grid[0])
        dp = [[float("inf") for i in range(row_len)] for j in range(col_len)]
        # dp = [[0 if grid[i][j]==1 else float("inf") for i in range(row_len)] for j in range(col_len)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dp[i][j] = 0
        #         else:
        #             dp[i][j] = float("inf")
        # print(dp)
        # print([[0 if grid[i][j]==1 else float("inf") for i in range(row_len)] for j in range(col_len)])
        # print([[0 if grid[i][j] else float("inf") for i in range(row_len)] for j in range(col_len)] == dp)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    dp[i][j] = 0
                    continue
                if i-1 >= 0:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j])
                if j-1 >= 0:
                    dp[i][j] = min(dp[i][j-1]+1, dp[i][j])
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j]==1:
                    dp[i][j] = 0
                    continue
                if i+1 < row_len:
                    dp[i][j] = min(dp[i+1][j]+1, dp[i][j])
                if j+1 < col_len:
                    dp[i][j] = min(dp[i][j+1]+1, dp[i][j])
        res = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res = max(res, dp[i][j])
        return res if res != float("inf") else -1




if __name__ == '__main__':
    demo = Solution()
    demo.maxDistance([[1,0,1],[0,0,0],[1,0,1]])


    # [[1,0,1],[0,0,0],[1,0,1]]
    # [[1,0,0],[0,0,0],[0,0,0]]
    # [[1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,0,1,0,1,1,1,0],[1,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,1,0],[1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1],[0,1,1,1,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0],[0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,1,0,0],[0,0,0,1,1,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1],[1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1],[1,0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1,0],[1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,0,0,1,0,1,1,0,1,0,1,1,1],[0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0],[1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1],[1,1,1,0,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0],[0,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1],[1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,1],[1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1],[1,1,0,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1],[1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0],[1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0],[0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0],[1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0],[0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0],[0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,1,1,0],[0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0],[0,0,0,1,0,1,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1],[1,0,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1],[0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0],[1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1],[0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,1,1],[1,0,0,1,0,0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],[1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1],[1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1],[0,1,0,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1],[1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1],[1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0]]

    # [[1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,0,1,0,1,1,1,0],[1,0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,1,0],[1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1],[0,1,1,1,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0],[0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,1,1,0,0],[0,0,0,1,1,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1],[1,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1],[1,0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1,0],[1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,0,0,1,0,1,1,0,1,0,1,1,1],[0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0],[1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1],[1,1,1,0,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0],[0,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1],[1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,1],[1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1],[1,1,0,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,1],[1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0],[1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0],[0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0],[1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0],[0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0],[0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,1,1,0],[0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,0,0],[0,0,0,1,0,1,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1],[1,0,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,0,0,0,1],[0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0],[1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1],[0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,1,1,1],[1,0,0,1,0,0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],[1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1],[1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1],[0,1,0,0,0,1,1,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,1],[1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1],[1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0]]
    # [[0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1],[1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,1,0,1],[1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0],[0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1],[1,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0],[1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0],[1,1,1,1,0,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,0],[1,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1],[0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,1,0,1],[0,0,0,0,1,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1],[1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1,0],[0,0,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1],[0,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1],[0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1],[0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1],[0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,1,1,1],[1,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0],[1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,1,1,0,0,1],[1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,1],[1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1],[1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1],[0,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0],[0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1],[0,1,0,1,0,0,0,0,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1],[1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,0],[0,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0],[0,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1],[0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0],[1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,0,0],[0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0,0]]
    # [[0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1],[1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,1,0,1],[1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0],[0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1],[1,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0],[1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0],[1,1,1,1,0,1,1,0,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,1,0,0],[1,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1],[0,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,1,0,1],[0,0,0,0,1,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1],[1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1,0],[0,0,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1],[0,1,1,1,0,0,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1],[0,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1],[0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1],[0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,1,0,1,1,1,1],[1,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0],[1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,1,1,0,0,1],[1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,0,1],[1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1],[1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1],[0,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0],[0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1],[0,1,0,1,0,0,0,0,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1],[1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,1,1,0],[0,1,0,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0],[0,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1],[0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,0],[1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,0,0],[0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0,0]]