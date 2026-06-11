from datetime import datetime
import os

def generate_receipt(product_name,quantity,unit_price,total):
  os.makedirs("receipts",exist_ok=True)#create receiptsd folder if it doesn't exist
  timestamp=datetime.now().strftime("%Y%m%d%H%M%S")#generate  
  filename=f"receipts/receipt_{timestamp}.txt"
  receipt_content = f"""
=================================
            RECEIPT
=================================

Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Product: {product_name}
Quantity: {quantity}
Unit Price: ${unit_price:.2f}

---------------------------------
TOTAL: ${total:.2f}
---------------------------------

Thank you for your purchase!

=================================
"""
  with open(filename, "w") as f:
    f.write(receipt_content)
    print(f"receipt generated: {filename}")