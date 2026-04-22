# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:47:42 2026

@author: Purva Dange
"""

# Program to find average marks and topper marks

# Taking number of students
n = int(input("Enter number of students: "))

# Creating an empty list
marks = []

# Taking marks input from user
for i in range(n):
    m = float(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

# Calculating average
average = sum(marks) / n

# Calculating topper marks
topper = max(marks)

print("\n--- Result ---")
print("Marks List:", marks)
print("Average Marks:", average)
print("Topper Marks:", topper)