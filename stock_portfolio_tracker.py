import csv
from datetime import datetime

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}

def display_stocks():
    print("\nAvailable Stocks:")
    print("-" * 30)
    for stock, price in STOCK_PRICES.items():
        print(f"{stock} : ₹{price}")
    print("-" * 30)

def add_stock():
    display_stocks()
    stock = input("Enter stock symbol: ").upper()

    if stock not in STOCK_PRICES:
        print("❌ Stock not available!")
        return

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("❌ Invalid quantity!")
        return

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print("✅ Stock added successfully!")

def view_portfolio():
    if not portfolio:
        print("\n📭 Portfolio is empty!")
        return

    print("\n📊 PORTFOLIO SUMMARY")
    print("-" * 55)
    print(f"{'Stock':<10}{'Qty':<10}{'Price':<10}{'Value':<10}")
    print("-" * 55)

    total_value = 0
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = qty * price
        total_value += value
        print(f"{stock:<10}{qty:<10}{price:<10}{value:<10}")

    print("-" * 55)
    print(f"💰 Total Investment Value: ₹{total_value}")
    print("-" * 55)

def save_to_file():
    if not portfolio:
        print("❌ Nothing to save!")
        return

    choice = input("Save as (1) TXT or (2) CSV: ")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if choice == "1":
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as file:
            file.write("Stock Portfolio Report\n")
            file.write("-" * 40 + "\n")
            total = 0
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                value = qty * price
                total += value
                file.write(f"{stock} | Qty: {qty} | Price: ₹{price} | Value: ₹{value}\n")
            file.write("-" * 40 + "\n")
            file.write(f"Total Investment: ₹{total}\n")

        print(f"✅ Portfolio saved as {filename}")

    elif choice == "2":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            total = 0
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                value = qty * price
                total += value
                writer.writerow([stock, qty, price, value])
            writer.writerow(["TOTAL", "", "", total])

        print(f"✅ Portfolio saved as {filename}")

    else:
        print("❌ Invalid choice!")

def main_menu():
    while True:
        print("\n📈 STOCK PORTFOLIO TRACKER")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Save Portfolio")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            save_to_file()
        elif choice == "4":
            print("👋 Thank you for using Stock Portfolio Tracker!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main_menu()
