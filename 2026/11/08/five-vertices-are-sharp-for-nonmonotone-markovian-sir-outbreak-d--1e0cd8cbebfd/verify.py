"""Exact checks for finite Markov SIR duration on simple undirected graphs.

Requires Python >=3.9 and sympy. Does not rely on a graph catalogue.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
import sympy as sp

z = sp.symbols('z', positive=True)


def connected(n, edges):
    reach = {0}
    while True:
        new = set(reach)
        for u, v in edges:
            if u in reach: new.add(v)
            if v in reach: new.add(u)
        if new == reach: return len(reach) == n
        reach = new


def canonical(n, edges):
    return min(tuple(sorted((min(p[u],p[v]),max(p[u],p[v]))
                             for u,v in edges)) for p in permutations(range(n)))


def exact_mean(n, edges, start, rate):
    # State is (susceptible bit mask, infectious bit mask). All other nodes removed.
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    @lru_cache(None)
    def T(s, i):
        if i == 0: return sp.Integer(0) if rate == z else Fraction(0)
        infectious = [u for u in range(n) if (i >> u) & 1]
        total = len(infectious)
        numerator = sp.Integer(1) if rate == z else Fraction(1)
        for u in infectious:
            numerator += T(s, i & ~(1 << u))
            for v in adj[u]:
                if (s >> v) & 1:
                    total += rate
                    numerator += rate * T(s & ~(1 << v), i | (1 << v))
        return sp.cancel(numerator / total) if rate == z else numerator / total
    return T(((1 << n) - 1) & ~(1 << start), 1 << start)


def small_graph_certificate():
    # Enumerate ALL 2^(n choose 2) labeled simple graphs, then quotient by
    # explicit permutation isomorphism. Disconnected components reduce to smaller n.
    catalog = defaultdict(dict)
    total_labeled = 0
    for n in range(1, 5):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = tuple(e for j,e in enumerate(possible) if (mask >> j) & 1)
            if not connected(n,edges): continue
            total_labeled += 1
            catalog[n][canonical(n,edges)] = True
    expected_classes = {1:1, 2:1, 3:2, 4:6}
    assert {n:len(catalog[n]) for n in range(1,5)} == expected_classes
    checked = 0
    for n in range(1,5):
        for edges in catalog[n]:
            for source in range(n):
                t = exact_mean(n,edges,source,z)
                numerator, denominator = sp.fraction(sp.factor(sp.diff(t,z)))
                p = sp.Poly(numerator,z)
                q = sp.Poly(denominator,z)
                assert all(c >= 0 for c in p.all_coeffs())
                assert all(c >= 0 for c in q.all_coeffs())
                assert any(c > 0 for c in q.all_coeffs())
                if n > 1: assert any(c > 0 for c in p.all_coeffs())
                checked += 1
    return total_labeled, checked, expected_classes


def witness_certificate():
    # B_3 = K_{2,3} + the edge between its two hubs (3,4).
    E = ((0,3),(0,4),(1,3),(1,4),(2,3),(2,4),(3,4))
    x = Fraction(100)
    t = exact_mean(5,E,3,x)
    h5 = sum((Fraction(1,k) for k in range(1,6)),Fraction(0))
    gap = t - h5
    assert h5 == Fraction(137,60)
    assert gap == Fraction(1326298572426638149591240301,
                           28318637979426772160758383665220)
    assert gap > 0
    return t,h5,gap

if __name__ == '__main__':
    import time
    a=time.monotonic()
    labeled,tests,classes=small_graph_certificate()
    print('Connected labeled graphs:',labeled)
    print('Isomorphism classes by n:',classes)
    print('Symbolic root tests:',tests)
    t,h,g=witness_certificate()
    print('Exact B3 expected duration at rate 100:',t)
    print('Exact high-rate limit:',h)
    print('Exact positive gap:',g,'=',float(g))
    print('PASS',round(time.monotonic()-a,3),'seconds')
