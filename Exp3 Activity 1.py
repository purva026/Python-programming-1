# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:40:55 2026

@author: Purva Dange
"""

# Receipt Copy Printer using Nested Loops

copies = int(input("Enter number of receipt copies: "))
items = int(input("Enter number of items: "))

for i in range(1, copies + 1):
    print(f"\nReceipt Copy {i}:")
    for j in range(1, items + 1):
        print(f"Item Number: {j}")