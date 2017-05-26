import math
from decimal import Decimal


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator < 0:
            numerator *= -1
            denominator *= -1
        self.numerator = int(numerator)
        self.denominator = int(denominator)
    
    @staticmethod
    def value_of(n):
        return Fraction(n, 1)

    def to_str(self):
        if self.is_undefined():
            return "Undefined"
        elif self.numerator == 0:
            return "0"
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)

    @staticmethod
    def equals(f1, f2):
        if (f1.simplify().numerator == f2.simplify().numerator
                and f2.simplify().denominator == f1.simplify().denominator):
            return True
        return False

    def to_float(self):
        return self.numerator / self.denominator

    def to_decimal(self):
        return Decimal(self.numerator) / Decimal(self.denominator)

    def simplify(self):
        numerator = self.numerator
        denominator = self.denominator
        gcd = math.gcd(numerator, denominator)

        # Floor division to avoid converting from int to float
        if gcd != 0:
            numerator //= gcd
            denominator //= gcd

        if denominator < 0:
            numerator *= -1
            denominator *= -1

        return Fraction(numerator, denominator)

    def is_undefined(self):
        if self.denominator == 0:
            return True
        return False

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def negate(self):
        return Fraction(-self.numerator, self.denominator)

    def abs(self):
        return Fraction(abs(self.numerator), abs(self.denominator))

    def add(self, f):
        return Fraction(self.numerator * f.denominator +
                        f.numerator * self.denominator,
                        self.denominator * f.denominator).simplify()
    
    def subtract(self, f):
        return Fraction(self.numerator * f.denominator -
                        f.numerator * self.denominator,
                        self.denominator * f.denominator).simplify()
    
    def multiply(self, f):
        return Fraction(self.numerator * f.numerator,
                        self.denominator * f.denominator).simplify()
    
    def divide(self, f):
        return Fraction(self.numerator * f.denominator,
                        self.denominator * f.numerator).simplify()

    def pow(self, n):
        if n == 0:
            if self.numerator != 0 and self.denominator != 0:
                return Fraction(1, 1)
            else:
                return Fraction(0, 0)
        elif n < 0:
            return Fraction(self.denominator ** int(n * -1),
                            self.numerator ** int(n * -1)).simplify()
        else:
            return Fraction(self.numerator ** int(n),
                            self.denominator ** int(n)).simplify()
