
def knapsack(W, weights, profits, n):

    # Create DP table
    dp = [[0 for j in range(W + 1)]
          for i in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    # Maximum profit
    max_profit = dp[n][W]

    # Find selected items
    selected_items = []
    w = W

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    print("\nMaximum Profit:", max_profit)
    print("Selected Items:", selected_items)


# Main program
n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    weight = int(input("Enter weight of item: "))
    profit = int(input("Enter profit of item: "))

    weights.append(weight)
    profits.append(profit)

W = int(input("Enter knapsack capacity: "))

knapsack(W, weights, profits, n)
