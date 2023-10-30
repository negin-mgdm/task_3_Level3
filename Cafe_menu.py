# Create a menu list with available items
menu = ['Latte', 'Espresso', 'Cake', 'Tea', 'Brownie', 'Apple pie']

# Create a dictionary 'stock' with the quantity of each item in stock
# Brownies and apple pies are newly added to menu
stock = {
    'Latte': 14,
    'Espresso': 23,
    'Cake': 10,
    'Tea': 12,
    'Brownie': 14,
    'Apple pie': 11
}

# Create a dictionary 'price' with the price of each item
price = {
    'Latte': 3 ,
    'Espresso': 3.5 ,
    'Cake': 2.75 ,
    'Tea': 2.5,
    'Brownie': 3.4,
    'Apple pie': 3.2
}

# Calculate the value of each item by multiplying its price with its stock quantity
latte = price['Latte'] * stock['Latte']
espresso = price['Espresso'] * stock['Espresso']
cake = price['Cake'] * stock['Cake']
tea = price['Tea'] * stock['Tea']
brownie = price['Brownie'] * stock['Brownie']
apple_pie = price['Apple pie'] * stock['Apple pie']

# Iterate through each item in the 'menu' and calculate the value of each item by multiplying stock by price
total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value 

# Print the total stock price   
print (f"Total stock price:\n ${total_stock}") 
# Print the price of each item in stock
print (f"Price of each item in stock:\n Latte: ${latte}\n Esperesso: ${espresso}\n Cake: ${cake}\n Tea: ${tea}\n Brownie: ${brownie}\n Apple Pie: ${apple_pie}")

    
  
    
