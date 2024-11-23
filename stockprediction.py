# %% [markdown]
# # Hack the Market OA 2024 - Question 1
# 
# This question consists of two parts (one coding and one written).
# 
# ## Part 1: Stock Price Prediction
# 
# You are given an array of integers `prices` representing the daily stock prices of a company. Write a function called `stockPricePrediction` that returns an integer array such that `answer[i]` is the number of days you have to wait after the `i`th day to see a higher stock price. If there is no future day with a higher price, keep `answer[i] == 0` instead.
# 
# ### Example 1:
# Input: `prices = [100, 101, 102, 99, 98, 101, 103, 100]`
# 
# Output: `[1, 1, 4, 2, 1, 1, 0, 0]`
# 
# Explanation: On the first day (price = 100), you have to wait 1 day to get a higher price (101). Similarly, for the second day (101), the next higher price (102) occurs after 1 day. On the third day (102), it takes 4 days to see a higher price (103), and so on.
# 
# ### Example 2:
# Input: `prices = [30, 40, 50, 60]`
# 
# Output: `[1, 1, 1, 0]`
# 
# Explanation: On each day, the stock price is higher the next day, except for the last day.
# 
# ### Example 3:
# Input: `prices = [90, 60, 30]`
# 
# Output: `[0, 0, 0]`
# 
# Explanation: On the first day (price = 90), there are no future days with a higher price. On the second day (price = 60), there are also no future days with a higher price. Similarly, on the third day (price = 30), there are no future days with a higher price.
# 
# ### Constraints:
# - `1 <= prices.length <= 10^6`
# 
# - `1 <= prices[i] <= 1000`
# 
# ### Requirements:
# 
# - You must define and implement a function called `stockPricePrediction`.
# 
# - The cummulative runtime of all test cases should be less than 5 seconds.
# 
# - Leave useful comments in your solution.

# %%
# Your Code Here

def stockPricePrediction(prices):
    """
    Returns an array indicating the number of days needed to wait for a higher price.

    :param prices: List[int], the stock prices on each day.
    :return: List[int], where each element represents the number of days to wait for a higher price.
    """
    n = len(prices)
    answer = [0] * n  # Initialize the answer array with 0s
    stack = []  # This will store indices of days in a decreasing price order

    for i in range(n):
        # While stack is not empty and the current price is greater than the price
        # at the index stored at the top of the stack
        while stack and prices[i] > prices[stack[-1]]:
            prev_day = stack.pop()  # Get the index of the day with a smaller price
            answer[prev_day] = i - prev_day  # Calculate the difference in days
        # Push the current index onto the stack
        stack.append(i)

    # Any remaining indices in the stack will naturally have 0 in the answer array
    # since there is no future day with a higher price.

    return answer

# %% [markdown]
# 

# %%
# Unit testing cell (feel free to modify this and/or add more tests as needed)

prices1 = [100, 101, 102, 99, 98, 101, 103, 100]
prices2 = [30, 40, 50, 60]
prices3 = [90, 60, 30]

assert stockPricePrediction(prices1) == [1, 1, 4, 2, 1, 1, 0, 0]
assert stockPricePrediction(prices2) == [1, 1, 1, 0]
assert stockPricePrediction(prices3) == [0, 0, 0]

# %% [markdown]
# ## Part 2: Time/Space Complexity Analysis
# 
# State the time/space complexity (Big O notation) of your algorithm in part 1 provide a 1-2 sentence explanation.
# 
# Time Complexity: O()
# 
# Space Compleity: O()
# 
# Explanation: (double click to edit)


