from wsgiref import headers
from database.db import connect
from utils.receipt import generate_receipt
from  tabulate import tabulate
def sell_product(product_id,quantity):
  conn=connect()
  cursor=conn.cursor()
  cursor.execute("SELECT name,price,quantity FROM products WHERE id=?", (product_id,))
  product=cursor.fetchone()
  if not product:
    print("product not found")
    conn.close()
    return 
  name,price,stock=product
  if quantity>stock : #check stocks
    print(f"Not enough stock for {name}. Available: {stock}")
    conn.close()
    return
  total=price*quantity#calculate total
  new_stock=stock-quantity#update quantity

  cursor.execute("""
  UPDATE products SET quantity=?
                 WHERE id=?
  """,(new_stock,product_id))


  cursor.execute("""
INSERT INTO sales(product_name,quantity,total)
                 VALUES(?,?,?)   
""",(name,quantity,total))  #record the sale in the sales table
  conn.commit()
  conn.close()

  generate_receipt(name, quantity, price, total)

  print(f"Sold {quantity} units of {name}. Total: ${total:.2f}. Remaining stock: {new_stock}")        


def view_sales_history():
  conn = connect()
  cursor =conn.cursor()
  cursor.execute("""
        SELECT id, product_name, quantity, total, sale_time
        FROM sales
        ORDER BY id DESC
    """)
  sales =cursor.fetchall()
  conn.close()

  if not sales:
    print("No sales history found.")
    return
  
  headers = ["SALE ID ", "Product", "Quantity", "Total", "Date "]
  print(tabulate(sales, headers=headers, tablefmt="grid"))


def revenue_dashboard():
    conn = connect()
    cursor = conn.cursor()

    # Total revenue
    cursor.execute("""
        SELECT SUM(total)
        FROM sales
    """)
    total_revenue = cursor.fetchone()[0]

    # Total transactions
    cursor.execute("""
        SELECT COUNT(*)
        FROM sales
    """)
    total_transactions = cursor.fetchone()[0]

    # Total units sold
    cursor.execute("""
        SELECT SUM(quantity)
        FROM sales
    """)
    total_units = cursor.fetchone()[0]

    # Best selling product
    cursor.execute("""
        SELECT product_name,
               SUM(quantity) as units_sold
        FROM sales
        GROUP BY product_name
        ORDER BY units_sold DESC
        LIMIT 1
    """)

    best_product = cursor.fetchone()

    conn.close()

    print("\n========== DASHBOARD ==========\n")

    print(f"Total Revenue: ${total_revenue or 0:.2f}")
    print(f"Total Transactions: {total_transactions}")
    print(f"Total Units Sold: {total_units or 0}")

    if best_product:
        print("\nBest Selling Product:")
        print(f"{best_product[0]} ({best_product[1]} units)")
    else:
        print("\nNo sales yet.")

    print("\n===============================\n")