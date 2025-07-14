# Question: Given an amount and a list of coin denominations, find the number of ways to make change for the given amount.

def count_coin_change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

amount = 5
coins = [1, 2, 5]
print(count_coin_change(amount, coins))
