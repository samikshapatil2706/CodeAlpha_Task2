stock_prices = {
    "RELIANCE": 3050,    # Reliance Industries Ltd.
    "TCS": 3800,         # Tata Consultancy Services
    "INFY": 1600,        # Infosys Ltd.
    "HDFCBANK": 1650,    # HDFC Bank
    "ICICIBANK": 1100,   # ICICI Bank
    "HINDUNILVR": 2600,  # Hindustan Unilever Ltd.
    "ITC": 450,          # ITC Ltd.
    "MRF": 132500        # MRF Ltd. (Most expensive stock in India)
}

stock_full_names = {
    "RELIANCE": "Reliance Industries Ltd.",
    "TCS": "Tata Consultancy Services",
    "INFY": "Infosys Ltd.",
    "HDFCBANK": "HDFC Bank",
    "ICICIBANK": "ICICI Bank",
    "HINDUNILVR": "Hindustan Unilever Ltd.",
    "ITC": "ITC Ltd.",
    "MRF": "MRF Ltd."
}

#  Initialize portfolio
portfolio = {}
total_value = 0

#  Styled input instructions
print("\n" + "=" * 60)
print("STOCK ENTRY MODE")
print("=" * 60)
print("Enter stock symbol (e.g., TCS), then quantity.")
print("Type 'done' to finish entering stocks.")
print("\nAvailable Stocks:\n")

#   Display available stock list
for ticker, full_name in stock_full_names.items():
    print(f"  {ticker:<12} - {full_name} (₹{stock_prices[ticker]})")

#  Take user input
while True:
    stock = input("\nStock name: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Invalid stock symbol. Please choose from the list above.")
        continue
    try:
        qty = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("Invalid number. Please enter a valid quantity.")

#   Display formatted portfolio summary
print("\n" + "=" * 60)
print("PORTFOLIO SUMMARY")
print("=" * 60)
print(f"{'Symbol':<12} | {'Company':<30} | Summary")
print("-" * 70)

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock:<12} | {stock_full_names[stock]:<30} | {qty} shares × ₹{price} = ₹{value}")

print(f"\nTotal Investment: ₹{total_value}")

#   Save to file (optional)
save = input("\nDo you want to save this summary to a file? (y/n): ").lower()
if save == 'y':
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary (India)\n")
        file.write("----------------------------------\n")
        file.write(f"{'Symbol':<12} | {'Company':<30} | Summary\n")
        file.write("-" * 70 + "\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock:<12} | {stock_full_names[stock]:<30} | {qty} shares × ₹{stock_prices[stock]} = ₹{value}\n")
        file.write(f"\nTotal Investment: ₹{total_value}\n")
    print("Summary saved to 'portfolio_summary.txt'")
else:
    print("File not saved. Exiting program.")
