##### TODO 1 #####
def price_to_profit(L): 
    profits = [0]
    for i in range(1, len(L)):
        profit = L[i] - L[i-1]
        profits.append(profit)
    return profits

# brute force solution
def max_profit_brute(L):
    """Finds maximum profit. Assumes L is a list of profits (i.e. change in price every day), not raw prices"""
    n = len(L)
    max_sum = 0 # assume we can at least break even - buy and sell on the same day

    # outer loop finds the max profit for each buy day
    for i in range(n):
       # total profit if we bought on day i and sold on day j
        total = L[i]
        if total > max_sum: max_sum = total
        
        for j in range(i+1, n): 
            total += L[j] # total profit if we sell on day j
                          # we assume L[j] is the profit if we bought on day j-1 and sold on day j
                          # i.e., L is the change in value each day, relative to the day before
            if total > max_sum: max_sum = total

    return max_sum


##### TODO 2 #####
# you'll need a helper function or default parameters here
def max_profit(L, left, right):  # O(nlogn)
    if left >= right:
        return 0 
    # BASE CASE
    #    Only 1 item? Max profit is easy - it's the profit if we bought the day before and sold today
    mid = (left + right) // 2
    max_profit_left = max_profit(L, left, mid)
    max_profit_right = max_profit(L, right, mid)

    max_profit_crossing(L, left, right, mid)

    return max(max_profit_left, max_profit_right, max_profit_crossing)

    # DIVIDE into three problems and CONQUER:
    #    find the max profit if we buy and sell in the left (recursive call)
    #    find the max profit if we buy and sell in the right (recursive call)
    #    find the max profit if we buy in the left and sell in the right (requires a separate function)

    # COMBINE subproblems into the solution for this level of recursion
    #    Which of the above three scenarios gives the best profit?

##### TODO 3 #####
def max_profit_crossing(L, left, right, median):
    pass
   # O(n): Max profit if we sell on the median?
   
   # O(n): Max profit if we buy on the median?

   # O(1): Max profit if we buy before and sell after?