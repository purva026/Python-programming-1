# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:52:09 2026

@author: Purva Dange
"""

# Program to reverse a customer feedback message

feedback = input("Enter customer feedback: ")

# Reverse the string
reversed_feedback = feedback[::-1]

print("\n--- Result ---")
print("Original Feedback:", feedback)
print("Reversed Feedback:", reversed_feedback)