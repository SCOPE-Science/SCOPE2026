"""Reproducibility checker for exact facet areas of linked symmetric-snake polytopes.

Requires Python 3.10+; NumPy and SciPy for an independent convex-hull test.
The combinatorial counts use only the Python standard library.
"""
import itertools
import math
from functools import lru_cache


def extensions(pred):
    n = len(pred)

    @lru_cache(None)
    def rec(mask):
        if mask == (1 << n) - 1:
            return 1
        ans = 0
        for i in range(n):
            if not (mask >> i) & 1 and pred[i] & mask == pred[i]:
                ans += rec(mask | (1 << i))
        return ans

    return rec(0)


def path_predecessors(n, bits):
    pred = [0] * n
    for i in range(n - 1):
        if bits >> i & 1:
            pred[i + 1] |= 1 << i
        else:
            pred[i] |= 1 << (i + 1)
    return pred


def delete_vertex(pred, i):
    keep = [j for j in range(len(pred)) if j != i]
    return [sum(1 << k for k, j in enumerate(keep) if pred[v] >> j & 1)
            for v in keep]


def contract_edge(pred, i):
    n = len(pred)
    groups = [[j] for j in range(n) if j not in (i, i + 1)] + [[i, i + 1]]
    groups.sort(key=lambda group: min(group))
    out = []
    for k, group in enumerate(groups):
        q = 0
        for a in group:
            for j, other in enumerate(groups):
                if j != k and any(pred[a] >> b & 1 for b in other):
                    q |= 1 << j
        out.append(q)
    return out


def exact_extension_formula(n, bits):
    pred = path_predecessors(n, bits)
    n_ext = extensions(pred)
    edge_counts = [extensions(contract_edge(pred, i)) for i in range(n - 1)]
    mins = {i for i in range(n) if pred[i] == 0}
    maxs = {i for i in range(n) if not any(p >> i & 1 for p in pred)}
    boundary = [(i, extensions(delete_vertex(pred, i))) for i in sorted(mins | maxs)]
    area = (sum(edge_counts) + sum(math.sqrt(n - i) * e for i, e in boundary)) / math.factorial(n - 1)
    return n_ext / math.factorial(n), area, edge_counts, boundary


def actual_vertices(n, bits):
    for yy in itertools.product((0, 1), repeat=n):
        if all((yy[i] <= yy[i + 1] if bits >> i & 1 else yy[i] >= yy[i + 1])
               for i in range(n - 1)):
            yield [(int(bool(bits >> i & 1)) + yy[i] - yy[i + 1])
                   for i in range(n - 1)] + [yy[-1]]


def mirror_formula(n):
    low = 1 + (n - 2)**2 + math.sqrt(n) + (n - 1) * math.sqrt(n - 1) + n - 2
    high = 1 + (n - 2)**2 + (n - 2) * math.sqrt(n) + (n - 1) * math.sqrt(2) + 1
    delta = (n - 3) * (math.sqrt(n) - 1) - (n - 1) * (math.sqrt(n - 1) - math.sqrt(2))
    return low / math.factorial(n - 1), high / math.factorial(n - 1), delta / math.factorial(n - 1)


def main():
    from scipy.spatial import ConvexHull
    import numpy as np

    total = 0
    for n in range(3, 8):
        for bits in range(1 << (n - 1)):
            vol, area, _, _ = exact_extension_formula(n, bits)
            hull = ConvexHull(np.asarray(list(actual_vertices(n, bits)), dtype=float))
            assert abs(hull.volume - vol) < 1e-6, (n, bits, hull.volume, vol)
            assert abs(hull.area - area) < 1e-6, (n, bits, hull.area, area)
            total += 1
    assert total == 124
    for n in range(3, 13):
        a, b, gap = mirror_formula(n)
        va, aa, _, _ = exact_extension_formula(n, 1)
        vb, ab, _, _ = exact_extension_formula(n, 1 << (n - 2))
        assert va == vb == (n - 1) / math.factorial(n)
        assert abs(a - aa) < 1e-10 and abs(b - ab) < 1e-10
        assert abs((ab - aa) - gap) < 1e-10
        assert (gap == 0 if n == 3 else gap > 0)
    print('SNAKE_FACET_AREA_PASS: 124 hull profiles and ten exact mirrored pairs')


if __name__ == '__main__':
    main()
