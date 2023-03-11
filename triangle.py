# -*- coding: utf-8 -*-
"""
This module contains a function to classify triangles based on the lengths of their sides.
"""
def classify_triangle(side_a, side_b, side_c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    Return:
        - 'Equilateral' if all three sides are equal
        - 'Isosceles' if exactly one pair of sides are equal
        - 'Scalene' if no pair of sides are equal
        - 'NotATriangle' if not a valid triangle
        - 'Right' if the sum of any two sides equals the square of the third side
    """
    if not (isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        return 'InvalidInput'
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return 'InvalidInput'
    if side_a > 200 or side_b > 200 or side_c > 200:
        return 'InvalidInput'
    if side_a >= side_b + side_c or side_b >= side_a + side_c or side_c >= side_a + side_b:
        return 'NotATriangle'
    if side_a == side_b == side_c:
        return 'Equilateral'
    if side_a == side_b or side_b == side_c or side_a == side_c:
        return 'Isosceles'
    if side_a ** 2 + side_b ** 2 == side_c ** 2 or \
   side_b ** 2 + side_c ** 2 == side_a ** 2 or \
   side_a ** 2 + side_c ** 2 == side_b ** 2:
        return 'Right'
    return 'Scalene'
