# -*- coding: utf-8 -*-
"""Iterative ver 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16a1UayV1nNMIq2gh_R9Q0XoGSFhAFH53
"""

def quadratic_model(a, b, c, x):
    return a * x**2 + b * x + c
def read_coefficients_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    coefficients = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            coefficients.append(list(map(float, line.split())))
    return coefficients
filename = "/content/Iterative data ver 3.txt"
coefficients = read_coefficients_from_file(filename)
temp_coeffs, rainfall_coeffs, humidity_coeffs = coefficients
days = [1, 100, 200, 365]
temperature = [quadratic_model(*temp_coeffs, day) for day in days]
rainfall = [quadratic_model(*rainfall_coeffs, day) for day in days]
humidity = [quadratic_model(*humidity_coeffs, day) for day in days]
print("\nIterative Model - Version 3 :")
print(f"Days: {days}")
print(f"Temperature: {temperature}")
print(f"Rainfall: {rainfall}")
print(f"Humidity: {humidity}")