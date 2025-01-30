# Data Cleaning & Transformation (ETL Process)
# In real-world projects, you need to clean and transform the data before using it for analysis or visualization.

# Here, we will focus on cleaning your stock data to ensure it's ready for analysis.

 ## Data Cleaning
# We can clean the stock data by:

# Handling missing values: Incomplete data, like missing stock prices, needs to be handled.
# Correcting data types: Ensure the data types are consistent (e.g., datetime, float).
# Code to Handle Missing Values

# Fill missing values (if any) with forward fill or a specific value like 0
stock_data.fillna(method='ffill', inplace=True)  # Forward fill to fill missing values

# Drop rows with missing critical data
stock_data.dropna(subset=['open_price', 'close_price'], inplace=True)
# Forward Fill: Propagates the previous value forward.
# Drop NaN Rows: Removes rows that have missing values in important columns (like price).
# Code to Ensure Correct Data Types

# Ensure 'datetime' is in the correct format
stock_data['datetime'] = pd.to_datetime(stock_data['datetime'])

# Convert stock prices to float (if they are not already)
stock_data['open_price'] = stock_data['open_price'].astype(float)
stock_data['close_price'] = stock_data['close_price'].astype(float)

# Data Transformation
# Transformation might include aggregating data or adding calculated fields like percentage change, moving averages, etc.

# Example: Add Percentage Change (Price Change)

# Calculate percentage change in close price
stock_data['price_change'] = stock_data['close_price'].pct_change() * 100  # Percentage change
# Save the Cleaned Data
# You can store the cleaned and transformed data back into PostgreSQL or export it for analysis.

# Save Cleaned Data to PostgreSQL

# Store cleaned data back into PostgreSQL
stock_data.to_sql('stocks_cleaned', engine, if_exists='replace', index=False)
