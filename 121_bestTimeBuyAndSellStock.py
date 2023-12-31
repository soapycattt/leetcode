class Solution:
    """
    121. Best Time to Buy and Sell Stock 
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    
    Tag: array
    """
    def maxProfit(self, prices: list[int]) -> int:
        """
        Start off with 2 values at index 0, and 1
        We'll take difference of the right index to the left index
        If it's positive, select the max between the difference and the current maxProfit move the right pointer
        If it's negative, it means that the right pointer is at the currentMin of the array,
        so move the left pointer at the right pointer index, then move the right pointer forward by 1 index
        Run it till the right index is out of index
        """

        leftIdx = 0
        rightIdx = 1
        maxProfit = 0

        while rightIdx < len(prices):
            difference = prices[rightIdx] - prices[leftIdx]

            if difference > 0:
                maxProfit = max(maxProfit, difference)
            
            else:
                leftIdx = rightIdx
    
    def maxProfit(prices: list[int]) -> int: 
        """
        Trader POV:
        - Update local minima up find the the current day stock lower than the tracked day 
        - Keep track of maximum profit. 
        - If today profit increases, then hold and wait to the next day
        - If today profit decreases, still hold 
        -> If the difference is positive -> profit -> hold till the next day
        -> Else, then update the local minima to the current day, 
        -> Always move the latter pointer up by  1 position
        """
        profit = 0 
        p1 = 0 
        p2 = 1
        while p2 < len(prices): 
            # Get max profit for the current day
            diff = prices[p2] - prices[p1]
            profit = max(profit, diff)

            # If current day stock is lower than the current sell day. Switch the sell day to current day
            if diff < 0:  
                p1 = p2 
            
            p2 += 1 
    
    
    def maxProfit(self, prices: List[int]) -> int:
        """
        - I need biggest different from right pointer minus left pointer
        - If I got profit, I tend to hold my stock as long as possible -> move right pointer
        - If the stock at the curr day is lower than my prev sell day, I'd love to buy stock at the curr day -> move left pointer to the curr day if it's lower than left pointer

        Sliding window: 
            - Constrain metric: difference between 2 values
            - Numeric restriction of metric(to update left pointer): diff must be > 0
            - Most valid answer: maximum of profit 
        """
        buy = prices[0]
        profit = 0 

        for sell in prices[1:]:
            diff = sell - buy
            profit = max(profit, diff)
            
            if diff < 0:
                buy = sell
        
        return profit
