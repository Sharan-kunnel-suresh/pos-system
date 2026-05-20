from app.database.db import create_tables
from app.services.inventory_service import add_product, view_products

def menu():
  print("\n===POS SYSTEM MENU===")
  print("1. Add product")
  print("2.View Peoducts")
  print("3. exit")

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
      print("Exiting>>>")
      break
    else:
      print("Invalid choice. Please try again.")  

if __name__=="__main__":  main()