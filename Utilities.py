import math
from Fraction import Fraction


class Utilities:
    @staticmethod
    def ncr(n, r):
        if n == r:
            return Fraction.value_of(1)
        if n == 0:
            return Fraction.value_of(0)
        if r == 0:
            return Fraction.value_of(1)
        numerator = math.factorial(n)
        denominator = math.factorial(r) * math.factorial(n - r)
        return Fraction(numerator, denominator)
    
    @staticmethod
    def npr(n, r):
        numerator = math.factorial(n)
        denominator = math.factorial(n - r)
        return Fraction(numerator, denominator)
    
    @staticmethod
    def bernoulli(n):
        if n < 0 or n != int(n):
            raise ValueError
        if n == 0:
            return Fraction.value_of(1)
        if n != 1 and n % 2 != 0:
            return Fraction.value_of(0)
        
        result = Fraction.value_of(0)
        for k in range(0, n):
            result = result.add(Utilities.ncr(n, k).negate().multiply(Utilities.bernoulli(k)).divide(Fraction.value_of(n - k + 1))).simplify()
        return result
