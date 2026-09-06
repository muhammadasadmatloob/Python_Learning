# array
daily_sales=[10000,15000,9000,7000,2000]
highest_sale = 0 

for sale in daily_sales:
    if sale > highest_sale:
        highest_sale = sale
    else:
        pass

print("Highest sale:", highest_sale)


# dictionary

inventory =[
    {"name": "headphones", "price": 10000},
    {"name": "keyboard", "price": 9000},
    {"name": "mouse", "price": 15000},

]
highest_price = 10000
for items in inventory:
    if items["price"] > highest_price:
        print(f"highest price item name is: {items['name']} and its price is {items['price']} ")
    else:
        pass


# class

class employee:

    def __init__(self,name,role):
        self.name=name
        self.role=role

    def clock_in(self):
        print(f"{self.name} clocked in as {self.role}")

class cashier(employee):
    
    def scan_item(self,item_name): 
        print(f"{self.name} just scanned a {item_name}.")



register_worker = cashier("Muhammad Asad Matloob", "Cashier")

register_worker.clock_in()
register_worker.scan_item("Headphones")


# project

database = []
incoming_request={
        "product_name": "iPhone 15",
        "price": -5000
    }

valid_admin_token = "ey12345admin"

def delete_product(product_id, provided_token):
    if provided_token == valid_admin_token:
        print(f"Status 200: Product with ID {product_id} deleted from database")
    else:
        print("Status 403: Error! Invalid admin token.")

delete_product(99, "ey12345admin")


def process_order(order_data):
    if order_data["price"] > 0:
        print(f"Status 200: Order saved to database")
        database.append(order_data)
    else:
        print("Status 400: Error! Price cannot be negative.")

process_order(incoming_request)