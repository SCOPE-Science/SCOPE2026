"""Independent exhaustive verification of connected zero-forcing sets on partially whiskered cycles.

Run: python verify_partial_sunlet.py
Requires only Python 3 standard library.
"""
from collections import Counter


def predicted_polynomial(n, A):
    """All-cardinality interval formula, independently of any forcing simulation."""
    A = set(A)
    out = Counter()
    for b in range(len(A) + 1):
        from math import comb
        out[n + b] += comb(len(A), b)
    for size in range(2, n):
        for start in range(n):
            included = [(start + j) % n for j in range(size)]
            gap = [(start + size + j) % n for j in range(n - size)]
            left, right = included[-1], included[0]
            internal = sum(x in A for x in included[1:-1])
            marks = [i + 1 for i, v in enumerate(gap) if v in A]
            m = len(gap)
            for e in (0, 1):
                for f in (0, 1):
                    # An undecorated boundary is always active.
                    if left not in A and e != 1: continue
                    if right not in A and f != 1: continue
                    L = (marks[0] if marks else m) if e else 0
                    R = (m + 1 - marks[-1] if marks else m) if f else 0
                    if L + R < m: continue
                    required = (left in A and e == 1) + (right in A and f == 1)
                    for j in range(internal + 1):
                        from math import comb
                        out[size + required + j] += comb(internal, j)
    return {k: v for k,v in out.items() if v}


def graph(n, A):
    """Adjacency lists with explicit pendant vertices, no formulas."""
    A = sorted(A)
    adj = [set() for _ in range(n + len(A))]
    for v in range(n):
        w = (v + 1) % n
        adj[v].add(w); adj[w].add(v)
    for j, v in enumerate(A):
        adj[v].add(n + j); adj[n + j].add(v)
    return adj


def is_connected(adj, S):
    if not S: return False
    seen = {next(iter(S))}
    while True:
        nxt = seen | (set().union(*(adj[x] for x in seen)) & S)
        if nxt == seen: return seen == S
        seen = nxt


def is_forcing(adj, S):
    colored = set(S)
    while True:
        newly = set()
        for v in colored:
            white = adj[v] - colored
            if len(white) == 1: newly.update(white)
        if not newly: return len(colored) == len(adj)
        colored.update(newly)


def exhaustive_polynomial(n, A):
    adj = graph(n, A)
    out = Counter()
    for bits in range(1, 1 << len(adj)):
        S = {i for i in range(len(adj)) if bits & (1 << i)}
        if is_connected(adj, S) and is_forcing(adj, S):
            out[len(S)] += 1
    return dict(out)


def test():
    cases = 0
    for n in range(3, 7):
        for bits in range(1 << n):
            A = {i for i in range(n) if bits & (1 << i)}
            actual = exhaustive_polynomial(n, A)
            predicted = predicted_polynomial(n, A)
            if actual != predicted:
                raise AssertionError((n, sorted(A), actual, predicted))
            cases += 1
    # Independent sums for two same-degree-sequence, non-isomorphic leaf placements.
    A = predicted_polynomial(7, {0,1,2})
    B = predicted_polynomial(7, {0,2,4})
    assert A == {3:6,4:14,5:22,6:30,7:32,8:21,9:7,10:1}, A
    assert B == {5:8,6:20,7:26,8:19,9:7,10:1}, B
    assert A == exhaustive_polynomial(7, {0,1,2})
    assert B == exhaustive_polynomial(7, {0,2,4})
    # Fully whiskered-cycle formula, including the special triangle case.
    for n in range(3, 15):
        from math import comb
        p = predicted_polynomial(n, set(range(n)))
        assert min(p) == n and p[n] == (7 if n == 3 else 3*n + 1)
        assert sum(p.values()) == (17 if n == 3 else (7*n+16)*(2**(n-4)))
    print('VERIFY_OK exhaustive_leaf_patterns=120 n=3..6 labelled_placement_comparisons='+str(cases))
    print('DEGREE_SEQUENCE_CONTRAST_PASS n=7 three_leaves min_sizes=3_and_5')
    print('KNOWN_SUNLET_SPECIALIZATION_PASS n=3..14')

if __name__ == '__main__': test()
