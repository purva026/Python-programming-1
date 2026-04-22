# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:18:18 2026

@author: Purva Dange
"""

# Program to read a complaint file and display all complaints

# Step 1: Read the file
try:
    file = open("complaints.txt", "r")
    print("--- List of Complaints ---\n")

    # Step 2: Display complaints line by line
    for complaint in file:
        print(complaint.strip())

    file.close()

except FileNotFoundError:
    print("Complaint file not found!")