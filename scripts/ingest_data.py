import sqlite3
import pandas as pd

conn = sqlite3.connect("ecom.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    location TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    payment_date TEXT,
    amount REAL,
    mode TEXT,
    FOREIGN KEY(order_id) REFERENCES orders(id)
);
""")

# Load CSVs
customers = pd.read_csv("../data/customers.csv")
products = pd.read_csv("../data/products.csv")
orders = pd.read_csv("../data/orders.csv")
order_items = pd.read_csv("../data/order_items.csv")
payments = pd.read_csv("../data/payments.csv")

# Insert into DB
customers.to_sql('customers', conn, if_exists='append', index=False)
products.to_sql('products', conn, if_exists='append', index=False)
orders.to_sql('orders', conn, if_exists='append', index=False)
order_items.to_sql('order_items', conn, if_exists='append', index=False)
payments.to_sql('payments', conn, if_exists='append', index=False)

conn.commit()
conn.close()

print("Data inserted successfully into ecom.db!")
