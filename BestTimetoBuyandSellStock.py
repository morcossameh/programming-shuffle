# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        maximum = 0

        for i in range(1, len(prices)):
            diff = prices[i] - currMin
            maximum = max(maximum, diff)

            if prices[i] < currMin:
                currMin = prices[i]
        
        return maximum
