"""Independent finite-field direct Fourier checks for three-line projection norms.

Run with Python 3 (standard library only): python3 checker.py
This tests finite examples; the arbitrary-prime-power proof is in RESULT.md.
"""
import cmath
import itertools
import math


def field(p, m):
    moduli = {(2, 2): (1, 1, 1), (2, 3): (1, 1, 0, 1),
              (3, 2): (1, 0, 1), (5, 2): (2, 0, 1)}
    elems = list(itertools.product(range(p), repeat=m))
    zero = (0,) * m
    one = (1,) + (0,) * (m - 1)
    poly = moduli.get((p, m))

    def add(a, b):
        return tuple((x + y) % p for x, y in zip(a, b))

    def mul(a, b):
        product = [0] * (2 * m - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                product[i + j] = (product[i + j] + x * y) % p
        if m > 1:
            for j in range(2 * m - 2, m - 1, -1):
                v = product[j]
                for k in range(m):
                    product[j - m + k] = (product[j - m + k] - v * poly[k]) % p
        return tuple(product[:m])

    def power(a, n):
        product, base = one, a
        while n:
            if n & 1:
                product = mul(product, base)
            base = mul(base, base)
            n //= 2
        return product

    def trace(a):
        value, term = zero, a
        for _ in range(m):
            value = add(value, term)
            term = power(term, p)
        assert value[1:] == zero[1:]
        return value[0]

    return elems, zero, one, add, mul, trace


def predicted(p, q):
    z = cmath.exp(2j * math.pi / p)
    R = sum(abs(1 + z**a + z**b) for a in range(p) for b in range(p))
    T = sum(abs(2 + z**a) for a in range(p))
    U = sum(abs(q - 2 - z**a) for a in range(p))
    triangular = ((q / p)**2 * R + 3 * (q / p) * (U - T) + 12) / q**2
    if q == 2:
        triangular = 1.5
    pencil = 5 - 12/q + 8/q**2
    if p == 2:
        assert math.isclose(triangular, 4.5 - 12/q + 12/q**2,
                            abs_tol=1e-10)
    return pencil, triangular


def direct_norm(S, elements, add, mul, trace, p):
    q = len(elements)
    phase = [cmath.exp(2j * math.pi * j/p) for j in range(p)]
    return sum(abs(sum(phase[trace(add(mul(u, x), mul(v, y)))]
                       for (x, y) in S))
               for u in elements for v in elements) / q**2


def canonical_checks(p, m):
    es, zero, one, add, mul, trace = field(p, m)
    q = len(es)
    pencil = {(x, y) for x in es for y in es
              if x == zero or y == zero or add(x, y) == zero}
    triangle = {(x, y) for x in es for y in es
                if x == zero or y == zero or add(x, y) == one}
    norm_pencil, norm_triangle = predicted(p, q)
    for support, expected in [(pencil, norm_pencil),
                              (triangle, norm_triangle)]:
        observed = direct_norm(support, es, add, mul, trace, p)
        assert math.isclose(observed, expected, abs_tol=2e-9), (p, m, observed, expected)
    if q == 2:
        assert norm_pencil < norm_triangle
    else:
        assert norm_triangle < norm_pencil
    print('canonical GF(%d): pencil %.12f triangle %.12f' %
          (q, norm_pencil, norm_triangle))


def all_arrangements(p, m):
    es, zero, one, add, mul, trace = field(p, m)
    q = len(es)
    points = list(itertools.product(es, repeat=2))
    directions = [(one, slope) for slope in es] + [(zero, one)]
    signs = {}
    for normal in directions:
        for offset in es:
            signs[normal, offset] = {point for point in points
                    if add(mul(normal[0], point[0]),
                           mul(normal[1], point[1])) == offset}
    expected = predicted(p, q)
    count = 0
    for normals in itertools.combinations(directions, 3):
        for offsets in itertools.product(es, repeat=3):
            lines = [signs[norm, offset]
                     for norm, offset in zip(normals, offsets)]
            intersections = lines[0] & lines[1]
            assert len(intersections) == 1
            concurrent = bool(intersections & lines[2])
            S = set().union(*lines)
            observed = direct_norm(S, es, add, mul, trace, p)
            target = expected[0 if concurrent else 1]
            assert math.isclose(observed, target, abs_tol=3e-9), (p, m, normals, offsets, concurrent, observed, target)
            count += 1
    print('all-arrangements GF(%d): %d direct Fourier comparisons' % (q, count))


if __name__ == '__main__':
    for p, m in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2),(7,1),(11,1)]:
        canonical_checks(p, m)
    for p, m in [(2,1),(3,1),(2,2),(5,1)]:
        all_arrangements(p, m)
    print('all direct comparisons passed')
