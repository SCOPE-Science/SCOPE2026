"""Exact finite checks of triangle / induced four-cycle moments in G(n,p).

Requires only the Python standard library. Does not replace the all-n proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, sqrt


def edges(n):
    return tuple(combinations(range(n), 2))


def motifs(n, mask):
    E = edges(n)
    state = {e: (mask >> i) & 1 for i, e in enumerate(E)}
    triangles = sum(all(state[e] for e in combinations(s, 2))
                    for s in combinations(range(n), 3))
    squares = 0
    for s in combinations(range(n), 4):
        if sum(state[e] for e in combinations(s, 2)) != 4:
            continue
        if all(sum(state[tuple(sorted((u, v)))] for v in s if v != u) == 2
               for u in s):
            squares += 1
    return triangles, squares


def enumerated_moments(n, p):
    m = comb(n, 2)
    ET = EH = ET2 = EH2 = ETH = Q(0)
    for mask in range(1 << m):
        k = mask.bit_count()
        weight = p ** k * (1 - p) ** (m - k)
        t, h = motifs(n, mask)
        ET += weight * t
        EH += weight * h
        ET2 += weight * t * t
        EH2 += weight * h * h
        ETH += weight * t * h
    return ET2 - ET * ET, EH2 - EH * EH, ETH - ET * EH


def exact_covariance(n, p):
    q = 1 - p
    return 3 * comb(n, 3) * (n - 3) * p ** 6 * q ** 2 * (
        (n - 4) - Q(3 * n - 10, 2) * p)


def exact_triangle_variance(n, p):
    q = 1 - p
    return (comb(n, 2) * (n - 2) ** 2 * p ** 5 * q
            + n * comb(n - 1, 2) * p ** 4 * q ** 2
            + comb(n, 3) * p ** 3 * q ** 3)


def exact_square_variance(n, p):
    q = 1 - p
    h = 3 * p ** 4 * q ** 2
    a = p ** 7 * q ** 3 * (2 - 3 * p) ** 2
    b = 3 * p ** 6 * q ** 4 * (1 - 3 * p) ** 2 + 9 * p ** 7 * q ** 5
    c = h * (1 - h) - 6 * a - 4 * b
    return (comb(n, 2) * comb(n - 2, 2) ** 2 * a
            + comb(n, 3) * (n - 3) ** 2 * b
            + comb(n, 4) * c)


def local_walsh_support_variance(p):
    """Independently obtain four-vertex Walsh variances by 64-state sums."""
    E = edges(4)
    result = {2: Q(0), 3: Q(0), 4: Q(0)}
    for S in range(1, 1 << 6):
        k = S.bit_count()
        coefficient = Q(0)
        for mask in range(1 << 6):
            present = mask.bit_count()
            weight = p ** present * (1 - p) ** (6 - present)
            _, square = motifs(4, mask)
            product = Q(1)
            for e in range(6):
                if S & (1 << e):
                    product *= Q((mask >> e) & 1) - p
            coefficient += weight * square * product
        coefficient /= (p * (1 - p)) ** k
        support = {u for e, uv in enumerate(E) if S & (1 << e) for u in uv}
        size = len(support)
        result[size] += coefficient ** 2 * (p * (1 - p)) ** k / comb(4, size)
    return result


def check():
    checks = 0
    for n in (4, 5, 6):
        for p in (Q(1, 3), Q(2, 3), Q(4, 5)):
            a, b, c = enumerated_moments(n, p)
            assert a == exact_triangle_variance(n, p)
            assert b == exact_square_variance(n, p)
            assert c == exact_covariance(n, p)
            checks += 3
    for p in (Q(1, 3), Q(2, 3), Q(4, 5)):
        groups = local_walsh_support_variance(p)
        q = 1 - p
        g2 = p ** 7 * q ** 3 * (2 - 3 * p) ** 2
        g3 = 3 * p ** 6 * q ** 4 * (1 - 3 * p) ** 2 + 9 * p ** 7 * q ** 5
        h = 3 * p ** 4 * q ** 2
        g4 = h * (1 - h) - 6 * g2 - 4 * g3
        assert groups == {2: g2, 3: g3, 4: g4}
        checks += 1
    assert local_walsh_support_variance(Q(2, 3)) == {
        2: Q(0), 3: Q(320, 59049), 4: Q(784, 19683)}
    checks += 1
    for n in (5, 10, 100):
        root = Q(2 * (n - 4), 3 * n - 10)
        for p in (root / 2, root, (root + 1) / 2):
            c = exact_covariance(n, p)
            assert (c > 0 if p < root else c == 0 if p == root else c < 0)
            checks += 1
    # Numerical convergence is only a diagnostic, not proof of the limit.
    for lam in (-2, -1, 0, 1, 2):
        n = 10000
        p = Q(2, 3) + Q(lam, 100)
        corr = (float(exact_covariance(n, p)) /
                sqrt(float(exact_triangle_variance(n, p)) *
                     float(exact_square_variance(n, p))))
        limit = -lam / sqrt(lam * lam + 10 / 27)
        assert abs(corr - limit) < 0.01
        checks += 1
    print(f"PASS: {checks} checks; complete labeled-graph enumeration through n=6.")


if __name__ == '__main__':
    check()
