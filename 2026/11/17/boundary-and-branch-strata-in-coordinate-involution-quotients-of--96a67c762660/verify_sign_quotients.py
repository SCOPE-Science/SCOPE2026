#!/usr/bin/env python3
"""Independent cubical orbit-cell checks for polygonal real moment-angle surfaces.

Use the cubical subdivision of every coordinate interval at zero.  Cells are
encoded by -1, 0, 1 (vertices) and -2, 2 (left/right unit intervals).
"""
from itertools import product, combinations
from collections import Counter


def admissible(t):
    n = len(t)
    active = [i for i, a in enumerate(t) if a in (0, -2, 2)]
    return len(active) <= 1 or (len(active) == 2 and (active[0] - active[1]) % n in (1, n-1))


def cells(n):
    out = [[], [], []]
    for t in product((-2, -1, 0, 1, 2), repeat=n):
        d = sum(abs(x) == 2 for x in t)
        if d <= 2 and admissible(t):
            out[d].append(t)
    return out


def fixed_counts(cell_by_dimension, mask):
    # A subdivided cell is invariant under the sign flip exactly when all
    # flipped coordinates are the 0 vertex. It is then fixed pointwise.
    return [sum(all(t[i] == 0 for i in mask) for t in dim) for dim in cell_by_dimension]


def chi(counts):
    return counts[0] - counts[1] + counts[2]


def components_fixed(cell_by_dimension, mask):
    # Fixed subcomplex is either empty, circles, or isolated points.
    vertices = [t for t in cell_by_dimension[0] if all(t[i] == 0 for i in mask)]
    edges = [t for t in cell_by_dimension[1] if all(t[i] == 0 for i in mask)]
    parent = {t: t for t in vertices}
    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for e in edges:
        i = next(j for j, x in enumerate(e) if abs(x) == 2)
        a, b = list(e), list(e)
        if e[i] == -2:
            a[i], b[i] = -1, 0
        else:
            a[i], b[i] = 0, 1
        a, b = tuple(a), tuple(b)
        ra, rb = root(a), root(b)
        parent[rb] = ra
    return len({root(v) for v in vertices}), len(vertices), len(edges)


def expected(n, mask):
    s = len(mask)
    g = 1 + (n-4)*2**(n-3)
    if s == 1:
        return ('bordered_orientable', 1+(n-5)*2**(n-4), 2**(n-3))
    if s == 2 and (mask[0]-mask[1]) % n in (1, n-1):
        return ('closed_orientable_branched', 1+(n-5)*2**(n-4), 2**(n-2))
    if s % 2:
        return ('closed_nonorientable_free', g+1, 0)
    return ('closed_orientable_free', 1+(n-4)*2**(n-4), 0)


def run():
    total = 0
    for n in range(3, 8):
        cb = cells(n)
        chi_m = chi([len(x) for x in cb])
        assert chi_m == (4-n)*2**(n-2)
        classcounts = Counter()
        for k in range(1, n+1):
            for mask in combinations(range(n), k):
                total += 1
                typ, param, other = expected(n, mask)
                f = fixed_counts(cb, mask)
                chi_f = chi(f)
                assert all((len(cb[d])+f[d])%2 == 0 for d in range(3))
                qcounts = [(len(cb[d])+f[d])//2 for d in range(3)]
                chi_q = chi(qcounts)
                assert 2*chi_q == chi_m+chi_f
                if typ == 'bordered_orientable':
                    assert chi_f == 0
                    assert chi_q == 2 - 2*param - other
                    b, v, e = components_fixed(cb, mask)
                    assert b == other and v == e
                elif typ == 'closed_orientable_branched':
                    assert chi_f == other
                    assert f[1] == f[2] == 0
                    b, v, e = components_fixed(cb, mask)
                    assert b == other and e == 0 and v == other
                    assert chi_q == 2-2*param
                elif typ == 'closed_orientable_free':
                    assert f == [0, 0, 0]
                    assert chi_q == 2-2*param
                else:
                    assert f == [0, 0, 0]
                    assert chi_q == 2-param
                classcounts[typ] += 1
        print(f'n={n} dimensions={[len(v) for v in cb]} chi={chi_m} involutions={2**n-1} classes={dict(sorted(classcounts.items()))}')
    print(f'POLYGON_MOMENT_ANGLE_ALL_SIGN_INVOLUTIONS_PASS cases={total}')

if __name__ == '__main__':
    run()
