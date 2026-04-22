# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:09:49 2026

@author: purva dange
"""

# Attendance sets for two classes
classA = {101, 102, 103, 104}
classB = {103, 104, 105, 106}

print("Class A Attendance:", classA)
print("Class B Attendance:", classB)

# Finding common students
both_present = classA.intersection(classB)

print("\nStudents present in both classes:", both_present)