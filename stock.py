import requests
import pandas as pd

# Your Alpha Vantage API Key (replace with your actual key)
API_KEY = "your_api_key_here"

# Define a function to fetch real-time stock data from Alpha Vantage
def get_stock_data(symbol):
    url = "https://www.alphavantage.co/query"
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Get the latest stock price
    if 'Time Series (5min)' in data:
        latest_time = list(data['Time Series (5min)'].keys())[0]
        latest_data = data['Time Series (5min)'][latest_time]
        close_price = float(latest_data['4. close'])
        return close_price
    else:
        print(f"Error retrieving data for symbol: {symbol}")
        return None

# Portfolio class to manage stocks
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
        
    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
        else:
            price = get_stock_data(symbol)
            if price is not None:
                self.portfolio[symbol] = {'quantity': quantity, 'average_price': price}
            else:
                print(f"Failed to fetch stock data for {symbol}. Stock not added.")
        
    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio and self.portfolio[symbol]['quantity'] >= quantity:
            self.portfolio[symbol]['quantity'] -= quantity
            if self.portfolio[symbol]['quantity'] == 0:
                del self.portfolio[symbol]
        else:
            print(f"Not enough shares of {symbol} to remove")
        
    def track_portfolio(self):
        portfolio_value = 0
        for symbol, data in self.portfolio.items():
            current_price = get_stock_data(symbol)
            if current_price is not None:
                portfolio_value += current_price * data['quantity']
        return portfolio_value
    
    def display_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return
        
        portfolio_df = pd.DataFrame.from_dict(self.portfolio, orient='index')
        portfolio_df['current_price'] = portfolio_df.index.map(get_stock_data)
        portfolio_df['total_value'] = portfolio_df['current_price'] * portfolio_df['quantity']
        print(portfolio_df)

# Main functionality to interact with the user
def main():
    portfolio = StockPortfolio()
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Track Portfolio Performance")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL, MSFT): ").upper()
            try:
                quantity = int(input("Enter number of shares: "))
                portfolio.add_stock(symbol, quantity)
                print(f"Added {quantity} shares of {symbol}")
            except ValueError:
                print("Invalid input. Please enter a numeric value for quantity.")
        
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            try:
                quantity = int(input("Enter number of shares to remove: "))
                portfolio.remove_stock(symbol, quantity)
                print(f"Removed {quantity} shares of {symbol}")
            except ValueError:
                print("Invalid input. Please enter a numeric value for quantity.")
        
        elif choice == '3':
            portfolio.display_portfolio()
        
        elif choice == '4':
            portfolio_value = portfolio.track_portfolio()
            print(f"Total portfolio value: ${portfolio_value:.2f}")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == '__main__':
    main()
