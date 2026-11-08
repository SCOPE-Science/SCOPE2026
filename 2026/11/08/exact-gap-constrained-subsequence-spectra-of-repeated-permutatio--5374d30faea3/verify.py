#!/usr/bin/env python3
"""Check distinct gap-constrained subsequence counts by two separate constructions.

All intervals bound the difference of successive selected zero-based positions.
No external packages or data are needed.
"""
from itertools import product
from math import comb
from random import Random


def count_by_patterns(q, k, bounds):
    """Enumerate complete query languages with a feasible-position DP."""
    host = list(range(q)) * k
    answer = 0
    for word in product(range(q), repeat=len(bounds) + 1):
        positions = [j for j, c in enumerate(host) if c == word[0]]
        for i, (lo, hi) in enumerate(bounds, 1):
            positions = [j for j, c in enumerate(host)
                         if c == word[i] and any(lo <= j-p <= hi for p in positions)]
            if not positions:
                break
        if positions:
            answer += 1
    return answer


def count_by_polynomial(q, k, bounds):
    """Compute the claimed polynomial by multiplying each interval factor."""
    n = q * k
    coefficient = [0] * n
    for x in range(q):
        coefficient[x] = 1
    for lo, hi in bounds:
        s = min(q, hi - lo + 1)
        new = [0] * n
        for x, value in enumerate(coefficient):
            if value:
                for d in range(lo, lo+s):
                    if x+d < n:
                        new[x+d] += value
        coefficient = new
    return sum(coefficient)


def count_uniform_closed(q, k, h, lo, hi):
    s = min(q, hi-lo+1)
    t = q*k-1-lo*(h-1)
    def choose(n, r):
        return comb(n,r) if n >= r else 0
    return sum((-1)**(j+r)*choose(h-1,r)*choose(t-j*q-r*s+h,h)
               for j in (0,1) for r in range(h))


def run():
    uniform = 0
    for q in range(2, 5):
        for k in range(1, 5):
            for h in range(1, 5):
                for lo in range(1, q+3):
                    for hi in range(lo, lo+q+3):
                        bounds = [(lo,hi)]*(h-1)
                        observed = count_by_patterns(q,k,bounds)
                        polynomial = count_by_polynomial(q,k,bounds)
                        closed = count_uniform_closed(q,k,h,lo,hi)
                        assert observed == polynomial == closed, (q,k,h,lo,hi,observed,polynomial,closed)
                        uniform += 1
    rng = Random(124)
    varied = 0
    for q in range(2, 6):
        for k in range(1, 6):
            for h in range(1, 6):
                for trial in range(40):
                    bounds = []
                    for i in range(h-1):
                        lo = rng.randint(1,q+5)
                        bounds.append((lo,lo+rng.randint(0,q+5)))
                    observed = count_by_patterns(q,k,bounds)
                    predicted = count_by_polynomial(q,k,bounds)
                    assert observed == predicted, (q,k,bounds,observed,predicted)
                    varied += 1
                    s = [min(q,hi-lo+1) for lo,hi in bounds]
                    saturation = q*k >= q + sum(lo+si-1 for (lo,hi),si in zip(bounds,s))
                    local_total = q
                    for si in s:
                        local_total *= si
                    assert (predicted == local_total) == saturation
                    universal = all(si==q for si in s) and saturation
                    assert (predicted == q**h) == universal
    assert count_by_polynomial(3,3,[(2,4),(2,4)]) == 23
    assert count_by_polynomial(3,4,[(2,4),(2,4)]) == 27
    print(f"VERIFY_OK uniform={uniform} nonuniform={varied} example=23/27")


if __name__ == '__main__':
    run()
