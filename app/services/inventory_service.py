from database.db import connect
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

def restock_product(product_id,added_quantity):
    conn=connect()
    cursor=conn.cursor()
    cursor.execute("SELECT name,quantity FROM products WHERE id=?", (product_id,))
    product=cursor.fetchone()
    if not product:
        print("Product not found.")
        conn.close()
        return
    name,stock=product
    new_stock=stock+added_quantity
    cursor.execute("""        
    UPDATE products SET quantity=?
                    WHERE id=?
    """,(new_stock,product_id))#update the quantity in the products table
    conn.commit()
    conn.close()

    print(f"{name} restocked successfully. New quantity: {new_stock}")
    print(f"Added {added_quantity} units to {name}. Total quantity: {new_stock} ")
    
def search_product(keyword):
        conn=connect()
        cursor=conn.cursor()

        cursor.execute(" SELECT * FROM products WHERE name LIKE?",(f"%{keyword}%",))
        
        products=cursor.fetchall()

        conn.close()
        if not products:
            print("there is no products matching ") 
            return
        headers=["ID","Name","Price","Quantity"]
        print(tabulate(products,headers=headers,tablefmt="grid"))
'''
    def product_sort_by_name():
        conn=connect()
        cursor=conn.cursor()

        cursor.execute("SELECT * FROM products ORDER BY name")
        products=cursor.fetchall()

        conn.close()
        if not products:
            print("No products found.")
            return
        headers=["ID","Name","Price","Quantity"]
        print(tabulate(products,headers=headers,tablefmt="grid"))
        
'''
def update_product(product_id, name=None, price=None, quantity=None):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, price, quantity FROM products WHERE id=?",
        (product_id,)
    )

    product = cursor.fetchone()

    if not product:
        print("Product not found.")
        conn.close()
        return
    current_name, current_price, current_quantity = product

    if price is not None and price < 0:
        print("Price cannot be negative.")
        conn.close()
        return

    if quantity is not None and quantity < 0:
        print("Quantity cannot be negative.")
        conn.close()
        return

    new_name = name if name is not None else current_name
    new_price = price if price is not None else current_price
    new_quantity = quantity if quantity is not None else current_quantity

    cursor.execute("""
        UPDATE products
        SET name=?, price=?, quantity=?
        WHERE id=?
    """, (new_name, new_price, new_quantity, product_id))

    conn.commit()
    conn.close()

    print(f"Product ID {product_id} updated successfully.")