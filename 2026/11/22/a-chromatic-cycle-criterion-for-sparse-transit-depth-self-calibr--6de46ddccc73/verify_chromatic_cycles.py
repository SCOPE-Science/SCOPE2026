"""Exact rational checks for a sparse chromatic transit-depth theorem.

Standalone: Python 3 standard library only. These finite tests supplement,
but never replace, the exact symbolic proof.
"""
from fractions import Fraction as F
from random import Random


def observations(edges, cover, depth, contrast):
    return {(e, b): (1 - contrast[b] * cover[e]) / depth[b]
            for e, b in edges}


def recover_affine(edges, n_epochs, n_bands, contrast, q):
    """Return (root_value, recoverable, affine epoch/planet maps).

    Graph must be connected. Each epoch fraction and each band depth
    is propagated as a pair (slope, intercept) in the root epoch fraction.
    """
    nodes = [('e', i) for i in range(n_epochs)] + [('b', j) for j in range(n_bands)]
    adjacent = {v: [] for v in nodes}
    for e, b in edges:
        adjacent[('e', e)].append(('b', b))
        adjacent[('b', b)].append(('e', e))
    affine = {('e', 0): (F(1), F(0))}
    pending = [('e', 0)]
    for v in pending:
        s, t = affine[v]
        for w in adjacent[v]:
            e, b = (v[1], w[1]) if v[0] == 'e' else (w[1], v[1])
            if w not in affine:
                if v[0] == 'e':
                    affine[w] = (-contrast[b] * s / q[e, b],
                                 (1 - contrast[b] * t) / q[e, b])
                else:
                    affine[w] = (-q[e, b] * s / contrast[b],
                                 (1 - q[e, b] * t) / contrast[b])
                pending.append(w)
    assert len(affine) == len(nodes)
    roots = set()
    for e, b in edges:
        a, k = affine['e', e]
        s, t = affine['b', b]
        coeff = q[e, b] * s + contrast[b] * a
        offset = q[e, b] * t + contrast[b] * k - 1
        if coeff:
            roots.add(-offset / coeff)
        else:
            assert offset == 0
    assert len(roots) <= 1
    return (next(iter(roots)) if roots else None, bool(roots), affine)


def check(condition, counter):
    assert condition
    counter[0] += 1


def main():
    tests = [0]
    c = [F(1, 4), F(3, 4)]
    f = [F(1, 5), F(2, 5)]
    d = [F(1, 50), F(1, 40)]
    ed = [(0, 0), (1, 0), (0, 1), (1, 1)]
    q = observations(ed, f, d, c)
    check(q[0, 0] == F(95, 2), tests)
    check(q[1, 0] == F(45), tests)
    check(q[0, 1] == F(34), tests)
    check(q[1, 1] == F(28), tests)
    H = (q[1, 0] / q[0, 0]) * (q[0, 1] / q[1, 1])
    check(H == F(153, 133), tests)
    root, identifiable, amap = recover_affine(ed, 2, 2, c, q)
    check(identifiable and root == f[0], tests)
    for e in range(2):
        a, b = amap['e', e]
        check(a * root + b == f[e], tests)
    for j in range(2):
        a, b = amap['b', j]
        check(a * root + b == d[j], tests)
    rng = Random(118035)
    for m in range(2, 8):
        for n in range(2, 7):
            contrast = [F(j + 1, n + 2) for j in range(n)]
            edges = [(0, 0), (0, 1), (1, 0), (1, 1)]
            edges.extend((e, 0) for e in range(2, m))
            edges.extend((0, j) for j in range(2, n))
            check(len(edges) == m + n, tests)
            for _ in range(100):
                cover = [F(rng.randint(1, 79), 100) for e in range(m)]
                if cover[0] == cover[1]:
                    continue
                depths = [F(rng.randint(1, 15), 100) for j in range(n)]
                q = observations(edges, cover, depths, contrast)
                root, identifiable, amap = recover_affine(edges, m, n, contrast, q)
                check(identifiable and root == cover[0], tests)
                for e in range(m):
                    a, b = amap['e', e]
                    check(a * root + b == cover[e], tests)
                for j in range(n):
                    a, b = amap['b', j]
                    check(a * root + b == depths[j], tests)
                # Delete one cycle edge: a spanning tree cannot identify.
                tree = edges[:-1] if edges[-1] == (1, 1) else [x for x in edges if x != (1, 1)]
                qtree = observations(tree, cover, depths, contrast)
                _, unique, _ = recover_affine(tree, m, n, contrast, qtree)
                check(not unique, tests)
    for _ in range(300):
        # Even a full K2,2 is ambiguous when contrasts are equal.
        contrast = [F(2, 5), F(2, 5)]
        cover = [F(rng.randint(1, 80), 100) for _ in range(2)]
        depths = [F(rng.randint(1, 10), 100) for _ in range(2)]
        q = observations(ed, cover, depths, contrast)
        root, identifiable, _ = recover_affine(ed, 2, 2, contrast, q)
        check(root is None and not identifiable, tests)
        # A small exact gauge perturbation stays in the physical domain.
        a = F(1001, 1000)
        f2 = [(1 - a) / contrast[0] + a * x for x in cover]
        d2 = [a * x for x in depths]
        check(all(0 < x < 1 for x in f2), tests)
        check(observations(ed, f2, d2, contrast) == q, tests)
    print('PASS:', tests[0], 'exact-rational assertions; illustrative numerical checks only')


if __name__ == '__main__':
    main()
