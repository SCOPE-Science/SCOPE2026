#!/usr/bin/env python3
"""Independent exhaustive checks of fixed-point laws for complete mappings of rectangular bands."""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial


def brute(a, b):
    """Iterate all bijections of the grid, testing BOTH complete-mapping requirements."""
    grid = tuple(product(range(a), range(b)))
    hist = Counter()
    n = 0
    for target in permutations(grid):
        alpha = dict(zip(grid, target))
        if len(set(alpha.values())) != a*b:
            raise AssertionError('not a permutation')
        orth = {(i,j): (i,alpha[(i,j)][1]) for i,j in grid}
        if len(set(orth.values())) == a*b:
            n += 1
            hist[sum(alpha[x] == x for x in grid)] += 1
    return n, hist


def formula(a, b):
    """Exact probability coefficients via inclusion-exclusion over bipartite edge sets."""
    cells = tuple(product(range(a), range(b)))
    denom = factorial(a)**b * factorial(b)**a
    # P(F=r) = sum_T C(|T|,r) (-1)^(|T|-r) P(T subset fixed).
    moments = [Fraction(0)]*(a*b+1)
    for bits in range(1 << (a*b)):
        r = bits.bit_count()
        dr = [0]*a
        dc = [0]*b
        for z,(i,j) in enumerate(cells):
            if bits & (1 << z):
                dr[i] += 1
                dc[j] += 1
        prob = Fraction(1)
        for d in dr:
            prob /= factorial(b)//factorial(b-d)
        for d in dc:
            prob /= factorial(a)//factorial(a-d)
        for k in range(r+1):
            moments[k] += (-1)**(r-k)*comb(r,k)*prob
    assert sum(moments) == 1 and all(v>=0 for v in moments)
    assert all((v*denom).denominator == 1 for v in moments)
    return denom, Counter({k:int(v*denom) for k,v in enumerate(moments) if v})


def verify():
    for a,b in [(1,1),(1,3),(2,2),(2,3)]:
        exact, counts = brute(a,b)
        expected, formula_counts = formula(a,b)
        assert exact == expected, (a,b,exact,expected)
        assert counts == formula_counts, (a,b,counts,formula_counts)
        avg = Fraction(sum(k*v for k,v in counts.items()),exact)
        var = Fraction(sum((k-1)**2*v for k,v in counts.items()),exact)
        assert avg == 1
        if a>=2 and b>=2:
            assert var == 1+Fraction(1,a*b), (a,b,var)
        elif a*b>1:
            assert var==1
        else:
            assert var==0
        print('EXHAUSTIVE_OK',a,b,'count',exact,'fixed_point_histogram',sorted(counts.items()),'mean',avg,'variance',var)
    a,b=3,3
    n,hist = formula(a,b)
    assert n==46656
    assert hist[0]==17972 and hist[1]==16515
    print('SUBSET_IDENTITY_OK',a,b,'count',n,'zero_fixed',hist[0],'one_fixed',hist[1])
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
