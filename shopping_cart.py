# shopping_cart.py
import datetime

now = datetime.datetime.now()

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

#print(products)

#GUIDED CHECKPOINT PART 1

possible_choices = []
for ids in products:
    possible_choices.append(str(ids["id"]))

choices = []

#print(type(possible_choices))

filling_cart = input("Please input a product identifier: ")
while filling_cart != "DONE":
    if filling_cart in possible_choices:
        choices.append(int(filling_cart))
    else:
        print("Please enter a valid product identifier")
    filling_cart = input("Please input a product identifier: ")
    
print("------------------------------")
print("DAVE'S FOODS AND STUFF")
print("WWW.HUNGRY-DAVE.COM")
print("------------------------------")
print("CHECKOUT AT: ", now.strftime("%Y-%m-%d %H:%M %p"))
print("------------------------------")
# GUIDED CHECKPOINT STEP 2

#choices = [1, 8, 6, 16, 6] # temporary list of valid ids for testing purposes

#print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:", choices)
print("SELECTED PRODUCTS:")

total_price = 0


for choice in choices:  #do not mess with this section of the code
    matching_choices = [c for c in products if str(c["id"]) == str(choice)]   
    for i in matching_choices:
        print("...", i['name'], "(" + to_usd(i["price"]) + ")")
        total_price = total_price + i["price"]
print("------------------------------")
print("SUBTOTAL:", to_usd(total_price))
tax = total_price*.08875
print("TAX:", to_usd(tax))
print("TOTAL:", to_usd(tax+total_price))
print("------------------------------")
print("THANKS, SEE YOU AGAIN SOON")
print("------------------------------")