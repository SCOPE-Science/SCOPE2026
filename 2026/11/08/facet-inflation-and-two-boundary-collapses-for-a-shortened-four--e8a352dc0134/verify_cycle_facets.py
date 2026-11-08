"""Exact rational checks for four-cycle-shortened finite metric facets.

No nonstandard packages are required.  The Prüfer enumeration is independent
of the four-value state classification in the mathematical proof.
"""
from fractions import Fraction
from itertools import product
from collections import Counter

EDGES = frozenset({(0, 1), (1, 2), (2, 3), (0, 3)})

def short(i, j):
    return tuple(sorted((i, j))) in EDGES

def dist(i, j, t):
    return t if short(i, j) else Fraction(1)

def core_count(t, anchor):
    v = sorted({Fraction(0), 1 - t, t, Fraction(1)})
    counts = Counter()
    for q in product(range(len(v)), repeat=4):
        if any(abs(v[q[i]] - v[q[j]]) > dist(i, j, t)
               for i in range(4) for j in range(i + 1, 4)):
            continue
        adj = [[] for _ in range(4)]
        for i in range(4):
            for j in range(i + 1, 4):
                if abs(v[q[i]] - v[q[j]]) == dist(i, j, t):
                    adj[i].append(j); adj[j].append(i)
        used = set(); valid = True
        for i in range(4):
            if i in used:
                continue
            comp, todo = set(), [i]
            while todo:
                a = todo.pop()
                if a not in comp:
                    comp.add(a); todo.extend(adj[a])
            used.update(comp)
            if not any(v[q[a]] in anchor for a in comp):
                valid = False
        if valid:
            counts[tuple(q.count(j) for j in range(len(v)))] += 1
    return counts

def tree_edges(code, n):
    """Decode Prüfer word into all labelled trees; duplicates do not occur."""
    deg = [1] * n
    for x in code:
        deg[x] += 1
    out = []
    for x in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        out.append((leaf, x))
        deg[leaf] -= 1; deg[x] -= 1
    rem = [i for i in range(n) if deg[i] == 1]
    out.append((rem[0], rem[1]))
    return out

def exhaustive_vertices(n, t):
    """All spanning trees and every tight-edge orientation, exact arithmetic."""
    vertices = set()
    pairs = [(i, j, dist(i, j, t)) for i in range(n) for j in range(i + 1, n)]
    for word in product(range(n), repeat=n - 2):
        edges = tree_edges(word, n)
        links = [[] for _ in range(n)]
        for i, j in edges:
            d = dist(i, j, t)
            links[i].append((j, d)); links[j].append((i, d))
        root = n - 1
        parent = {root: -1}; order = [root]
        for v in order:
            for w, d in links[v]:
                if w not in parent:
                    parent[w] = v; order.append(w)
        dt = {tuple(sorted((v, parent[v]))): dist(v, parent[v], t)
              for v in range(n) if v != root}
        order_pairs = sorted(dt)
        for signs in product((-1, 1), repeat=n - 1):
            signed = {e: s * dt[e] for e, s in zip(order_pairs, signs)}
            pot = {root: Fraction(0)}
            for v in order[1:]:
                p = parent[v]
                e = tuple(sorted((v, p)))
                pot[v] = pot[p] + (signed[e] if v < p else -signed[e])
            if all(abs(pot[i] - pot[j]) <= d for i, j, d in pairs):
                vertices.add(tuple(pot[i] for i in range(n - 1)))
    return len(vertices)

def formula(n, t):
    k = n - 4
    if t == Fraction(1, 2):
        return 26 * 2**k - 22
    if Fraction(1, 2) < t < Fraction(1):
        return 38 * 2**k - 22
    if t == Fraction(1):
        return 2**n - 2
    raise ValueError('Outside theorem domain')

def main():
    for t, a, b in [(Fraction(1, 2), 26, 15),
                    (Fraction(3, 4), 38, 27),
                    (Fraction(7, 8), 38, 27)]:
        two = core_count(t, {Fraction(0), Fraction(1)})
        one = core_count(t, {Fraction(1)})
        assert sum(two.values()) == a, (t, two)
        assert sum(one.values()) == b, (t, one)
        print('STATE_COUNTS', str(t), a, b, sorted(two.items()), sorted(one.items()))
        for n in (5, 6):
            computed = exhaustive_vertices(n, t)
            asserted = formula(n, t)
            print('EXHAUSTIVE_TIGHT_TREES', n, str(t), computed, asserted)
            assert computed == asserted
    for n in (5, 6):
        computed = exhaustive_vertices(n, Fraction(1))
        assert computed == formula(n, Fraction(1))
        print('EQUILATERAL_ENDPOINT', n, computed)
    print('ALL_SHORT_CYCLE_FACET_CHECKS_PASSED')
if __name__ == '__main__':
    main()
