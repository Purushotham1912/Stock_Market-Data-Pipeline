# Stock_Market-Data-Pipeline


#Goal:
## Fetch real-time stock market data using Yahoo Finance (yfinance)
## Store it in a PostgreSQL database
## Query the stored data for analysis

# Step 1: Data Source Selection
## We will scrape stock market data from Yahoo Finance using the yfinance Python library (which is more stable than traditional web scraping).

# Step 2: Extract Data (Web Scraping / API Call)
## Fetch real-time stock prices, historical data, volume, and market cap for selected stocks.
## Schedule the data extraction using cron jobs or Apache Airflow.

# Step 3: Data Processing & Cleaning
## Remove null values, convert timestamps, and ensure proper data types.
## Store clean data in PostgreSQL or AWS S3 (CSV format).

# Step 4: Store Data (Database / Cloud Storage)
## Use PostgreSQL to store structured data.
## Upload CSV files to AWS S3 for long-term storage.

# Step 5: Automate the Pipeline
## Use Apache Airflow (optional) to schedule daily stock data ingestion.

 # Tech Stack
## Python (yfinance, pandas, sqlalchemy)
## PostgreSQL (Database)
## Apache Airflow (For scheduling, optional)
