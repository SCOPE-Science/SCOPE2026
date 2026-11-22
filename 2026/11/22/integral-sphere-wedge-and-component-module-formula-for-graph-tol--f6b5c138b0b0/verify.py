"""Finite checks for the homotopy-profile formula of graph tolerance complexes.

Uses a direct face rule and independent sparse mod-two boundary elimination.
Finite checks supplement the general integral proof; they do not certify it.
"""
from itertools import combinations
from math import comb
from collections import defaultdict


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def bitrank(columns):
    pivots = {}
    for col in columns:
        x = col
        while x:
            high = x.bit_length() - 1
            if high in pivots:
                x ^= pivots[high]
            else:
                pivots[high] = x
                break
    return len(pivots)


def profile(n, graphmask, t, potential_edges=None):
    if potential_edges is None:
        potential_edges = tuple(combinations(range(n), 2))
    edges = [pair for i, pair in enumerate(potential_edges) if graphmask >> i & 1]
    parent = list(range(n))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        parent[root(u)] = root(v)
    c = len({root(i) for i in range(n)})
    edgemasks = [(1 << u) | (1 << v) for u, v in edges]
    lower = tuple(combinations(range(n), t + 1))
    index = {f: k for k, f in enumerate(lower)}
    top = []
    independent = 0
    for face in combinations(range(n), t + 2):
        x = sum(1 << u for u in face)
        if any((x & e) == e for e in edgemasks):
            top.append(face)
        else:
            independent += 1
    boundaries = [sum(1 << index[face[:j] + face[j+1:]] for j in range(t+2))
                  for face in top]
    rank = bitrank(boundaries)
    predicted_low = choose(c - 1, t + 1)
    predicted_top = choose(n - 1, t + 2) - independent + predicted_low
    actual_low = choose(n - 1, t + 1) - rank
    actual_top = len(top) - rank
    assert actual_low == predicted_low, (n, t, graphmask, c, actual_low, predicted_low)
    assert actual_top == predicted_top, (n, t, graphmask, actual_top, predicted_top)
    return c, independent, actual_low, actual_top


def exact_integer_examples():
    from sympy import ZZ, Matrix
    from sympy.matrices.normalforms import smith_normal_form
    from sympy.polys.domains import ZZ as DZZ
    examples = [
        ('path-7', 7, [(i, i + 1) for i in range(6)], 2),
        ('cycle-7', 7, [(i, (i+1)%7) for i in range(7)], 2),
        ('two-triangles', 6, [(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)], 2),
        ('empty-7', 7, [], 2),
        ('disconnected-7', 7, [(0,1),(1,2),(3,4)], 3),
    ]
    for name, n, edges, t in examples:
        fs = list(combinations(range(n), t+1))
        ix = {face:i for i,face in enumerate(fs)}
        es = {tuple(sorted(e)) for e in edges}
        tops = [f for f in combinations(range(n), t+2)
                if any(tuple(sorted(e)) in es for e in combinations(f,2))]
        B = Matrix.zeros(len(fs), len(tops))
        for j, f in enumerate(tops):
            for k in range(t+2):
                B[ix[f[:k]+f[k+1:]], j] = (-1)**k
        normal = smith_normal_form(B, domain=DZZ)
        nonzero = [abs(int(normal[i,i])) for i in range(min(normal.shape)) if normal[i,i] != 0]
        assert all(x == 1 for x in nonzero), (name, nonzero)
        allowed = set(es)
        em = list(combinations(range(n),2))
        mask = sum(1 << i for i, e in enumerate(em) if e in allowed)
        c, ind, lo, hi = profile(n, mask, t, em)
        assert len(nonzero) == choose(n-1,t+1)-lo
        print(f'INTEGER {name}: n={n}, t={t}, components={c}, independent={ind}, H_{t}=Z^{lo}, H_{t+1}=Z^{hi}, all Smith factors=1')


def main():
    all_cases = 0
    for n in range(2, 7):
        potential_edges = tuple(combinations(range(n),2))
        checked = 0
        for graphmask in range(1 << len(potential_edges)):
            for t in range(2, min(4, n - 2)+1):
                profile(n, graphmask, t, potential_edges)
                checked += 1
        print(f'EXHAUSTIVE n={n}: {checked} graph-and-tolerance cases; all mod-two boundary ranks agree')
        all_cases += checked
    print('EXHAUSTIVE TOTAL', all_cases)
    exact_integer_examples()
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()
