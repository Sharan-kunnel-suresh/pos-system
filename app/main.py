from database.db import create_tables
from services.inventory_service import add_product, restock_product, view_products, search_product
from services.sales_service import sell_product
     
def menu():
  print("\n===POS SYSTEM MENU===")
  print("1. Add product")
  print("2.View Peoducts")
  print("3. Restock Product")
  print("4. Sell Product")
  print("5. Search Product")
  print("6. Exit")

def main():
  create_tables()
  while True:
    menu()
    choice = input("Enter your choice: ")
    if (choice=="1"):
      name=input("Enter product name:")
      price=float((input("Enter the price of the product:")))
      quantity=int(input("enter the quantity of the product:"))
      add_product(name,price,quantity)
    elif(choice=="2"):
      print("\nProducts in the inventory:")
      view_products()
    elif(choice=="3"):
      product_id=int(input("Enter the ID of the product to restock:"))
      quantity=int(input("Enter the quantity to add:"))
      restock_product(product_id,quantity)
    elif(choice=="4"):
      product_id=int(input("Enter the ID of the product to sell:"))
      quantity=int(input("Enter the quantity to sell:"))
      sell_product(product_id,quantity)
    elif(choice=="5"):
      keyword=input("Enter the name of the product")
      search_product(keyword)
    elif(choice=="6"):  
      print("Exiting>>>")
      
      break
    else:
      print("Invalid choice. Please try again.")  

if __name__=="__main__":  main()