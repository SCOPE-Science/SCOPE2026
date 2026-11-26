#!/usr/bin/env python3
"""Independent finite verification of a graph-theoretic characterization. Python standard library only."""
from itertools import product
from collections import Counter

def edges_of_comb(n):
    return [(i, i + 1) for i in range(n - 1)]

def direct_minimal_forts(n, edges):
    adj = [0] * (2 * n)
    for i in range(n):
        adj[i] |= 1 << (n + i)
        adj[n + i] |= 1 << i
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    forts = []
    for mask in range(1, 1 << (2 * n)):
        if all((adj[v] & mask).bit_count() != 1
               for v in range(2 * n) if not (mask >> v & 1)):
            forts.append(mask)
    minimal = []
    for mask in sorted(forts, key=int.bit_count):
        if not any((smaller & mask) == smaller for smaller in minimal):
            minimal.append(mask)
    return set(minimal)

def predicted_minimal_forts(n, edges):
    nbr = [set() for _ in range(n)]
    for u, v in edges:
        nbr[u].add(v)
        nbr[v].add(u)
    result = set()
    for a in range(1, 1 << n):
        selected = [i for i in range(n) if a >> i & 1]
        count = [sum((a >> j) & 1 for j in nbr[i]) for i in range(n)]
        links = {i: set() for i in selected}
        for v in range(n):
            if not (a >> v & 1) and count[v] == 2:
                u, w = [i for i in nbr[v] if a >> i & 1]
                links[u].add(w)
                links[w].add(u)
        seen = {selected[0]}
        todo = [selected[0]]
        while todo:
            for u in links[todo.pop()]:
                if u not in seen:
                    seen.add(u)
                    todo.append(u)
        if len(seen) != len(selected):
            continue
        f = a
        for v in range(n):
            if (a >> v & 1) or count[v] == 1:
                f |= 1 << (n + v)
        result.add(f)
    return result

def expected_comb_poly(n):
    answer = Counter()
    for a in range(n):
        for b in range(a, n, 2):
            size = b - a + 2 + int(a > 0) + int(b < n - 1)
            answer[size] += 1
    return answer

# Six representative unlabeled trees with six vertices, obtained from degree partitions.
trees6 = [
    [(0,1),(1,2),(2,3),(3,4),(4,5)],
    [(0,1),(0,2),(0,3),(0,4),(0,5)],
    [(0,1),(0,2),(0,3),(0,4),(4,5)],
    [(0,1),(0,2),(0,3),(3,4),(4,5)],
    [(0,1),(0,2),(0,3),(3,4),(3,5)],
    [(0,1),(0,2),(0,3),(1,4),(2,5)],
]
for n in range(2, 9):
    actual = direct_minimal_forts(n, edges_of_comb(n))
    predicted = predicted_minimal_forts(n, edges_of_comb(n))
    assert actual == predicted, (n, len(actual), len(predicted))
    poly = Counter(m.bit_count() for m in actual)
    assert poly == expected_comb_poly(n), (n, poly)
    assert len(actual) == (n + 1) ** 2 // 4, n
    assert set(poly) == set(range(3, n + 2)), n
    assert poly[3] == 2 and poly[n + 1] == 2, n
    print('COMB', n, len(actual), sorted(poly.items()), 'PASS')
for n in range(2, 6):
    # Prüfer codes enumerate all labelled trees, including isomorphic duplicates.
    seen_count = 0
    for code in product(range(n), repeat=n-2):
        deg = [1] * n
        for x in code: deg[x] += 1
        edges = []
        for x in code:
            leaf = next(i for i in range(n) if deg[i] == 1)
            edges.append((leaf,x))
            deg[leaf] -= 1
            deg[x] -= 1
        u,v=[i for i in range(n) if deg[i]==1]
        edges.append((u,v))
        assert direct_minimal_forts(n,edges)==predicted_minimal_forts(n,edges),(n,code)
        seen_count += 1
    print('ALL_LABELLED_TREE_CORES',n,seen_count,'PASS')
for i,ed in enumerate(trees6):
    assert direct_minimal_forts(6,ed)==predicted_minimal_forts(6,ed),i
print('SIX_TREE_REPRESENTATIVES_6 PASS')
print('VERIFY_OK')
