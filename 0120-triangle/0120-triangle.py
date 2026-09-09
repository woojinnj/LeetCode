class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * len(row) for row in triangle]

        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] =triangle[i][j]+ dp[i - 1][0]
                elif j == (len(triangle[i]) - 1):
                    dp[i][j] =triangle[i][j]+ dp[i - 1][i - 1]
                else:
                    dp[i][j] =triangle[i][j]+ min(dp[i - 1][j - 1], dp[i - 1][j])

        answer = min(dp[n - 1])
        return answer
