# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:46:58 2026

@author: User
"""

def simple_interest(principal, rate, time):
 si = (principal * rate * time) / 100
 return si

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

interest = simple_interest(p, r, t)
print("Simple Interest is:", interest)