#!/usr/bin/env python3
"""Exact F_3 arithmetic census for rational line sections of a nodal quartic.

Python standard library only. Run: python3 verify_bks.py
Each field is represented independently with two monic irreducible moduli.
"""
from collections import Counter
from itertools import combinations

MODULI = {
    3: [(1, 2, 0, 1), (2, 2, 0, 1)],
    4: [(2, 1, 0, 0, 1), (2, 2, 0, 0, 1)],
}
EXPECTED = {
    3: {
        'curve': 31,
        'lines': {0: 240, 1: 256, 2: 195, 3: 42, 4: 24},
        'on': {0: 7, 4: 24},
        'off': {0: 282, 1: 312, 2: 132},
    },
    4: {
        'curve': 79,
        'lines': {0: 2520, 1: 2290, 2: 1515, 3: 114, 4: 204},
        'on': {0: 3, 10: 72, 24: 4},
        'off': {0: 108, 1: 1332, 2: 2496, 3: 1248, 4: 1134, 5: 240, 18: 6},
    },
}


def build_field(mod):
    """A table realization of F_3[t]/(mod); arithmetic is exact mod 3."""
    m = len(mod) - 1
    n = 3 ** m
    # Direct irreducibility certificate. A monic cubic is irreducible iff
    # it has no F_3 root; for a quartic also rule out each irreducible
    # monic quadratic over F_3. This test does not assume field axioms.
    assert all(sum(mod[i] * a ** i for i in range(m + 1)) % 3
               for a in range(3))
    if m == 4:
        def remainder(poly, divisor):
            p = list(poly)
            for k in range(len(p) - 1, len(divisor) - 2, -1):
                coefficient = p[k]
                for j, coeff in enumerate(divisor):
                    p[k - len(divisor) + 1 + j] = (
                        p[k - len(divisor) + 1 + j] - coefficient * coeff) % 3
            return p[:len(divisor) - 1]
        assert all(any(remainder(mod, quad)) for quad in
                   ((1, 0, 1), (2, 1, 1), (2, 2, 1)))
    dig = [[(a // 3 ** j) % 3 for j in range(m)] for a in range(n)]

    def encode(c):
        return sum((a % 3) * 3 ** i for i, a in enumerate(c))

    add = [[encode([dig[a][j] + dig[b][j] for j in range(m)])
            for b in range(n)] for a in range(n)]
    mul = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            c = [0] * (2 * m - 1)
            for i in range(m):
                for j in range(m):
                    c[i + j] = (c[i + j] + dig[a][i] * dig[b][j]) % 3
            for k in range(2 * m - 2, m - 1, -1):
                top = c[k]
                for j in range(m):
                    c[k - m + j] = (c[k - m + j] - top * mod[j]) % 3
            mul[a][b] = encode(c[:m])
    neg = [encode([-a for a in dig[i]]) for i in range(n)]

    def power(a, k):
        r = 1
        while k:
            if k & 1:
                r = mul[r][a]
            a = mul[a][a]
            k //= 2
        return r

    inv = [None] + [power(a, n - 2) for a in range(1, n)]
    assert all(mul[a][inv[a]] == 1 for a in range(1, n))
    assert all(power(a, n - 1) == 1 for a in range(1, n))
    assert all(power(a, 3 ** m) == a for a in range(n))
    return n, add, mul, neg, power, inv


def census(m, mod):
    n, add, mul, neg, power, inv = build_field(mod)

    def plus(a, b):
        return add[a][b]

    def times(a, b):
        return mul[a][b]

    def normalize(v):
        a = next(a for a in v if a != 0)
        return tuple(times(x, inv[a]) for x in v)

    def dot(u, v):
        return plus(plus(times(u[0], v[0]), times(u[1], v[1])),
                    times(u[2], v[2]))

    def cross(u, v):
        return normalize((
            plus(times(u[1], v[2]), neg[times(u[2], v[1])]),
            plus(times(u[2], v[0]), neg[times(u[0], v[2])]),
            plus(times(u[0], v[1]), neg[times(u[1], v[0])]),
        ))

    # Unique representatives of all points AND dual lines of P^2(F_n).
    plane = [(1, a, b) for a in range(n) for b in range(n)]
    plane += [(0, 1, b) for b in range(n)] + [(0, 0, 1)]
    assert len(plane) == n * n + n + 1

    # Homogeneous BKS quartic for q=3:
    # 2 Y^4 - X^3 Z - X Z^3 - X Y^2 Z + X^2 Z^2.
    def f(P):
        x, y, z = P
        return plus(plus(plus(plus(
            times(2, power(y, 4)),
            neg[times(power(x, 3), z)]),
            neg[times(x, power(z, 3))]),
            neg[times(times(x, power(y, 2)), z)]),
            times(power(x, 2), power(z, 2)))

    curve = {P for P in plane if f(P) == 0}
    assert len(curve) == EXPECTED[m]['curve']

    # Independently parameterize the smooth normalization and identify
    # the 3 rational nodes (they are absent from its F_{27}-image).
    image = {normalize((
        times(2, power(plus(t, 1), 4)),
        plus(plus(2, t), power(t, 3)), 1)) for t in range(n)}
    image.add((1, 0, 0))
    assert image <= curve
    assert len(curve - image) == (3 if m % 2 else 0)
    nodes = {(1, 2, 1), (1, 0, 2), (1, 1, 1)}
    assert nodes <= curve
    assert ((curve - image) == nodes if m % 2 else nodes <= image)

    # Direct enumeration of all line intersection divisors.
    weights = {}
    for L in plane:
        weights[L] = sum(dot(L, P) == 0 for P in curve)
    spectrum_lines = dict(Counter(weights.values()))
    assert spectrum_lines == EXPECTED[m]['lines']
    secants = {L for L, weight in weights.items() if weight == 4}

    # Independent way to find every four-secant: span pairs on the curve.
    pair_lines = {cross(P, Q) for P, Q in combinations(sorted(curve), 2)}
    assert secants == {L for L in pair_lines if weights[L] == 4}
    assert all(weights[L] <= 4 for L in plane)

    # Every point is tested against every four-secant, including all
    # points outside the quartic, not just points on its normalization.
    multiplicity = {P: sum(dot(L, P) == 0 for L in secants) for P in plane}
    on = dict(Counter(multiplicity[P] for P in curve))
    off = dict(Counter(multiplicity[P] for P in set(plane) - curve))
    assert on == EXPECTED[m]['on']
    assert off == EXPECTED[m]['off']

    # Exact double incidence count, two independent totals.
    assert sum(k * v for k, v in spectrum_lines.items()) == len(curve) * (n + 1)
    assert sum(k * v for k, v in (Counter(multiplicity.values())).items()) == len(secants) * (n + 1)
    # All thirteen base-field points are tested separately; seven lie on
    # the quartic, including its three rational nodes.
    base = {P for P in plane if all(x in (0, 1, 2) for x in P)}
    assert len(base) == 13
    assert len(base & curve) == 7
    assert len(base - curve) == 6
    if m == 3:
        assert all(multiplicity[P] == 0 for P in base)
    else:
        assert {P for P in base if multiplicity[P] == 0} == nodes

    return (len(curve), tuple(sorted(spectrum_lines.items())),
            tuple(sorted(on.items())), tuple(sorted(off.items())))


def main():
    for m, moduli in MODULI.items():
        values = [census(m, mod) for mod in moduli]
        assert values[0] == values[1]
        print('degree', m, 'field_size', 3 ** m,
              'curve', values[0][0],
              'line_spectrum', values[0][1],
              'point_on', values[0][2],
              'point_off', values[0][3])
    print('BKS_SHORT_EXTENSION_COMPLETE_EXACT_CENSUS_PASS')


if __name__ == '__main__':
    main()
