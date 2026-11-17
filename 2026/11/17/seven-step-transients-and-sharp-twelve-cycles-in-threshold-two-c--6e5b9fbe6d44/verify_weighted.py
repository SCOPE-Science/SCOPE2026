"""Independent multinomial weighting of the 2187 truncated population signatures.
Run: python verify_weighted.py. Requires verify_capped.py in the same directory.
"""
from math import comb
from functools import lru_cache
from verify_capped import all_classes, trace, identical_at

@lru_cache(None)
def weight(n, cap):
    """Labelled assignments of n vertices with each colour count truncated to cap."""
    total = 0
    for a in range(n + 1):
        if min(a, 2) != cap[0]:
            continue
        for b in range(n - a + 1):
            c = n - a - b
            if min(b, 2) == cap[1] and min(c, 2) == cap[2]:
                total += comb(n, a) * comb(n - a, b)
    return total

def signature_periods():
    cls = []
    for s in all_classes():
        q = trace(s)
        period = next(d for d in (1,2,3,4,6,12)
                      if identical_at(q, 7, 7 + d, s))
        cls.append((s,period))
    return cls

CLASSES = signature_periods()

def count(m,n):
    total={1:0,3:0,12:0}
    for s,p in CLASSES:
        total[p] += weight(m,s[3:6])*weight(n,s[6:9])
    assert sum(total.values()) == 3**(m+n+1)
    return total

def analytic_period3(m,n):
    # A_s counts counts (a,b,c) with all >= 2; B_s counts (1,b,c), b,c >=2.
    A=lambda s:weight(s,(2,2,2))
    B=lambda s:weight(s,(1,2,2))
    U=lambda s:2 if s in (1,2) else 0
    return 3*((A(m)+B(m))*(A(n)+B(n))+U(m)*A(n)+A(m)*U(n))

if __name__=='__main__':
    for m,n in ((1,6),(2,6),(3,4),(4,4),(4,5),(5,5),(6,6),(10,10),(20,20),(40,40)):
        b=count(m,n)
        assert b[3]==analytic_period3(m,n)
        assert (b[12]>0) == (min(m,n)>=4)
        print(f'K_1,{m},{n}: periods_1_3_12=({b[1]},{b[3]},{b[12]})')
    for n in (20,40):
        b=count(n,n)
        actual=b[12]/3**(2*n+1)
        asym=(2*n+6)*(2/3)**n
        print(f'balanced_{n}: prob12={actual:.12g} leading={asym:.12g} ratio={actual/asym:.9g}')
    print('MULTINOMIAL_BASINS_PASS')
