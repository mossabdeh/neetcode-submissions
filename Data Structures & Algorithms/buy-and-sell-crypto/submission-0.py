class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = set()
        for i in range(len(prices)):
            for j in range(i+1 , len(prices)):
                if prices[i] < prices[j] :
                    profit.add(prices[j] - prices[i])

        return max(profit) if len(profit) > 0  else 0
                    
        