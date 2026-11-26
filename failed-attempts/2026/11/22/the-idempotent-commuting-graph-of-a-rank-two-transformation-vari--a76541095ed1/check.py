"""Direct finite verification of rank-two sandwich idempotent commuting graphs.

Only the Python standard library is needed. Finite checks corroborate,
but do not replace, the all-degree proof in RESULT.md.
"""
from itertools import product
from collections import Counter


def compose(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def star(f, a, g):
    return compose(compose(f, a), g)


def check(a):
    n = len(a)
    assert n >= 2 and len(set(a)) == 2
    outputs = sorted(set(a))
    fibers = [{i for i, value in enumerate(a) if value == z} for z in outputs]
    u, v = map(len, fibers)
    t = 2 ** (n - 2)
    maps = list(product(range(n), repeat=n))
    idem = [f for f in maps if star(f, a, f) == f]
    constants = [f for f in idem if len(set(f)) == 1]
    rank_two = [f for f in idem if len(set(f)) == 2]
    assert len(constants) == n
    assert len(rank_two) == u * v * t
    # All degree-two vertices correspond to rank-two sandwich idempotents.
    degrees = Counter()
    neighbors = {f: [] for f in idem}
    edges = 0
    for i, f in enumerate(idem):
        for g in idem[:i]:
            if star(f, a, g) == star(g, a, f):
                neighbors[f].append(g)
                neighbors[g].append(f)
                edges += 1
    assert edges == 2 * len(rank_two)
    assert all(len(neighbors[f]) == 2 for f in rank_two)
    assert all(len(neighbors[f]) == (v if f[0] in fibers[0] else u)*t for f in constants)
    for f in rank_two:
        assert set(neighbors[f]) == {tuple([z]*n) for z in set(f)}
    for f in constants:
        assert all(g in rank_two for g in neighbors[f])
    # Verify the full positive-spectrum identity via traces of BB^T.
    vertex_list = [tuple([z]*n) for z in range(n)]
    BBT = [[sum(1 for f in rank_two if vertex_list[i] in neighbors[f]
                     and vertex_list[j] in neighbors[f]) for j in range(n)] for i in range(n)]
    def mm(A, B):
        return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    P = [[int(i == j) for j in range(n)] for i in range(n)]
    for k in range(1, n + 1):
        P = mm(P, BBT)
        observed = sum(P[i][i] for i in range(n))
        predicted = (n*t)**k + (u-1)*(v*t)**k + (v-1)*(u*t)**k
        assert observed == predicted
    return n, u, v, len(idem), edges


total = 0
for n in range(2, 7):
    for u in range(1, n):
        v = n-u
        examples = [tuple([0]*u+[1]*v)]
        if n > 2:
            # Same fiber sizes, but a different output choice and placement.
            examples.append(tuple([n-1]*u+[0]*v)[::-1])
        for a in examples:
            ans = check(a)
            total += 1
            print('PASS n=%d fibers=(%d,%d) idempotents=%d edges=%d' % ans)
print('PASS total configurations=%d' % total)
