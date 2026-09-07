class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[1]*(n+1)
        for i in range(1,n):
            m=0
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j]>m:
                        m=dp[j]
            dp[i]=m+1
        return max(dp)