# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#create empty data structure
grocery_item = {}
grocery_history = []

#variable to check if while loop condition has been met
stop = False

#loop implemented to allow user to record all grovery items
while not stop:
    
    #accept input of name, number, and price
    name = input("Enter name of item: ")
    number = input("Enter number of items: ")
    price = input("Enter price per item: ")
    
    #create dictionary to store captured grocery items
    grocery_item = {'name': name, 'number': int(number), 'price': float(price)}
    
    #add grocery_item to grocery_history
    grocery_history.append(grocery_item)
    
    #create a way to end loop by asking if user input is complete
    done_shopping = input("Do you have more items to enter?\nEnter Y or N: ")
    
    if done_shopping == 'N':
        stop = True
    else:
        if done_shopping == 'n':
            stop = True
    
#variable to hold the total price of all items 
grand_total = 0

#loop implemented to print grocery items and total prices
for item in grocery_history:
    
    #total cost for each grocery_item
    total_cost = item['number'] * item['price']
    
    #add item total to grand total
    grand_total += total_cost
    
    #print the total number of specified items with cost and total cost
    print("\n%d %s @ $%.2f ea $%.2f" %(item['number'], item['name'], item['price'], total_cost))
    
#print grand total
print("\nGrand total: $%.2f" % grand_total)
    

        
        
        

        
    
        
        