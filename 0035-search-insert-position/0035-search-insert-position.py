class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1

        if nums[right]<target:
            return right+1
        if nums[left]>target:
            return 0

        while left<=right:
            mid=(left+right)//2
            if left==right:
                if nums[left]<target:
                    return left+1
                else:
                    return left
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>=target:
                right=mid-1
    
        return mid