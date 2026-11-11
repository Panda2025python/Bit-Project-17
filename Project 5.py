print("================================")
print("TALLEST BAR SCANNER")
print("================================")

prices = [100, 180, 260, 310, 40, 535, 695]
print("\nPART 1 & 2: Stocks Buy-Sell & Profit")
print("Stock Prices:", prices)

profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        gain = prices[i] - prices[i - 1]
        profit += gain
        print(f"Buy at {prices[i - 1]}, Sell at {prices[i]}, Gain: {gain}")

print("Total Profit:", profit)

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(heights)

left_tallest = [0] * n
left_tallest[0] = heights[0]
for i in range(1, n):
    left_tallest[i] = max(left_tallest[i - 1], heights[i])

right_tallest = [0] * n
right_tallest[n - 1] = heights[n - 1]
for i in range(n - 2, -1, -1):
    right_tallest[i] = max(right_tallest[i + 1], heights[i])

print("\nPART 3 & 4: Tallest Bars")
print("Heights:      ", heights)
print("Left Tallest: ", left_tallest)
print("Right Tallest:", right_tallest)

water = 0
for i in range(n):
    water += min(left_tallest[i], right_tallest[i]) - heights[i]

print("\nPART 5: Rainwater Trapped")
print("Total Rainwater Trapped:", water)

print("\n================================")
print("TALLEST BAR SCANNER SUMMARY")
print("================================")
print("Stock profit was calculated by adding every positive price difference.")
print("Left tallest bars store the highest bar seen from the left side.")
print("Right tallest bars store the highest bar seen from the right side.")
print("Rainwater is calculated using the smaller value from left and right tallest bars.")
print("================================")
