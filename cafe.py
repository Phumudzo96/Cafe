menu = ["coffee", "cappuccino", "latte", "tea"]              # create a list with set values

stock = {"coffee" : 20,                                      # create a dictionary with stock of the list values
        "cappuccino" : 20,
        "latte" : 20,
        "tea" : 20}

price = {"coffee" : 15.00,                                   # create a dictionary with prices of the list values
        "cappuccino" : 20.00,
        "latte" : 25.00,
        "tea" : 10.00}

menu[0] = (stock["coffee"] * price["coffee"])               # calculate the first list value stock and price
print(menu[0])
menu[1] = (stock["cappuccino"] * price["cappuccino"])       # calculate the second list value stock and price
print(menu[1])
menu[2] = (stock["latte"] * price["latte"])                 # calculate the third list value stock and price
print(menu[2])
menu[3] = (stock["tea"] * price["tea"])                     # calculate the fourth list value stock and price

print(menu[3])
final_total = (menu[0] + menu[1] + menu[2] + menu[3])       # add up all the lists values

print(f"Everything will be a total of R{final_total}")      # print out the total amount of everything
