# Problem: https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maximum = max(maximum, currSum)
        return maximum
