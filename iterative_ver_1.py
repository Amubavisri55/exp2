# -*- coding: utf-8 -*-
"""Iterative ver 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uCGVsw50qn129hqoYGMB0HIvA6QuBo3L
"""

def quadratic_model(a, b, c, x):
    return a * x**2 + b * x + c
print("Enter coefficients for Temperature (a, b, c):")
temp_coeffs = [float(input(f"Enter coefficient {coef}: ")) for coef in ['a', 'b', 'c']]
print("Enter coefficients for Rainfall (a, b, c):")
rainfall_coeffs = [float(input(f"Enter coefficient {coef}: ")) for coef in ['a', 'b', 'c']]
print("Enter coefficients for Humidity (a, b, c):")
humidity_coeffs = [float(input(f"Enter coefficient {coef}: ")) for coef in ['a', 'b', 'c']]
days = [1, 100, 200, 365]
temperature = [quadratic_model(*temp_coeffs, day) for day in days]
rainfall = [quadratic_model(*rainfall_coeffs, day) for day in days]
humidity = [quadratic_model(*humidity_coeffs, day) for day in days]
print("\nIterative Model - Version 2 (Keyboard Input):")
print(f"Days: {days}")5
print(f"Temperature: {temperature}")
print(f"Rainfall: {rainfall}")
print(f"Humidity: {humidity}")