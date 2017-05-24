import math
import Function
from Utilities import Utilities


def main():
    pass


def test():
    #print(Utilities.bernoulli(64).to_str())
    for i in range(0, 1000):
        bernoulli = Utilities.bernoulli(i)
        print(str(i) + ": " + bernoulli.to_str())

test()
