"""Exact-arithmetic supporting checks for farthest-vertex hypercube dynamics.
Not a replacement for the unrestricted analytical proof.
"""
from fractions import Fraction
from itertools import product
from math import ceil, log

def f(x, lam):
    c = 1-lam
    return lam*x-c if x >= 0 else lam*x+c

def first_flip_positive(x, lam):
    """Direct iteration, independent of the proposed logarithmic threshold."""
    assert x > 0
    for k in range(1,400):
        x = f(x, lam)
        if x < 0:
            return k
        if x == 0:
            return None  # tie convention makes a null-set boundary exceptional
    raise AssertionError('no switch')

def test():
    checks = 0
    for lam in [Fraction(1,3), Fraction(1,2), Fraction(3,5), Fraction(3,4), Fraction(9,10)]:
        a = (1-lam)/(1+lam)
        assert f(a,lam)==-a and f(-a,lam)==a; checks+=2
        for d in range(1,5):
            # test every signed periodic vertex of the alleged cycles
            for s in product([-1,1],repeat=d):
                v = tuple(a*x for x in s)
                w = tuple(f(x,lam) for x in v)
                assert w == tuple(-x for x in v); checks += 1
            for coords in product([-1,0,1],repeat=d):
                if d>3: break
                # all coordinates eventually alternate, then approach a sign pattern
                y = [Fraction(x) for x in coords]
                for _ in range(80):
                    y = [f(x,lam) for x in y]
                # once in alternating branch, second step is affine with factor lam^2
                a2 = [f(f(x,lam),lam) for x in y]
                for i in range(d):
                    assert (y[i] > 0) == (a2[i] > 0)
                    assert abs(a2[i]-y[i]) == (1-lam*lam)*abs((a if y[i]>0 else -a)-y[i])
                    checks+=2
        # Compare direct exact rational iteration against the proposed CDF
        # on finite uniform grids. Rational zero-hits are excluded explicitly.
        for q in range(2,41):
            observed = [first_flip_positive(Fraction(j,q), lam)
                        for j in range(1,q)]
            valid = [(Fraction(j,q),t) for j,t in enumerate(observed,1)
                     if t is not None]
            for n in range(1,31):
                measured = sum(1 for x,t in valid if t <= n)
                cutoff = min(Fraction(1),lam**(-n)-1)
                calculated = sum(1 for x,t in valid if x <= cutoff)
                assert measured == calculated
                checks += 1
    print(f'PASS {checks} exact-rational supporting assertions')

if __name__=='__main__': test()
