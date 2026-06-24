from tabulate import tabulate
from database.db import connect
cart=[]
def add_to_cart(product_id,name,price,quantity):
    global cart
    item = {
        "product_id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(item)

    print(f"{name} added to cart.")
def view_cart():
    if not cart:
        print("Cart is empty.")
        return

    table = []
    total = 0

    for item in cart:
        subtotal = item["price"] * item["quantity"]

        total += subtotal

        table.append([
            item["product_id"],
            item["name"],
            item["price"],
            item["quantity"],
            subtotal
        ])

    headers = [
        "ID",
        "Product",
        "Price",
        "Qty",
        "Subtotal"
    ]

    print(tabulate(table, headers=headers, tablefmt="grid"))

    print(f"\nCart Total: ${total:.2f}")
def add_product_to_cart(product_id, quantity):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, price, quantity
        FROM products
        WHERE id = ?
    """, (product_id,))

    product = cursor.fetchone()

    conn.close()

    if not product:
        print("Product not found.")
        return

    pid, name, price, stock = product

    if quantity > stock:
        print("Not enough stock.")
        return

    add_to_cart(
        pid,
        name,
        price,
        quantity
    )