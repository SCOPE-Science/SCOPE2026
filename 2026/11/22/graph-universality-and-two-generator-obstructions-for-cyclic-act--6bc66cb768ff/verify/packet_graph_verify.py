#!/usr/bin/env python3
"""Finite independent cross-checks of a cyclic-action packet-colouring construction.

No external packages. These tests check finite instances only; the theorem relies
on its symbolic construction and the classical NP-completeness of 3-colouring.
"""
from itertools import combinations, product
from functools import lru_cache
from math import gcd, prod


def first_primes(n):
    out = []
    x = 2
    while len(out) < n:
        if all(x % p for p in out if p*p <= x):
            out.append(x)
        x += 1
    return out


def encode_graph(n, edges):
    # Edge primes followed by one private prime per vertex.
    ps = first_primes(len(edges) + n)
    d = ps[len(edges):]
    for j, (u, v) in enumerate(edges):
        d[u] *= ps[j]
        d[v] *= ps[j]
    N = prod(ps)
    return N, d, ps


def chromatic(n, edges):
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    def possible(k):
        colors = [-1]*n
        def go(i):
            if i == n:
                return True
            for c in range(k):
                if all(colors[j] != c for j in adj[i]):
                    colors[i] = c
                    if go(i+1):
                        return True
                    colors[i] = -1
            return False
        return go(0)
    return next(k for k in range(1, n+1) if possible(k))


def packet_number(d):
    n = len(d)
    indep = [False]*(1 << n)
    indep[0] = True
    for mask in range(1, 1 << n):
        v = (mask & -mask).bit_length() - 1
        rem = mask ^ (1 << v)
        indep[mask] = indep[rem] and all(gcd(d[v], d[u]) == 1 for u in range(n) if rem >> u & 1)
    @lru_cache(None)
    def f(mask):
        if not mask:
            return 0
        vbit = mask & -mask
        remaining = mask ^ vbit
        ans = n
        sub = remaining
        while True:
            block = sub | vbit
            if indep[block]:
                ans = min(ans, 1 + f(mask ^ block))
            if not sub:
                break
            sub = (sub - 1) & remaining
        return ans
    return f((1 << n)-1)


def run():
    cases = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for bits in range(1 << len(pairs)):
            edges = [e for i, e in enumerate(pairs) if bits >> i & 1]
            N, ds, primes = encode_graph(n, edges)
            assert len(set(ds)) == n and all(1 < d and N % d == 0 for d in ds)
            edge_set = set(edges)
            assert all((gcd(ds[u], ds[v]) > 1) == ((u, v) in edge_set) for u, v in pairs)
            assert packet_number(ds) == chromatic(n, edges), (n, edges)
            multiplicities = [sum(d % p == 0 for d in ds) for p in primes]
            assert max(multiplicities) == (2 if edges else 1)
            cases += 1
    ds = (6, 10, 15)
    assert packet_number(ds) == 3
    # Directly check two generators of C6 x C10 x C15, independent
    # of an invariant-factor argument.
    a = (1, 2, 0)
    b = (0, 5, 1)
    generated = {tuple((i*a[j]+k*b[j]) % ds[j] for j in range(3))
                 for i in range(30) for k in range(30)}
    assert len(generated) == prod(ds) == 900
    for r in range(2, 9):
        e = list(combinations(range(r), 2))
        N, ds, ps = encode_graph(r, e)
        assert packet_number(ds) == r
        assert max(sum(d%p==0 for d in ds) for p in ps) == 2
    print(f'PACKET_GRAPH_VERIFY_OK graphs={cases} (all labeled simple graphs with 1..5 vertices)')
    print('TRIANGLE_GROUP_GENERATORS_OK order=900 two_generators=True packets=3')
    print('COMPLETE_GRAPH_GAP_OK ranks=2 packets=2..8')

if __name__ == '__main__':
    run()
