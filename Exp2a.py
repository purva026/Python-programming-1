# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:35:04 2026

@author: Purva Dange
"""

year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")