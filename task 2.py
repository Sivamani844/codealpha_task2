stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"Added {stock} worth ${value}")
    else:
        print("Stock not found in list!")

print("\n💰 Total Investment Value: $", total_investment)
save = input("Do you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment Value: ${total_investment}")
    print("Result saved to portfolio.txt")
