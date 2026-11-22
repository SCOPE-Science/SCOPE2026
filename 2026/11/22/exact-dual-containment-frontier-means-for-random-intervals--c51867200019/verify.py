"""Exact finite checks for containment-frontier expectations in uniform interval matchings."""
from fractions import Fraction
from math import comb, factorial
from functools import lru_cache


def formula(n):
    assert n >= 1
    # Expectations of intervals that contain no other interval and intervals
    # not contained in any other, respectively.
    inner = Fraction(n * 4**n * factorial(n) * factorial(n-1),factorial(2*n))-1
    outer = sum((sum((Fraction(comb(j,k),2**j*(2*k+1)) for k in range(j+1)),Fraction(0)) for j in range(n)),Fraction(0))
    return inner,outer


def matchings(values):
    if not values:
        yield ()
        return
    first = values[0]
    for k in range(1,len(values)):
        for remaining in matchings(values[1:k]+values[k+1:]):
            yield ((first, values[k]),) + remaining


def counts(pairs):
    inner = sum(not any(a < x and y < b for x,y in pairs if (a,b)!=(x,y)) for a,b in pairs)
    outer = sum(not any(x < a and b < y for x,y in pairs if (a,b)!=(x,y)) for a,b in pairs)
    return inner,outer


def verify():
    assertions = 0
    for n in range(1,8):
        inner,outer=0,0
        total=0
        for pairs in matchings(tuple(range(2*n))):
            x,y=counts(pairs)
            inner+=x; outer+=y; total+=1
        expected=(Fraction(inner,total),Fraction(outer,total))
        assert total == factorial(2*n)//(2**n*factorial(n))
        assert expected == formula(n),(n,expected,formula(n))
        assertions+=2
    for n in range(1,21):
        i,o=formula(n)
        assert (i>=o if n>=3 else i==o)
        assertions+=1
    print(f"PASS: {assertions} exact assertions, including enumeration of every matching through 7 arcs")

if __name__=='__main__': verify()
