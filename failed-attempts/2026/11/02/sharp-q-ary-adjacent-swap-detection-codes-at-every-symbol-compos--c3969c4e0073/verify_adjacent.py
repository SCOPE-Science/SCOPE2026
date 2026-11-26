#!/usr/bin/env python3
"""Independent graph verification of exact one-adjacent-swap detection code size.
No external packages. Execute: python verify_adjacent.py
"""
from itertools import product
from collections import deque, Counter
from math import factorial, comb


def inversion_parity(word):
    return sum(word[i] > word[j] for i in range(len(word)) for j in range(i + 1, len(word))) % 2


def expected_unmatched(profile):
    odds = [v % 2 for v in profile]
    n = sum(profile)
    if n % 2 != sum(odds) or sum(odds) > 1:
        return 0
    m = n // 2
    denom = 1
    for v in profile:
        denom *= factorial(v // 2)
    return factorial(m) // denom


def hopcroft_karp(edges, left_vertices, right_vertices):
    mate_l, mate_r, d = {}, {}, {}
    infinite = 10 ** 12
    def bfs():
        queue = deque()
        found = False
        for u in left_vertices:
            if u not in mate_l:
                d[u] = 0
                queue.append(u)
            else:
                d[u] = infinite
        while queue:
            u = queue.popleft()
            for v in edges[u]:
                parent = mate_r.get(v)
                if parent is None:
                    found = True
                elif d.get(parent, infinite) == infinite:
                    d[parent] = d[u] + 1
                    queue.append(parent)
        return found
    def dfs(u):
        for v in edges[u]:
            parent = mate_r.get(v)
            if parent is None or (d.get(parent, infinite) == d[u] + 1 and dfs(parent)):
                mate_l[u] = v
                mate_r[v] = u
                return True
        d[u] = infinite
        return False
    while bfs():
        for u in left_vertices:
            if u not in mate_l:
                dfs(u)
    return len(mate_l)


def check(q, n):
    words = list(product(range(q), repeat=n))
    even = [w for w in words if inversion_parity(w) == 0]
    odd = set(words) - set(even)
    edges = {}
    for w in even:
        out = set()
        for i in range(n - 1):
            if w[i] != w[i + 1]:
                v = w[:i] + (w[i + 1], w[i]) + w[i + 2:]
                assert v in odd
                out.add(v)
        edges[w] = out
    matching = hopcroft_karp(edges, even, odd)
    answer = len(words) - matching
    formula = (q**n + q**((n + 1) // 2)) // 2
    assert answer == formula == len(even), (q, n, answer, formula, len(even))
    assert len(even) + len(odd) == len(words)
    groups = Counter(tuple(w.count(a) for a in range(q)) for w in words)
    for profile, count in groups.items():
        U = expected_unmatched(profile)
        group_even = sum(1 for w in even if tuple(w.count(a) for a in range(q)) == profile)
        assert group_even * 2 == count + U, (q,n,profile,group_even,count,U)
    return len(words), len(even), matching, len(groups)


def main():
    total = total_profiles = 0
    cases = [(2,n) for n in range(1,11)] + [(3,n) for n in range(1,8)] + [(4,n) for n in range(1,6)]
    for q,n in cases:
        vertices,_,_,profiles = check(q,n)
        total+=vertices
        total_profiles+=profiles
    print(f'ADJ_SWAP_VERIFY_OK cases={len(cases)} vertices={total} parikh_profiles={total_profiles} formula_and_maximum_matching=True')

if __name__ == '__main__':
    main()
