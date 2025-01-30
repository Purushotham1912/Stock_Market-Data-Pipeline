# Create a Database & Table
# Open pgAdmin 4 and connect to your PostgreSQL server.
# Click on Databases → Create Database → Name it stock_data.
# Open the Query Tool and run this SQL to create a table:

CREATE TABLE stocks (
    datetime TIMESTAMP PRIMARY KEY,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    volume BIGINT
);
