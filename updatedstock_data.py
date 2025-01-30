# Modify Python Script to Store Data

# Now, update stock_data.py to save the stock data into PostgreSQL:

# ----python code ----
import yfinance as yf
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Define the stock symbol (e.g., Tesla - TSLA)
stock_symbol = "TSLA"

# Fetch stock data
stock = yf.Ticker(stock_symbol)
stock_data = stock.history(period="1d", interval="1h")  # Last 1 day's data, hourly intervals
stock_data.reset_index(inplace=True)

# Database connection parameters
DB_NAME = "stock_data"
DB_USER = "postgres"
DB_PASSWORD = "your_password"  # Replace with your PostgreSQL password
DB_HOST = "localhost"
DB_PORT = "5432"

# Create database engine
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Rename columns to match PostgreSQL table
stock_data = stock_data[['Datetime', 'Open', 'High', 'Low', 'Close', 'Volume']]
stock_data.columns = ['datetime', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']

# Insert data into PostgreSQL
stock_data.to_sql('stocks', engine, if_exists='append', index=False)

print("Data successfully stored in PostgreSQL!")
