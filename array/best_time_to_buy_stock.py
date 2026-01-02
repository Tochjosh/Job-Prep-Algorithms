

def max_profit(prices: list[int]) -> int:
    """
    Problem:
    You are given an array of `prices` where `prices[i]` is the price of a given
    stock on the i-th day.

    You want to maximize your profit by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.

    Examples:
    Example 1:
        Input: prices = [7, 1, 5, 3, 6, 4]
        Output: 5
        Explanation:
            Buy on day 2 (price = 1) and sell on day 5 (price = 6),
            profit = 6 - 1 = 5.
            Buying on day 2 and selling on day 1 is not allowed because
            you must buy before you sell.

    Example 2:
        Input: prices = [7, 6, 4, 3, 1]
        Output: 0
        Explanation:
            No transactions are done and the maximum profit is 0.

    Constraints:
        1 <= prices.length <= 10^5
        0 <= prices[i] <= 10^4
    """
    profit = 0
    min_sell = prices[0]

    for price in prices:
        # Update the min sell price so far
        if price < min_sell:
            min_sell = price
        # Find the best gain so far
        gain = price - min_sell
        if gain > profit:
            profit = gain
    return profit


print(max_profit([7,1,5,3,6,4]))






