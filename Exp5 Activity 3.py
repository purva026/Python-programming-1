# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:11:15 2026

@author: purva dange
"""

# Shop inventory dictionary
inventory = {
    "Sugar": 50,
    "Rice": 100,
    "Oil": 30
}

print("Current Inventory:")
print(inventory)

# Add new stock
item = input("Enter item name to add/update: ")
qty = int(input("Enter quantity to add: "))

if item in inventory:
    inventory[item] += qty     # update existing stock
else:
    inventory[item] = qty      # add new item

print("\nStock updated successfully!")
print("Updated Inventory:")
print(inventory)