import math
import time
from Function import Function
from Utilities import Utilities


def main():
    pass


def test():
    start = time.time()
    for i in range(0, 1001):
        bernoulli = Utilities.bernoulli(i)
        print(str(i) + ": " + bernoulli.to_str())
    end = time.time()
    elapsed = end - start
    print(str(elapsed) + " seconds")
    #print(Utilities.bernoulli(64).to_str())
    """
    f = Function("ln(1+x)*sin(10x)")
    f = Function("44*(x-1)*(5*x-27)*(5*x-16)*(8*x-49)*(8*x-35)*(40*x-81)/4671275427")
    print(f.differentiate(6.4))
    print(f.integrate(0, 6.4))
    """

test()
