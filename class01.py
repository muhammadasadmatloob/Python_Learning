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

