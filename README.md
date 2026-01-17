# Stock-Showdown-Analysis
# Stock Showdown: Comparative Asset Analysis Tool

![Stock Showdown Chart](comparison_chart.png)

## 📊 Project Overview
I built this tool to analyze the performance of various assets (Stocks, Crypto, Gold) against the S&P 500 benchmark. It handles the "messy" reality of finance data, such as differing market hours and high volatility.

## 🛠️ Skills Demonstrated
* **Time-Series Analysis**: Normalizing prices to compare assets with different starting values.
* **Data Cleaning**: Handling missing values (NaNs) in cross-market data using forward-filling.
* **Quantitative Metrics**: Calculating Daily Returns, Volatility (Risk), and Correlation.
* **Visualization**: Plotting multi-asset growth charts with Matplotlib.

## 🚀 How it Works
The function `compare_stocks(ticker1, ticker2, start_date)` pulls live data from Yahoo Finance, scales it to a "Growth of $1" basis, and identifies how closely two assets move together relative to the S&P 500.

## 📈 Sample Output
*Calculates total percentage returns and visualizes risk-reward trade-offs.*
