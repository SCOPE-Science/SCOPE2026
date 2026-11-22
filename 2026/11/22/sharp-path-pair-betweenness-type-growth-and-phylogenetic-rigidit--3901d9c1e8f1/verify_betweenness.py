"""Independent finite tests for the path-pair betweenness-trace theorem.

Usage: python3 verify_betweenness.py
Only Python 3 standard library is required.  Finite tests do not prove the theorem.
"""
from collections import deque
from itertools import combinations, product
from math import prod


def from_prufer(seq, n):
    deg = [1] * n
    for v in seq:
        deg[v] += 1
    g = [set() for _ in range(n)]
    for v in seq:
        u = next(i for i in range(n) if deg[i] == 1)
        g[u].add(v)
        g[v].add(u)
        deg[u] -= 1
        deg[v] -= 1
    a, b = [i for i in range(n) if deg[i] == 1]
    g[a].add(b)
    g[b].add(a)
    return {i: set(g[i]) for i in range(n)}


def tree_path(g, a, b):
    q = deque([a])
    pred = {a: None}
    while q:
        u = q.popleft()
        if u == b:
            break
        for v in g[u]:
            if v not in pred:
                pred[v] = u
                q.append(v)
    result = []
    v = b
    while v is not None:
        result.append(v)
        v = pred[v]
    return result


def trace_family(g, A):
    pairs = list(combinations(A, 2))
    signatures = {v: 0 for v in g}
    for bit, (a, b) in enumerate(pairs):
        for v in tree_path(g, a, b):
            signatures[v] |= 1 << bit
    return frozenset(signatures.values())


def core_formula(g, A):
    A = set(A)
    h = set(A)
    for a, b in combinations(sorted(A), 2):
        h.update(tree_path(g, a, b))
    H = {v: g[v] & h for v in h}
    essential = A | {v for v in h if len(H[v]) >= 3}
    branching = len(essential) - len(A)
    subdivided_nonpendant = 0
    for u in essential:
        for first in H[u]:
            prev, cur, inside = u, first, 0
            while cur not in essential:
                inside += 1
                nxt = [v for v in H[cur] if v != prev]
                assert len(nxt) == 1
                prev, cur = cur, nxt[0]
            if u < cur and inside and len(H[u]) > 1 and len(H[cur]) > 1:
                subdivided_nonpendant += 1
    outside = int(len(h) < len(g))
    return len(A) + branching + subdivided_nonpendant + outside


def add_edge(g, u, v):
    g[u].add(v)
    g[v].add(u)


def remove_edge(g, u, v):
    g[u].remove(v)
    g[v].remove(u)


def binary_leaf_trees(m):
    # Leaves are exactly 0,...,m-1; internal vertices have negative names.
    trees = [{0: {-1}, 1: {-1}, 2: {-1}, -1: {0, 1, 2}}]
    for leaf in range(3, m):
        following = []
        for g in trees:
            for u, ns in g.items():
                for v in ns:
                    if u >= v:
                        continue
                    h = {x: set(ys) for x, ys in g.items()}
                    new = min(h) - 1
                    h[new] = set()
                    h[leaf] = set()
                    remove_edge(h, u, v)
                    add_edge(h, u, new)
                    add_edge(h, v, new)
                    add_edge(h, new, leaf)
                    following.append(h)
        trees = following
    return trees


def fully_witnessed_binary_tree(g, m):
    h = {x: set(ys) for x, ys in g.items()}
    for u, v in [(u, v) for u in g for v in g[u] if u < v and u < 0 and v < 0]:
        new = min(h) - 1
        h[new] = set()
        remove_edge(h, u, v)
        add_edge(h, u, new)
        add_edge(h, v, new)
    new = min(h) - 1
    h[new] = set()
    add_edge(h, 0, new)
    assert len(h) == 3*m - 4
    return h


def check():
    tested = 0
    for n in range(3, 8):
        for prufer in product(range(n), repeat=n-2):
            g = from_prufer(prufer, n)
            for m in range(3, n+1):
                A = tuple(range(m))
                actual = len(trace_family(g, A))
                predicted = core_formula(g, A)
                assert actual == predicted, (n, prufer, m, actual, predicted)
                assert actual <= min(n, 3*m-4)
                tested += 1
    print('EXHAUSTIVE_LABELED_TREE_MARKING_TESTS_OK', tested)
    for m in range(3, 8):
        observed = set()
        for g in binary_leaf_trees(m):
            witness = fully_witnessed_binary_tree(g, m)
            f = trace_family(witness, tuple(range(m)))
            assert len(f) == 3*m-4
            observed.add(tuple(sorted(f)))
        target = prod(range(1, 2*m-4, 2))  # (2m-5)!!
        assert len(observed) == target, (m, len(observed), target)
        print('BINARY_EXTREMAL_FAMILIES_OK', m, target)
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    check()
