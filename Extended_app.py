@app.route('/stock_data/<start_date>/<end_date>', methods=['GET'])
def get_stock_data_by_date(start_date, end_date):
    conn = psycopg2.connect(
        host="localhost",
        database="stock_db",
        user="your_user",
        password="your_password"
    )
    cursor = conn.cursor()
    
    query = """
    SELECT * FROM stocks_cleaned
    WHERE datetime BETWEEN %s AND %s;
    """
    cursor.execute(query, (start_date, end_date))
    rows = cursor.fetchall()

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

    cursor.close()
    conn.close()

    return jsonify(stock_data)
