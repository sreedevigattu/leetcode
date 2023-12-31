'''
121. Best Time to Buy and Sell Stock
ou are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
from typing import List

def maxProfit(prices: List[int]) -> int:
    profits = []

    loop = 0
    while len(prices) > 0:
        loop += 1
        print(f"\nLoop {loop}")
        print("prices: ", len(prices), prices)
        buy = min(prices)
        min_index = prices.index(buy)
        print("buy, min_index", buy, min_index)

        prices_rest = prices[min_index+1:]
        print("len(prices_rest), prices_rest", len(prices_rest), prices_rest)
        sell = 0
        if len(prices_rest) > 0:
            sell = max(prices_rest)
            max_index = prices.index(sell)
            print("sell, max_index", sell, max_index)

        profit = sell-buy if sell > buy else 0
        profits.append(profit)
        prices = prices[:min_index]
    
    profit = max(profits)
    return profit

#profit = maxProfit([2,4,1])
#print(profit)

import numpy as np
nums = [1, 2, 3, 4] # [24, 12, 8, 6]
print("nums", nums)
nums_len = len(nums)
prefix, postfix = 1, 1
#pre = [1] * nums_len
#post = [1] * nums_len
sol = [1] * nums_len
pr = 1
#for i in range(nums_len):
#    j = nums_len-i-1
for i, j in zip(range(nums_len), range(nums_len-1,-1,-1)):

    sol[i] *= prefix
    prefix *= nums[i]
    #pre[i] = prefix

    sol[j] *= postfix
    postfix *= nums[j]
    #post[j] = postfix

    print(i, j, prefix, postfix)

    '''print("pre", pre)
    print("post", post)'''
    print("sol", sol)

