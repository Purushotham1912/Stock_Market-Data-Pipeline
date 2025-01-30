## Data Visualization
# Now that your data is clean and stored in the database, let's visualize it.

# You can use Power BI or Python's Matplotlib/Seaborn to create visualizations of your stock data.

✅ Example: Visualize Stock Data with Python
Here’s a simple Python code to plot closing prices and moving averages:

python
Copy
Edit
import matplotlib.pyplot as plt
import seaborn as sns

#  Set plot style
sns.set(style="darkgrid")

#  Plot the closing prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data['datetime'], stock_data['close_price'], label="Close Price", color='blue')

#  Calculate and plot a moving average (e.g., 5-period moving average)
stock_data['moving_avg'] = stock_data['close_price'].rolling(window=5).mean()
plt.plot(stock_data['datetime'], stock_data['moving_avg'], label="5-Period Moving Avg", color='red')

#  Customize the plot
plt.title('Stock Closing Prices and Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()
# This will give you a time series plot of closing prices with a 5-period moving average.
