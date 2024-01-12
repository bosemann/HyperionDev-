"""This program defines a list and two dictionaries which are used to
calculate the total value of the menu stock contained in the list and 
dictionaries."""

# The code is defining three variables: `menu`, `stock`, and `price`.
menu = ["hamburger", "sandwich", "coffee", "pan cakes"]
stock = {"hamburger": 300, "sandwich": 200, "coffee": 150, "pan cakes" : 100}
price = {"hamburger": 5.00, "sandwich": 3.00, "coffee": 2.50, \
"pan cakes": 3.00}

# The line `total_stock = 0.0` is initializing a variable named `total_stock`
# assigning it a value of 0.0. This variable will be used to keep track of the
# total value of the stock, which is calculated by multiplying the quantity of
# each item in stock by its price and adding it to the total.
TOTAL_STOCK = 0.0

# The code is calculating the total value of the stock by iterating over each
# item in the `menu` list.For each item, it multiplies the quantity of the item
# in stock (`stock[item]`) by its price (`price[item]`), and adds the result to
# the `total_stock` variable. Finally, it prints the total value of the stock.
for item in menu:
    TOTAL_STOCK += stock[item] * price[item]
print("=====The Total Stock Value is:======")
print(f"£{TOTAL_STOCK}")
