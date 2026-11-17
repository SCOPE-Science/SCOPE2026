#!/usr/bin/env python3
"""Independent finite checks for reflection folding of noncrossing-forest complexes.
Only Python's standard library is needed. These checks support, not replace, the universal proof.
"""
from itertools import combinations
from collections import Counter
from math import comb

def crossing(e, f):
    a, b = sorted(e)
    c, d = sorted(f)
    return (a < c < b < d) or (c < a < d < b)

def acyclic(edges, n):
    par = list(range(n))
    def root(i):
        while par[i] != i:
            par[i] = par[par[i]]
            i = par[i]
        return i
    for a, b in edges:
        x, y = root(a), root(b)
        if x == y:
            return False
        par[x] = y
    return True

def fold_edge(edge, m):
    i, j = sorted(edge)
    def pair(t):
        return m + 2 - t, m + t - 1
    if (i, j) == (0, 1):
        return ((0, 1),)
    if i == 1:
        return (tuple(sorted(pair(j))),)
    if i == 0:
        a, b = pair(j)
        return tuple(sorted(((0, b), (1, a))))
    a, b = pair(i)
    c, d = pair(j)
    return tuple(sorted((tuple(sorted((a, c))), tuple(sorted((b, d))))))

def admissible_orbits(m):
    n = 2*m
    seen, result = set(), set()
    for edge in combinations(range(n), 2):
        if edge in seen:
            continue
        a, b = edge
        partner = tuple(sorted(((1-a) % n, (1-b) % n)))
        orbit = tuple(sorted(set((edge, partner))))
        seen.update(orbit)
        if acyclic(orbit, n) and not any(crossing(e, f) for e, f in combinations(orbit, 2)):
            result.add(orbit)
    return result

def admissible_small(edges, n):
    return acyclic(edges, n) and not any(crossing(a, b) for a, b in combinations(edges, 2))

def faces_of_complex(n, lifting):
    edges = list(combinations(range(n), 2))
    f = Counter({0: 1})
    for k in range(1, n):
        for face in combinations(edges, k):
            if admissible_small(face, n):
                if lifting is not None:
                    expanded = [ee for e in face for ee in lifting[e]]
                    assert admissible_small(expanded, 2*(n-1)), (n, face)
                f[k] += 1
    return f

def known_f(n, edges_count):
    k = n-edges_count
    return comb(n, k-1)*comb(3*n-2*k-1, n-k)//(2*n-k)

def main():
    pairs = 0
    for m in range(2, 13):
        base = list(combinations(range(m+1), 2))
        lifts = {edge: fold_edge(edge, m) for edge in base}
        assert set(lifts.values()) == admissible_orbits(m)
        for a, b in combinations(base, 2):
            direct = crossing(a, b)
            folded = any(crossing(u, v) for u in lifts[a] for v in lifts[b])
            assert direct == folded, (m, a, b)
            pairs += 1
    print(f'ORBIT_AND_PAIRWISE_CROSSINGS_PASS m=2..12 compared_pairs={pairs}')
    for m in range(2, 7):
        base = list(combinations(range(m+1), 2))
        lifts = {edge: fold_edge(edge, m) for edge in base}
        subsets = 0
        for k in range(len(base)+1):
            for face in combinations(base, k):
                assert acyclic(face, m+1) == acyclic([ee for e in face for ee in lifts[e]], 2*m), (m, face)
                subsets += 1
        print(f'ACYCLIC_EQUIVALENCE_PASS m={m} exhaustive_subsets={subsets}')
    for n in range(3, 9):
        m = n-1
        lifts = {e: fold_edge(e, m) for e in combinations(range(n), 2)}
        f = faces_of_complex(n, lifts)
        assert [f[k] for k in range(n)] == [known_f(n, k) for k in range(n)]
        print(f'FACE_VECTOR_PASS n={n} faces_by_edge_count={[f[k] for k in range(n)]}')
    print('NONCROSSING_FOREST_REFLECTION_FOLDING_PASS')

if __name__ == '__main__':
    main()
