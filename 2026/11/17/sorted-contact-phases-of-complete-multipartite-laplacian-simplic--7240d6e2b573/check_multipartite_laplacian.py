"""Exact finite checks for minimum enclosing balls of complete multipartite Laplacian simplices."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from random import Random


def evaluated_formula(part_sizes):
    a = tuple(sorted(part_sizes))
    n = sum(a)
    b = tuple((n - q) * (n - q + 1) for q in a)
    threshold = tuple(v + 2 * n for v in b)
    m = None
    positive = None
    for k in range(1, len(a) + 1):
        candidate = F(sum(a[i] * threshold[i] for i in range(k)) - 2 * n * n,
                      sum(a[:k]))
        if all(threshold[i] > candidate for i in range(k)) and all(
                threshold[i] <= candidate for i in range(k, len(a))):
            m, positive = candidate, k
            break
    assert m is not None
    c = tuple(max(F(-1), (F(bi) - m) / (2 * n)) for bi in b)
    radius_sq = m + sum(a[i] * c[i] ** 2 for i in range(len(a)))
    return a, b, threshold, m, c, radius_sq, positive


def inspect(part_sizes):
    a, b, threshold, m, c, radius_sq, positive = evaluated_formula(part_sizes)
    n = sum(a)
    assert sum(q * t for q, t in zip(a, c)) == 0
    assert sum(q * max(F(0), F(t) - m) for q, t in zip(a, threshold)) == 2 * n * n
    vertex_class = [i for i, sz in enumerate(a) for _ in range(sz)]
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u == v:
                L[u][v] = n - a[vertex_class[u]]
            elif vertex_class[u] != vertex_class[v]:
                L[u][v] = -1
    center = [c[i] for i in vertex_class]
    w = [F(1 + c[i], n) for i in vertex_class]
    assert all(x >= 0 for x in w) and sum(w) == 1
    assert [sum(w[v] * L[u][v] for v in range(n)) for u in range(n)] == center
    distances = [sum((L[u][v] - center[u])**2 for u in range(n)) for v in range(n)]
    for v in range(n):
        i = vertex_class[v]
        expected = radius_sq if threshold[i] >= m else radius_sq - (m - threshold[i])
        assert distances[v] == expected and distances[v] <= radius_sq
        if w[v] > 0: assert distances[v] == radius_sq
    assert max(distances) == radius_sq
    return positive, tuple(i for i in range(len(a)) if threshold[i] >= m)


def run():
    exact = 0
    levels = set()
    boundary = 0
    for r in range(2, 6):
        for parts in combinations_with_replacement(range(1, 7), r):
            if sum(parts) > 16: continue
            k, contact = inspect(parts)
            exact += 1
            levels.add((r, k))
            if len(contact) > k: boundary += 1
    rng = Random(1775)
    large = 0
    for _ in range(50):
        r = rng.randint(2, 6)
        parts = [rng.randint(1, 9) for _ in range(r)]
        inspect(parts)
        large += 1
    for case in [(12, 13, 13), (2, 8, 28), (4, 17, 17), (3, 3, 6)]:
        k, _ = inspect(case)
        levels.add((3, k))
    assert (3, 1) in levels and (3, 2) in levels and (3, 3) in levels
    assert boundary > 0
    print(f'MULTIPARTITE_LAPLACIAN_BALL_PASS exact_profiles={exact} large_profiles={large} distinct_active_levels={len(levels)} boundary_profiles={boundary}')


if __name__ == '__main__':
    run()
