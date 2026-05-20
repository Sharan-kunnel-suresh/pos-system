from app.database.db import connect
from tabulate import tabulate
def add_product(name,price,quantity):  # add a new poduct to the inventory
    conn =connect()
    cursor=conn.cursor()
    cursor.execute("""INSERT INTO PRODUCTS (name, price, quantity) VALUES (?, ?, ?)""", (name, price, quantity))
    conn.commit()
    conn.close()

    print (f"{name} added successfully to the inventory.")

def view_products():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    if not products:
        print("No products found.")
        return

    headers = ["ID", "Name", "Price", "Quantity"]

    print(tabulate(products, headers=headers, tablefmt="grid"))