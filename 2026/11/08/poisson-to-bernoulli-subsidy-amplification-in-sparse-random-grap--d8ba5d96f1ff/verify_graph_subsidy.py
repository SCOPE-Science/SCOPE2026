"""Finite consistency checks for the graph-orientation subsidy theorem.

Run: python checker_random_subsidy.py
Only standard Python is required. Finite verification is not a proof of limits.
"""
import itertools
import math
from collections import Counter


def component_counts(n, edges):
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    seen = set()
    trees = isolates = 0
    for u in range(n):
        if u in seen:
            continue
        q = [u]
        seen.add(u)
        for x in q:
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)
        c_edges = sum(len(adj[x]) for x in q) // 2
        if len(q) == 1:
            isolates += 1
        elif c_edges == len(q) - 1:
            trees += 1
    return trees, isolates


def predicted_min(n, edges):
    t, i = component_counts(n, edges)
    return t + i if t else 0


def brute_min(n, edges):
    # Each orientation is examined with all 0-1 payment vectors; the theorem
    # provides an integer-payment optimum, so this finite test is appropriate.
    nedge = len(edges)
    for total in range(n+1):
        for subsidized in itertools.combinations(range(n), total):
            paid = [int(i in subsidized) for i in range(n)]
            for orientation in range(1 << nedge):
                assigned = [0] * n
                for ix, (a, b) in enumerate(edges):
                    assigned[b if (orientation >> ix) & 1 else a] += 1
                good = True
                for i in range(n):
                    for j in range(n):
                        if i == j:
                            continue
                        value_i_of_j = sum(1 for eix, (a, b) in enumerate(edges)
                                           if (a == i and b == j and (orientation >> eix) & 1)
                                           or (a == j and b == i and not ((orientation >> eix) & 1)))
                        if assigned[i] + paid[i] < value_i_of_j + paid[j]:
                            good = False
                            break
                    if not good:
                        break
                if good:
                    return total
    raise AssertionError('No solution')


def expected_components(n, c):
    p = (math.log(n) + math.log(math.log(n)) + c) / (2*n)
    a = math.exp(-c/2) * math.sqrt(n/math.log(n))
    k2 = (n*(n-1)/2)*p*(1-p)**(2*(n-2))
    isolated = n*(1-p)**(n-1)
    # Exact expectation of tree components on 3..n/2 vertices,
    # computed in logarithmic form for numerical stability.
    z = 0.0
    for k in range(3, n//2 + 1):
        loge = (math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
                + (k-2)*math.log(k)+(k-1)*math.log(p)
                + (k*(n-k)+k*(k-1)//2-k+1)*math.log1p(-p))
        if loge > -740:
            z += math.exp(loge)
    return isolated/a, k2, z


def run():
    total = 0
    for n in range(1, 5):
        all_edges = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            edges = [e for i, e in enumerate(all_edges) if mask >> i & 1]
            got = brute_min(n, edges)
            expect = predicted_min(n, edges)
            assert got == expect, (n, edges, got, expect)
            total += 1
    # Five-vertex archetypes: disjoint edges plus isolate, star, cycle,
    # lone tree with isolates, and cyclic-plus-isolate.
    cases = [
        [(0, 1), (2, 3)],
        [(0, 1), (0, 2), (0, 3), (0, 4)],
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)],
        [(0, 1)],
        [(0, 1), (1, 2), (2, 0)],
        [(0, 1), (1, 2), (2, 0), (3, 4)]
    ]
    for edges in cases:
        assert brute_min(5, edges) == predicted_min(5, edges)
        total += 1
    for n in (1000, 10000):
        r, l, tail = expected_components(n, 0.0)
        assert 0.6 < r < 1.6 and 0 < l < 0.5 and tail < .5, (n,r,l,tail)
        print('n=%d isolated/scale=%.6f E[K2]=%.6f E[trees>=3 <= n/2]=%.6f' % (n,r,l,tail))
    print('PASS: %d exact graph-orientation subsidy tests; two expectation checks' % total)


if __name__ == '__main__':
    run()
