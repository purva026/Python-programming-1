# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:46:33 2026

@author: Purva Dange 
"""

# Multiplication tables from 1 to 10

for i in range(1, 11):          # Table number
    print(f"\nMultiplication Table of {i}")
    print("-" * 25)
    
    for j in range(1, 11):      # Multiply from 1 to 10
        print(f"{i} x {j} = {i * j}")