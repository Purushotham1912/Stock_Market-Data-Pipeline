# "Fetch Stock Data from Yahoo Finance":

# Here’s a Python script to get real-time stock data for a company (e.g., Tesla – TSLA):

# ----python code-----

import yfinance as yf
import pandas as pd

# Define the stock symbol (e.g., Tesla - TSLA)
stock_symbol = "TSLA"

# Fetch stock data
stock = yf.Ticker(stock_symbol)
stock_data = stock.history(period="1d", interval="1h")  # Last 1 day's data, hourly intervals

# Reset index to keep timestamps as a column
stock_data.reset_index(inplace=True)

# Display the first few rows
print(stock_data.head())

# Explanation:

# This fetches Tesla’s stock price for the last day at hourly intervals.
# You can change period="5d" to get 5 days of data.
# The reset_index() function ensures that the timestamp is stored as a column.
