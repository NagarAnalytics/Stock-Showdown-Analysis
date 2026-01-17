import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

'''# Download data for Apple and Nvidia
# We grab 'Close' prices only to keep it simple
tickers = ['AAPL', 'NVDA']
data = yf.download(tickers, start='2024-01-01', end='2026-01-01')['Close']

# Peek at the data
print(data.head())

# Get the prices from the very first day
first_day_prices = data.iloc[0]

# Divide every row by the first day's prices
# This "normalizes" the data
normalized_data = data / first_day_prices

# Plot it to see the "Showdown"
normalized_data.plot(figsize=(10,6))
plt.title('Stock Showdown: AAPL vs NVDA (Growth of $1)')
plt.ylabel('Relative Value')
plt.show()

# Calculate daily returns
daily_returns = data[['AAPL', 'NVDA']].pct_change()

# Find the date of the worst daily drop
worst_day_aapl = daily_returns['AAPL'].idxmin()
worst_day_nvda = daily_returns['NVDA'].idxmin()

# Find the actual percentage loss on those days
loss_aapl = daily_returns['AAPL'].min()*100
loss_nvda = daily_returns['NVDA'].min()*100

print(f"Apple's worst day was {worst_day_aapl.date()} with a {loss_aapl:.2f}% drop.")
print(f"Nvidia's worst day was {worst_day_nvda.date()} with a {loss_nvda:.2f}% drop.")'''

# The "Stock Showdown" Function
def compare_stocks(ticker1, ticker2, start_date):
    # 1. Download Data
    tickers = [ticker1, ticker2]
    data = yf.download(tickers, start=start_date)['Close']

    # 2. Normalize (Growth of $1)
    normalized = data / data.iloc[0]

    # 3. Calculate Daily Returns & Volatility
    returns = data.ffill().pct_change()
    vol = returns.std()

    # 4. Find Correlation
    corr_value = returns[ticker1].corr(returns[ticker2])

    # --- VISUALIZE ---
    plt.figure(figsize=(12, 6))
    plt.plot(normalized[ticker1], label=f"{ticker1} (Growth)")
    plt.plot(normalized[ticker2], label=f"{ticker2} (Growth)")

    plt.title(f"Showdown: {ticker1} vs {ticker2} (Corr: {corr_value:.2f})")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Total Percentage Return
    First_Price = data.iloc[0]
    Last_Price = data.iloc[-1]

    Total_Return = (Last_Price / First_Price) - 1

    # --- REPORT ---
    print(f"--- Analysis for {ticker1} vs {ticker2} ---")
    print(f"Volatility (Risk): \n{vol}")
    print(f"\nCorrelation: {corr_value:.2f}")
    print(f"Total Percentage Return: {Total_Return}")

# NOW YOU CAN USE IT LIKE THIS:
compare_stocks('AAPL', 'NVDA', '2025-01-01')







