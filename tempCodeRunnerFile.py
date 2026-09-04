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