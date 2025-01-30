from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Define the route to get stock data
@app.route('/stock_data', methods=['GET'])
def get_stock_data():
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",        # PostgreSQL host (usually localhost)
        database="stock_db",     # Your database name
        user="your_user",        # Your PostgreSQL username
        password="your_password" # Your PostgreSQL password
    )
    cursor = conn.cursor()
    
    # Query to fetch stock data
    cursor.execute("SELECT * FROM stocks_cleaned LIMIT 10;")
    rows = cursor.fetchall()
    
    # Format the result into a dictionary
    stock_data = []
    for row in rows:
        stock_data.append({
            'datetime': row[1],
            'open_price': row[2],
            'high_price': row[3],
            'low_price': row[4],
            'close_price': row[5],
            'volume': row[6]
        })

    # Close the database connection
    cursor.close()
    conn.close()

    # Return the data as JSON
    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(debug=True)
