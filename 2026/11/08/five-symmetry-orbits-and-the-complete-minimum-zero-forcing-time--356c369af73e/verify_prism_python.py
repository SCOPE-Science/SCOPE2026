#!/usr/bin/env python3
"""Independent exhaustive four-set census for cyclic-prism zero forcing."""
from itertools import combinations
from collections import Counter

def neighbors(n):
    return [((s*n+(i-1)%n), (s*n+(i+1)%n), ((1-s)*n+i))
            for s in range(2) for i in range(n)]

def time_to_force(n, B):
    N = 2*n
    nbr = neighbors(n)
    colored = set(B)
    t = 0
    while len(colored) != N:
        take = set()
        for v in tuple(colored):
            w = [x for x in nbr[v] if x not in colored]
            if len(w) == 1:
                take.add(w[0])
        if not take:
            return None
        colored |= take
        t += 1
    return t

def predicted(n):
    m = n//2
    if n % 2 == 0:
        return {m-1:n, m:8*n, m+1:4*n}
    return {m:3*n, m+1:6*n, m+2:4*n}

def orbit(n, B):
    return {tuple(sorted(((v//n)^f)*n+(sgn*(v%n)+k)%n for v in B))
            for f in (0,1) for sgn in (-1,1) for k in range(n)}

def reps(n):
    return [ (0,1,n,n+1), (0,1,2,3), (0,1,2,n),
             (0,1,n,2*n-1), (0,1,3,n+1) ]

for n in range(5,19):
    successful = {}
    for B in combinations(range(2*n),4):
        t = time_to_force(n,B)
        if t is not None: successful[B]=t
    histogram = Counter(successful.values())
    assert histogram == Counter(predicted(n)), (n, histogram)
    covered=set()
    for B,sz in zip(reps(n),(n,2*n,4*n,2*n,4*n)):
        orb = orbit(n,B)
        assert len(orb)==sz,(n,B,len(orb),sz)
        assert not covered.intersection(orb),(n,B)
        covered |= orb
        assert set(orb).issubset(successful)
    assert covered==successful.keys(), (n,len(covered),len(successful))
    print('order',n,'minimum_sets',len(successful),'time_counts',dict(sorted(histogram.items())))
assert Counter(time_to_force(4,B) for B in combinations(range(8),4)) [1] == 6
print('PYTHON_EXHAUSTIVE_PASS')
