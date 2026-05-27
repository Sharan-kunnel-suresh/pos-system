from database.db import connect

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

  print(f"Sold{quantity} x {name}")
  print(f"Total;${total:.2f}")
