# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:50:41 2026

@author: Purva Dange
"""

# Program to calculate total bill from a list of product prices

# Number of products
n = int(input("Enter number of products: "))

prices = []

# Taking price input
for i in range(n):
    p = float(input(f"Enter price of product {i+1}: "))
    prices.append(p)

# Calculating total bill
total_bill = sum(prices)

print("\n--- BILL DETAILS ---")
print("Product Prices:", prices)
print("Total Bill =", total_bill)