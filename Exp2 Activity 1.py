# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:32:08 2026

@author: Purva Dange
"""

# Traffic Police Speed Check

speed = float(input("Enter the vehicle speed in km/h: "))

if speed > 60:
    print("You are overspeeding! You have to pay a fine.")
else:
    print("Speed is within the limit. Drive safely!")