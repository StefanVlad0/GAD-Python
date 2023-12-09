"""
This is the homework for session 4 of the Google Python Workshop "Google Atelierul Digital - Programare", December 2023

Student - Vlad Stefan
"""


# Write a class Fraction(numerator, denominator) that implements the following methods:
# ○ __init__ : instantiate numerator and denominator
# ○ __str__ : display "numerator/denominator"
# ○ __add__ : return a new fraction that represents the addition
# ○ __sub__: return a new fraction that represents the subtraction
# ○ inverse: return a new fraction (the inverse of the fraction)


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("The denominator cannot be 0")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def inverse(self):
        if self.numerator == 0:
            raise ValueError("It is not possible to calculate the inverse for a fraction whose numerator is zero.")
        return Fraction(self.denominator, self.numerator)


frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

print("Fraction 1:", frac1)
print("Fraction 2:", frac2)
print("Sum:", frac1 + frac2)
print("Difference:", frac1 - frac2)
print("Inverse of the first fraction:", frac1.inverse())
