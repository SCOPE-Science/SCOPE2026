"""Self-contained finite checks for the Euclidean minimum width of star graph associahedra.

This checker is corroborative.  The all-dimensional proof is in RESULT.md.
Python >=3.9; no third-party packages.
"""
from fractions import Fraction
from math import comb, sqrt
from random import Random


def cut_width_squared(m, b):
    assert m >= 2 and 1 <= b <= m
    n = m + 1
    mixed = 2**m - 2**(m-b)
    return Fraction(mixed * mixed * n, b * (n-b))


def support_width(m, vector):
    # All nonsingleton connected tubes of the star are center plus nonempty leaf sets.
    assert len(vector) == m + 1
    total = 0
    for mask in range(1, 1 << m):
        entries = [vector[0]] + [vector[i + 1] for i in range(m) if mask & (1 << i)]
        total += max(entries) - min(entries)
    return total


def certify_direct():
    rng = Random(405772)
    tests = 0
    for m in range(2, 9):
        n = m + 1
        vals = [cut_width_squared(m, b) for b in range(1, m+1)]
        for b in range(1, m+1):
            vec = [Fraction(-b,n)]*(m+1)
            for i in range(1,b+1): vec[i] += 1
            numer = support_width(m, vec)
            norm2 = sum(z*z for z in vec)
            assert numer*numer/norm2 == vals[b-1]
            tests += 1
        lowest = min(vals)
        for _ in range(160):
            v = [rng.randrange(-11,12) for i in range(n)]
            if len(set(v))==1: continue
            mu = Fraction(sum(v),n)
            vec = [Fraction(x)-mu for x in v]
            ww = support_width(m,vec)
            norm2 = sum(z*z for z in vec)
            assert ww*ww/norm2 >= lowest
            tests+=1
    return tests


def certify_discrete():
    tests=0
    for n in range(3,351):
        m=n-1
        vals=[cut_width_squared(m,b) for b in range(1,m+1)]
        minimum=min(vals)
        b_min = [b+1 for b,w in enumerate(vals) if w==minimum]
        expected=1 if n<=14 else n//2
        assert b_min==[expected], (n,b_min,expected)
        tests+=m
        # Exact monotone decrease among centered cuts from b=2 to floor(n/2).
        if n>=14:
            for b in range(2,n//2):
                assert vals[b] < vals[b-1]
                tests+=1
    # Threshold comparison at exact integers:
    n14=14; n15=15
    assert cut_width_squared(13,7) > cut_width_squared(13,1)
    assert cut_width_squared(14,7) < cut_width_squared(14,1)
    return tests

if __name__=='__main__':
    a=certify_direct(); b=certify_discrete()
    print(f'STELLOHEDRON_WIDTH_CHECKS_PASSED direct={a} exact_cut_comparisons={b}')
