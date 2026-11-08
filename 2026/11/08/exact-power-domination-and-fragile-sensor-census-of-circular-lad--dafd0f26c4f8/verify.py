#!/usr/bin/env python3
"""Independent finite checks for the prism power-domination census.

Uses only the Python standard library. This program checks finite cases;
it does not replace the unrestricted mathematical proof.
"""
from collections import Counter
from itertools import combinations
from math import comb


def graph(n):
    adjacency = [set() for _ in range(2*n)]
    for rail in range(2):
        for column in range(n):
            v = rail*n+column
            adjacency[v] = {
                rail*n+(column-1)%n,
                rail*n+(column+1)%n,
                (1-rail)*n+column,
            }
    return adjacency


def closure(adjacency, mask):
    marked = mask
    for v in range(len(adjacency)):
        if (mask >> v) & 1:
            for w in adjacency[v]:
                marked |= 1 << w
    while True:
        additions = 0
        for v in range(len(adjacency)):
            if (marked >> v) & 1:
                unseen = [w for w in adjacency[v] if not (marked >> w) & 1]
                if len(unseen) == 1:
                    additions |= 1 << unseen[0]
        if (additions & ~marked) == 0:
            return marked
        marked |= additions


def graph_distance(v, w, n):
    c, d = v%n, w%n
    return min((c-d)%n, (d-c)%n) + ((v//n)!=(w//n))


def exact_coefficient(n, k):
    if k == 0: return 1
    if k > n//3: return 0
    total = 0
    for j in range(k//2+1):
        upper = n-3*k+2*j-1
        if upper >= k-1:
            total += comb(k, 2*j)*comb(upper, k-1)
    numerator = 2*n*total
    assert numerator % k == 0
    return numerator//k


def rational_expansion(limit):
    # 1/(1-x-z*x**3-z*x**4), represented as polynomial dictionaries.
    inverse = [{0: 1}]
    for n in range(1, limit+1):
        d = Counter()
        for delta, power in [(1, 0), (3, 1), (4, 1)]:
            if n >= delta:
                for k, c in inverse[n-delta].items():
                    d[k+power] += c
        inverse.append(dict(d))
    outputs = []
    for n in range(limit+1):
        d = Counter()
        for delta, multiplier, power in [(1, 1, 0), (3, 3, 1), (4, 4, 1)]:
            if n >= delta:
                for k, c in inverse[n-delta].items():
                    d[k+power] += multiplier*c
        if n >= 1:
            d[0] -= 1
        if n >= 3 and n % 3 == 0:
            d[n//3] -= 3*(-1)**(n//3-1)
        outputs.append({k:c for k,c in d.items() if c})
    return outputs


def lucas(n):
    a,b=2,1
    for _ in range(n):
        a,b=b,a+b
    return a


def run():
    examined = 0
    failed_count = 0
    for n in range(4,10):
        adj = graph(n)
        counts = Counter()
        for mask in range(1 << (2*n)):
            chosen = [v for v in range(2*n) if (mask >> v) & 1]
            independent = all(graph_distance(v,w,n) >= 4 for v,w in combinations(chosen,2))
            observed = closure(adj,mask).bit_count()
            assert (observed < 2*n) == independent
            if independent:
                assert observed == 4*len(chosen)
                counts[len(chosen)] += 1
                failed_count += 1
            examined += 1
        assert dict(counts) == {k: exact_coefficient(n,k) for k in range(n//3+1) if exact_coefficient(n,k)}
    transfer = rational_expansion(160)
    for n in range(4, 161):
        assert transfer[n] == {k:exact_coefficient(n,k)
                               for k in range(1, n//3+1)
                               if exact_coefficient(n,k)}
        lhs = 1 + sum(exact_coefficient(n,k) for k in range(1,n//3+1))
        rhs = lucas(n)
        if n % 2 == 0: rhs += 2*(-1)**(n//2)
        if n % 3 == 0: rhs += 3*(-1)**(n//3)
        assert lhs == rhs, (n, lhs, rhs)
    for n in range(7,31):
        for v in range(2*n):
            assert sum(graph_distance(v,w,n) <= 3 for w in range(2*n) if w != v) == 11
    assert closure(graph(3),0) == 0
    assert all(closure(graph(3),1<<v).bit_count()==6 for v in range(6))
    print('VERIFY_OK direct_prism_n=4..9 examined_subsets=%d failed_sets=%d'
          ' rational_coefficients_n=4..160 lucas_counts_n=4..160'
          ' pair_graph_11_regular_n=7..30 triangular_prism=PASS'
          % (examined, failed_count))

if __name__ == '__main__':
    run()
