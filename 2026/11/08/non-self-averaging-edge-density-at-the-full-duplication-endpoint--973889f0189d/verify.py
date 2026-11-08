"""Exact checks for a full-neighborhood duplication process.

Run with `python verify.py`. Uses Python's standard library only.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations


def edges(graph):
    return sum(x.bit_count() for x in graph) // 2


def stars(graph):
    return sum(x.bit_count() * (x.bit_count() - 1) // 2 for x in graph)


def states(n):
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        g = [0] * n
        for j, (a, b) in enumerate(pairs):
            if mask >> j & 1:
                g[a] |= 1 << b
                g[b] |= 1 << a
        yield tuple(g)


def next_graph(g, parent, link):
    n = len(g)
    h = list(g) + [0]
    new_mask = g[parent] | ((1 << parent) if link else 0)
    h[n] = new_mask
    for v in range(n):
        if new_mask >> v & 1:
            h[v] |= 1 << n
    return tuple(h)


def successors(g, r):
    n = len(g)
    for u in range(n):
        for link, p in [(0, 1 - r), (1, r)]:
            if p:
                yield next_graph(g, u, link), p / n


def first(n, r):
    return r * n * (n-1) / 2


def second_star(n, r):
    return r * (1 + 2*r) * n * (n-1) * (n-2) / 6


def edge_second(n, r):
    return n*r*(n-1)*(7*n*n*r+2*n*n-11*n*r+2*n-6*r+6)/36


def edge_var(n, r):
    return n*(n-1)*(n*n+n+3)*r*(1-r)/18


def main():
    tests = 0
    for r in (Q(0), Q(1, 3), Q(2, 5), Q(1)):
        for n in range(1, 5):
            for g in states(n):
                e, s = edges(g), stars(g)
                d1 = d2 = ds = Q(0)
                total = Q(0)
                for h, p in successors(g, r):
                    inc = edges(h) - e
                    d1 += p * inc
                    d2 += p * inc*inc
                    ds += p * (stars(h) - s)
                    total += p
                assert total == 1
                assert d1 == Q(2*e, n) + r
                assert ds == Q(3*s + (2+4*r)*e, n)
                assert d2 == Q(2*s + 2*e, n) + Q(4*r*e, n) + r
                tests += 4
        law = { (0,): Q(1) }
        for n in range(1, 7):
            ebar = sum(p*edges(g) for g,p in law.items())
            sbar = sum(p*stars(g) for g,p in law.items())
            e2 = sum(p*edges(g)**2 for g,p in law.items())
            assert ebar == first(n, r)
            assert sbar == second_star(n, r)
            assert e2 == edge_second(n, r)
            assert e2 - ebar**2 == edge_var(n, r)
            tests += 4
            if n == 6:
                break
            next_law = defaultdict(Q)
            for g, p in law.items():
                for h, q in successors(g, r):
                    next_law[h] += p*q
            law = dict(next_law)
            assert sum(law.values()) == 1
            tests += 1
        for n in range(1, 40):
            assert first(n+1,r) == (1+Q(2,n))*first(n,r)+r
            assert second_star(n+1,r) == (1+Q(3,n))*second_star(n,r) + (2+4*r)*first(n,r)/n
            assert edge_second(n+1,r) == (1+Q(4,n))*edge_second(n,r) + 2*r*first(n,r) + (2*second_star(n,r)+(2+4*r)*first(n,r))/n + r
            assert edge_second(n,r)-first(n,r)**2 == edge_var(n,r)
            tests += 4
    print(f"PASS: {tests} exact transition, finite-enumeration and moment-recurrence checks")


if __name__ == '__main__':
    main()
