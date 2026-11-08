#!/usr/bin/env python3
"""Direct finite-state verification of primitive three-cycles on complete graphs."""
from collections import Counter
from itertools import product
from math import factorial


def update(state):
    n = len(state)
    firing = sum(v >= n-1 for v in state)
    return tuple(v + firing - n * (v >= n-1) for v in state)


def expected(n):
    low = Counter()
    for a in range(1,n-1):
        for b in range(1,n-a):
            c = n-a-b
            mult = factorial(n)//(factorial(a)*factorial(b)*factorial(c))
            coefficients = {0:mult}
            for num,width in [(a,c),(b,a),(c,b)]:
                for _ in range(num):
                    new = Counter()
                    for k,v in coefficients.items():
                        for j in range(width):
                            new[k+j] += v
                    coefficients = new
            minimum = n*(n-1) - a*b-b*c-c*a
            for k,v in coefficients.items():
                low[minimum+k] += v
    total = Counter(low)
    for energy,count in low.items():
        total[n*(2*n-3)-energy] += count
    return total


def direct(n):
    totals = Counter()
    checked = 0
    # Any primitive-three state is confined to this box; derive independently
    # from periodicity and the fact that each vertex fires and waits.
    for state in product(range(2*n-2), repeat=n):
        checked += 1
        t1 = update(state)
        t2 = update(t1)
        t3 = update(t2)
        if t3 == state and t1 != state:
            totals[sum(state)] += 1
    return totals,checked


def main():
    for n in range(3,7):
        observed,checked=direct(n)
        asserted=expected(n)
        assert observed == asserted, (n,observed,asserted)
        assert sum(observed.values())%3==0
        print(f"n={n}: box={checked} primitive3_states={sum(observed.values())} orbits={sum(observed.values())//3} energies={sorted(observed)} MATCH")
    print('PASS: all finite boxes n=3..6 independently classified')

if __name__=='__main__':
    main()
