#!/usr/bin/env python3
"""Independent finite checks for a row of Łukasiewicz fuzzy accessibility."""
from fractions import Fraction
from itertools import product, combinations

Q = tuple(Fraction(i, 4) for i in range(5))

def diamond(r, x):
    return max((max(Fraction(0), a + b - 1) for a,b in zip(r,x)), default=Fraction(0))

def box(r, x):
    return min((min(Fraction(1), 1-a+b) for a,b in zip(r,x)), default=Fraction(1))

def check():
    checked = 0
    cuts = 0
    for n in range(1,4):
        for r in product(Q, repeat=n):
            for x in product(Q, repeat=n):
                D = diamond(r,x)
                B = box(r,x)
                assert B == 1-diamond(r,tuple(1-t for t in x))
                assert D in [max(Fraction(0),a+b-1) for a,b in zip(r,x)]
                assert B in [min(Fraction(1),1-a+b) for a,b in zip(r,x)]
                checked += 1
            for mask in range(1<<n):
                keep = [j for j in range(n) if mask & (1<<j)]
                omit = [j for j in range(n) if not mask & (1<<j)]
                tail = max((r[j] for j in omit),default=Fraction(0))
                max_d_error = Fraction(0)
                max_b_error = Fraction(0)
                for x in product(Q, repeat=n):
                    d = diamond(r,x)
                    bd = diamond([r[j] for j in keep],[x[j] for j in keep])
                    b = box(r,x)
                    bb = box([r[j] for j in keep],[x[j] for j in keep])
                    max_d_error = max(max_d_error,d-bd)
                    max_b_error = max(max_b_error,bb-b)
                assert max_d_error == tail and max_b_error == tail
                cuts += 1
    # Two-valued grids with 4 worlds, including zeros and fractional relation weights.
    for r in product((Fraction(0),Fraction(1,2),Fraction(1)),repeat=4):
        for x in product(Q,repeat=4):
            assert diamond(r,x) == 1-box(r,[1-t for t in x])
            checked += 1
    # Infinite sequences: finite prefixes have the predicted exact partial values.
    for n in (2,4,8,16,32,128):
        p_inc = [Fraction(j,j+1) for j in range(1,n+1)]
        p_dec = [Fraction(1,j+1) for j in range(1,n+1)]
        r = [Fraction(1)] * n
        assert diamond(r,p_inc) == Fraction(n,n+1)
        assert box(r,p_dec) == Fraction(1,n+1)
    print('VERIFY_OK checked_vectors=%d checked_truncations=%d prefixes=6' % (checked,cuts))
if __name__ == '__main__':
    check()
