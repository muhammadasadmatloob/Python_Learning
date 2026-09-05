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

