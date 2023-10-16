class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)
        for stock in range(0, length-1):
            if(prices[stock + 1] > prices[stock]):
                profit += prices[stock + 1] - prices[stock]
            
#         length = len(prices)
#         min_price = min(prices)
#         index_of_min = prices.index(min_price)
#         # print(length, min_price, index_of_min)
#         if(index_of_min + 1 == length):
#             return profit
#         else:
#             for stock in range(index_of_min, length-1):
#                 # print(stock)
#                 if(prices[stock + 1] > prices[stock]):
#                     profit += prices[stock + 1] - prices[stock]
                    
                
        return profit

            