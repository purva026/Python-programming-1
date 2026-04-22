# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:28:05 2026

@author: Purva Dange
"""

n = int(input("Enter number:"))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial:", fact)