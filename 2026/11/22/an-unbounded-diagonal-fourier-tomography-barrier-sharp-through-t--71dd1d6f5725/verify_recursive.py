#!/usr/bin/env python3
"""Exact mod-two certificate for low-degree diagonal tomography on convex polygons."""
from functools import lru_cache, reduce
from itertools import combinations
from math import comb

@lru_cache(None)
def triangulations(a, b):
    if b - a <= 2:
        return (frozenset(),)
    answer = []
    for k in range(a + 1, b):
        for left in triangulations(a, k):
            for right in triangulations(k, b):
                val = left | right
                if k > a + 1:
                    val = val | {(a, k)}
                if b > k + 1:
                    val = val | {(k, b)}
                answer.append(frozenset(val))
    return tuple(answer)

def catalan(k):
    return comb(2*k, k) // (k + 1)

def column_rank_mod2(n, max_degree):
    states = triangulations(0, n - 1)
    m = len(states)
    assert len(set(states)) == m == catalan(n - 2)
    edges = [e for e in combinations(range(n), 2)
             if e[1] - e[0] > 1 and e != (0, n-1)]
    columns = [sum(1 << j for j, T in enumerate(states) if e in T)
               for e in edges]
    pivots = {}
    def add(v):
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                return True
        return False
    ranks = []
    for degree in range(max_degree+1):
        if degree == 0:
            candidates = [(1 << m) - 1]
        else:
            candidates = (reduce(int.__and__, (columns[i] for i in indices))
                          for indices in combinations(range(len(edges)), degree))
        for vector in candidates:
            add(vector)
        ranks.append(len(pivots))
    return m, ranks

def main():
    expected = {
        4: (2, [1,2]),
        5: (5, [1,5]),
        6: (14, [1,9,14]),
        7: (42, [1,14,42]),
        8: (132, [1,20,100,132]),
        9: (429, [1,27,198,429]),
        10: (1430, [1,35,350,1195,1430]),
    }
    for n, (count, ranks) in expected.items():
        m, actual = column_rank_mod2(n, (n - 2)//2)
        assert (m,actual) == (count,ranks), (n, m, actual)
        print('n=%d states=%d mod2_ranks=%s' % (n,m,actual))
    print('PASS recursive exact exhaustive modular rank certificate')

if __name__ == '__main__':
    main()
