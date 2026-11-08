"""Exhaustive direct neighborhood checker for identifying codes on crown graphs.
Run with Python 3: python verify_direct.py
No third-party dependencies.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb


def original_graph_neighborhoods(n):
    out = []
    for i in range(n):
        out.append((1 << i) | sum(1 << (n + j) for j in range(n) if i != j))
    for i in range(n):
        out.append((1 << (n + i)) | sum(1 << j for j in range(n) if i != j))
    return out


def identifying(code, nb):
    traces = [code & neighbors for neighbors in nb]
    return all(traces) and len(set(traces)) == len(nb)


def combinatorial_state(code, n):
    state = []
    for i in range(n):
        aa = (code >> i) & 1
        bb = (code >> (n + i)) & 1
        if aa and bb:
            return None
        state.append(1 if aa else (2 if bb else 0))
    return tuple(state)


def expected_states(n):
    for hole in range(n):
        ids = [i for i in range(n) if i != hole]
        for p in range(2, n - 2):
            for aa in combinations(ids, p):
                state = [2] * n
                state[hole] = 0
                for i in aa: state[i] = 1
                yield tuple(state)


def state_code(state, n):
    return sum(1 << i for i, v in enumerate(state) if v == 1) | sum(1 << (n + i) for i, v in enumerate(state) if v == 2)


def direct_slide_graph(codes, n):
    S = set(codes)
    edges = {code: [] for code in codes}
    for code in codes:
        for u in range(2 * n):
            if not (code >> u) & 1:
                continue
            for v in range(2 * n):
                if code >> v & 1:
                    continue
                if ((u < n) == (v < n)) or ((u % n) == (v % n)):
                    continue
                candidate = code ^ (1 << u) ^ (1 << v)
                if candidate in S:
                    edges[code].append(candidate)
    for code, neighbors in edges.items():
        assert len(neighbors) == len(set(neighbors))
        for other in neighbors:
            assert code in edges[other]
    return edges


def components(G):
    unseen = set(G)
    out = []
    while unseen:
        root = next(iter(unseen)); unseen.remove(root)
        todo = [root]
        for u in todo:
            for v in G[u]:
                if v in unseen:
                    unseen.remove(v); todo.append(v)
        out.append(todo)
    return out


for n in range(5, 10):
    nb = original_graph_neighborhoods(n)
    k = n - 1
    # A size-(k-1) code cannot identify: any smaller identifying code
    # would extend to size k-1 by adding arbitrary vertices.
    assert all(not identifying(sum(1 << v for v in t), nb)
               for t in combinations(range(2 * n), k - 1))
    found = set()
    for t in combinations(range(2 * n), k):
        code = sum(1 << v for v in t)
        if identifying(code, nb):
            found.add(code)
    predicted = {state_code(x, n) for x in expected_states(n)}
    assert found == predicted
    assert len(found) == n * (2 ** (n - 1) - 2 * n)
    G = direct_slide_graph(found, n)
    sizes = Counter(map(len, components(G)))
    target = {5: Counter({1: 30}), 6: Counter({6: 20})}.get(n)
    if target:
        assert sizes == target, (n, sizes)
    else:
        assert sizes == Counter({len(found): 1}), (n, sizes)
    if n == 6:
        assert all(sum(1 for v in G[u] if v != u) == 3 for u in G)
        # Each component is K3,3: every pair of opposite-side vertices adjacent.
        for comp in components(G):
            assert len(comp) == 6 and all(len(G[x]) == 3 for x in comp)
            sides = {x:sum(1 for i in range(n) if x & (1 << i)) for x in comp}
            assert set(sides.values()) == {2, 3}
            assert all((sides[x] != sides[y]) == (y in G[x]) for x in comp for y in comp if x != y)
    expected_edges = n * (n - 1) // 2 * (2 ** (n - 1) - 4 * n + 4)
    assert sum(map(len, G.values())) // 2 == expected_edges
    print(f'n={n} min={k} codes={len(found)} edges={expected_edges} components={dict(sizes)} PASS')
print('ALL_DIRECT_CHECKS_PASS')
