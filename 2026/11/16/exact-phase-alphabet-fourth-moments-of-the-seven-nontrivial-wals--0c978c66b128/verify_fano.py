#!/usr/bin/env python3
"""Exact reproducibility certificate for seven-character Walsh fourth moments.

Standard-library Python only. All minimizations, comparisons, and orbit
certificates are integral (including the quadratic field Q(sqrt(5))).
"""
from itertools import product
from collections import Counter

SUPPORT = tuple(range(1, 8))
PAIRS = {
    h: tuple((j, j ^ h) for j in SUPPORT if j < (j ^ h) and (j ^ h) != 0)
    for h in SUPPORT
}
assert all(len(PAIRS[h]) == 3 for h in SUPPORT)
assert sorted((j, k) for h in SUPPORT for j, k in PAIRS[h]) == [
    (j, k) for j in SUPPORT for k in SUPPORT if j < k
]
# Entries are exactly 2*cos(2*pi*k/q), not numerical approximations.
INTEGER_COSINE = {
    2: (2, -2),
    3: (2, -1, -1),
    4: (2, 0, -2, 0),
    6: (2, 1, -1, -2, -1, 1),
}
# q=5 values (A+B*sqrt(5))/2; indices are modulo five.
FIFTH_COSINE = ((4, 0), (-1, 1), (-1, -1), (-1, -1), (-1, 1))
EXPECTED = {
    2: (109, 56, (7, 21, 28)),
    3: (67, 168, (84, 84)),
    4: (61, 224, (28, 28, 84, 84)),
    5: ((264, -12), 336, (168, 168)),  # (A+B sqrt(5))/4
    6: (61, 2688, (168,) * 16),
}


def sgn(x):
    return (x > 0) - (x < 0)


def compare_quadratic(a, b):
    """Order (A+B*sqrt(5))/4 exactly, without floating point."""
    A, B = a[0] - b[0], a[1] - b[1]
    if B == 0:
        return sgn(A)
    if A == 0:
        return sgn(B)
    if A * B > 0:
        return sgn(A)
    # Equal squares cannot occur for nonzero integers A and B.
    D = A * A - 5 * B * B
    assert D != 0
    return sgn(D) if A > 0 else -sgn(D)


def moment(seq, q):
    a = (0, 0) + tuple(seq)  # a[0] unused; a[1]=1 as gauge
    if q == 5:
        pairs = []
        for h in SUPPORT:
            A = B = 0
            for j, k in PAIRS[h]:
                x, y = FIFTH_COSINE[(a[j] - a[k]) % 5]
                A += x
                B += y
            pairs.append((A, B))
        return (196 + sum(A * A + 5 * B * B for A, B in pairs),
                sum(2 * A * B for A, B in pairs))
    values = INTEGER_COSINE[q]
    return 49 + sum(
        sum(values[(a[j] - a[k]) % q] for j, k in PAIRS[h]) ** 2
        for h in SUPPORT
    )


def less(a, b, q):
    return compare_quadratic(a, b) < 0 if q == 5 else a < b


def linear_maps():
    """Exactly 168 invertible F_2-linear maps on three coordinates."""
    result = []
    for u, v, w in product(SUPPORT, repeat=3):
        image = tuple((u if j & 1 else 0) ^
                      (v if j & 2 else 0) ^
                      (w if j & 4 else 0) for j in range(8))
        if len(set(image)) == 8:
            result.append(image)
    assert len(result) == 168 and len(set(result)) == 168
    return tuple(result)


def relabel(seq, q, image):
    a = (0, 0) + tuple(seq)
    b = [0] * 8
    for j in SUPPORT:
        b[image[j]] = a[j]
    return tuple((b[j] - b[1]) % q for j in range(2, 8))


def orbit_census(minima, q, maps):
    todo = set(minima)
    sizes = []
    representatives = []
    while todo:
        rep = min(todo)
        orbit = {relabel(rep, q, m) for m in maps}
        assert orbit <= todo, 'Moment must be invariant under GL(3,2)'
        assert 168 % len(orbit) == 0
        todo.difference_update(orbit)
        sizes.append(len(orbit))
        representatives.append((len(orbit), rep))
    return tuple(sorted(sizes)), tuple(representatives)


def direct_walsh_moment(seq, q):
    """Independent exact transform-side fourth moment for one coefficient array.

    Return either an integer or (A,B), representing (A+B*sqrt(5))/4.
    """
    a = (0, 0) + tuple(seq)
    if q == 5:
        total_A = total_B = 0
        for x in range(8):
            E, F = 14, 0
            for j in SUPPORT:
                for k in range(j + 1, 8):
                    sign = -1 if ((j ^ k) & x).bit_count() & 1 else 1
                    u, v = FIFTH_COSINE[(a[j] - a[k]) % 5]
                    E += sign * u
                    F += sign * v
            total_A += E * E + 5 * F * F
            total_B += 2 * E * F
        # E_x |P(x)|^4=(total_A+total_B sqrt5)/32.
        assert total_A % 8 == 0 and total_B % 8 == 0
        return (total_A // 8, total_B // 8)
    c = INTEGER_COSINE[q]
    total = 0
    for x in range(8):
        E = 7
        for j in SUPPORT:
            for k in range(j + 1, 8):
                sign = -1 if ((j ^ k) & x).bit_count() & 1 else 1
                E += sign * c[(a[j] - a[k]) % q]
        total += E * E
    assert total % 8 == 0
    return total // 8


def run():
    maps = linear_maps()
    total = 0
    for q in (2, 3, 4, 5, 6):
        best = None
        minimizers = []
        n = 0
        for seq in product(range(q), repeat=6):
            n += 1
            m = moment(seq, q)
            if best is None or less(m, best, q):
                best = m
                minimizers = [seq]
            elif m == best:
                minimizers.append(seq)
        expect_best, expect_count, expect_sizes = EXPECTED[q]
        assert n == q ** 6
        assert best == expect_best, (q, best)
        assert len(minimizers) == expect_count
        sizes, reps = orbit_census(minimizers, q, maps)
        assert sizes == expect_sizes, (q, sizes)
        for seq in minimizers:
            assert direct_walsh_moment(seq, q) == moment(seq, q)
        # Separately verify exact first representative, even for non-minimal alphabets.
        seq = tuple((j*j+1) % q for j in range(2, 8))
        assert direct_walsh_moment(seq, q) == moment(seq, q)
        total += n
        print(f'q={q} cases={n} minimum={best} normalized_minimizers={len(minimizers)}'
              f' orbit_sizes={sizes} representatives={reps}')
    assert total == 67170
    print('PASS: 67,170 exact exhaustive phase tests; 3,472 exact independent'
          ' Walsh-transform minimizer checks; five complete orbit partitions.')


if __name__ == '__main__':
    run()
