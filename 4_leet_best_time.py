# You cannot sell a stoc before you buy one
# stock that will give us the most profit in a historic data set

from typing import List
import time

'''
Example

Input: [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5

(price = 6), profit = 6 - 1 = 5,
            Not 7 - 1 =6, as selling price needs to be larger than buy price
'''

class Solution:
    
    ''' are there other restrintions ? 
    1. Memory restrinctions?
    2. The data set size can change?
    3. Is it stored in memory?
    4. the type of the value while be the same?
    '''
        
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price

            current_profit =  price - min_price 
            
            if current_profit > max_profit:
                max_profit = current_profit
            
        return max_profit, min_price
    
    def maxProfitV2(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit


# TEST

# Testing the Solution
if __name__ == "__main__":
    # Function to measure execution time
    def measure_execution_time(func, *args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        return result, end_time - start_time

    # Test case 1
    test_case_1 = [7, 1, 5, 3, 6, 4]
    print(f"Original: {test_case_1}")
    (max_profit, min_price), execution_time = measure_execution_time(Solution().maxProfit, test_case_1)
    print(f"Max Profit: {max_profit}")  # Expected: 5 (Buy at 1, sell at 6)
    print(f"Min Price: {min_price}")  # Expected: 5 (Buy at 1, sell at 6)
    print(f"Execution Time: {execution_time:.10f} seconds")
    
        # Test case 1
    test_case_2 = [7, 1, 5, 3, 6, 4]
    print(f"Original: {test_case_2}")
    (max_profit), execution_time = measure_execution_time(Solution().maxProfitV2, test_case_2)
    print(f"Max Profit: {max_profit}")  # Expected: 5 (Buy at 1, sell at 6)
    print(f"Execution Time: {execution_time:.10f} seconds")


'''

Comparison and Conclusion
Both functions maxProfit and maxProfitV2 have the same time and space complexities:

Time Complexity: O(n)
This is due to the single iteration over the input list, which makes both functions efficient in terms of time.
Space Complexity: O(1)
Both functions only use a constant amount of extra memory.
While the algorithms are similar in complexity, maxProfitV2 is slightly more concise by using Python's built-in min and max functions, which may also make the code slightly easier to read and maintain.

'''