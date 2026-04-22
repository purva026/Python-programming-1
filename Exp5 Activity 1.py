# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:06:20 2026

@author: purva dange
"""

# Library dictionary with book name and price
library = {
    "Python Basics": 350,
    "Data Science": 500,
    "Machine Learning": 650
}

print("Current Library Books and Prices:")
print(library)

# Updating book price
book = input("Enter the book name to update price: ")

if book in library:
    new_price = float(input("Enter new price: "))
    library[book] = new_price
    print("\nPrice updated successfully!")
else:
    print("\nBook not found in the library.")

print("\nUpdated Library Dictionary:")
print(library)