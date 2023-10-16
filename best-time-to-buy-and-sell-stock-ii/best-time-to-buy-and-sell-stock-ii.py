class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)
        for stock in range(0, length-1):
            if(prices[stock + 1] > prices[stock]):
                profit += prices[stock + 1] - prices[stock]                    
                
        return profit

            