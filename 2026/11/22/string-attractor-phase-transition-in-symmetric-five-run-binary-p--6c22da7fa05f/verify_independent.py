#!/usr/bin/env python3
"""Direct occurrence scans and coefficient identities for symmetric five-run words."""
from itertools import product
from random import Random


def is_attractor(w, positions):
    # Distinct implementation: enumerate a factor, and scan all its occurrences.
    n = len(w)
    for m in range(1, n + 1):
        for s in range(n - m + 1):
            f = w[s:s+m]
            if not any(w[t:t+m] == f and any(t <= p < t+m for p in positions)
                       for t in range(n - m + 1)):
                return False
    return True


def points(a, b, c):
    return ((a + b - 1, a + b + c - 1) if c >= a else
            ((a - 1, a + b + c) if b == 1 else
             (a - 1, a + b, a + 2*b+c-1)))


def exact_unique_occurrences(w, factor):
    return [t for t in range(len(w)-len(factor)+1) if w[t:t+len(factor)] == factor]


def count_from_series(n):
    # Coefficient of 2 z^9 / ((1-z^2)^2(1-z^3)).
    if n < 9: return 0
    return 2 * sum(t+1 for r in range((n-9)//3+1)
                       for t in range((n-9-3*r)//2+1)
                       if 2*t+3*r == n-9)


def run():
    rng=Random(20261117)
    cases=[(a,b,c) for a,b,c in product(range(1,6),repeat=3)]
    cases += [(rng.randrange(1,31),rng.randrange(1,31),rng.randrange(1,31)) for _ in range(180)]
    for a,b,c in cases:
        w='0'*a+'1'*b+'0'*c+'1'*b+'0'*a
        assert is_attractor(w, points(a,b,c)), (a,b,c,'factor')
        if a>=2 and b>=2 and c<a:
            factors=['0'*a+'1','1'*(b-1)+'0'*c+'1','1'+'0'*a]
            starts=[0,a+1,a+2*b+c-1]
            for f,start in zip(factors,starts):
                assert exact_unique_occurrences(w,f) == [start], (a,b,c,f)
            spans=[(s,s+len(f)-1) for s,f in zip(starts,factors)]
            assert spans[0][1] < spans[1][0] and spans[1][1] < spans[2][0]
    for n in range(5,111):
        direct=2*sum(1 for a in range(1,n) for b in range(1,n)
                     if (c:=n-2*a-2*b)>=1 and a>=2 and b>=2 and c<a)
        assert direct==count_from_series(n), (n,direct,count_from_series(n))
    print(f'INDEPENDENT_OK witness_cases={len(cases)} unique_occurrence_cases=verified generating_coefficients=5..110')

if __name__=='__main__':
    run()
