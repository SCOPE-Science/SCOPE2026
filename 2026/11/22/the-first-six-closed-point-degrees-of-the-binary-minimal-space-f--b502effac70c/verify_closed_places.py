#!/usr/bin/env python3
"""Exact finite-field and symbolic checks for a fixed (3,4) space-filling curve.
Requires Python 3.9+ and SymPy for the four projective smoothness charts.
All public mathematics is over F_2; no external data or services are needed.
"""
from itertools import product
import sympy as S

# Each polynomial is a binary bit mask, bit j being the X^j coefficient.
IRRED = {1: 0b11, 2: 0b111, 3: 0b1011,
         4: 0b10011, 5: 0b100101, 6: 0b1000011}
AUT = (14, 3, 12, 11)  # Coordinate masks for (Y+Z+W, X+Y, Z+W, X+Y+W).


def polynomial_mod(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def field(n):
    modulus = IRRED[n]
    # A degree-n polynomial with no proper monic factor of degree <= floor(n/2).
    for d in range(1, n // 2 + 1):
        for lower in range(1, 1 << d, 2):
            assert polynomial_mod(modulus, (1 << d) | lower) != 0
    size = 1 << n
    multiplication = [[0] * size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            a, b, result = x, y, 0
            while b:
                if b & 1:
                    result ^= a
                b >>= 1
                a <<= 1
                if a & size:
                    a ^= modulus
            multiplication[x][y] = result
    return multiplication


def curve_points(n):
    m = 1 << n
    multiply = field(n)
    squares = [multiply[x][x] for x in range(m)]

    def phi(a, b):
        return multiply[squares[a]][b] ^ multiply[a][squares[b]]

    def on_curve(x, y, z, w):
        if phi(x, y) ^ phi(z, w):
            return False
        value = (multiply[x ^ z][phi(x, z)]
                 ^ multiply[y ^ z ^ w][phi(x, w)]
                 ^ multiply[x ^ y ^ z ^ w][phi(y, z)]
                 ^ multiply[z ^ w][phi(y, w)]
                 ^ multiply[y][phi(z, w)])
        return value == 0

    # Exactly one normalized representative of each projective point:
    # the first nonzero coordinate is 1.
    points = set()
    for first in range(4):
        for tail in product(range(m), repeat=3 - first):
            point = (0,) * first + (1,) + tail
            if on_curve(*point):
                points.add(point)
    return points, multiply


def normalized(point, multiply):
    lead = next(x for x in point if x)
    size = len(multiply)
    inverse = next(x for x in range(1, size) if multiply[x][lead] == 1)
    return tuple(multiply[x][inverse] for x in point)


def frob(point, multiply):
    return normalized(tuple(multiply[x][x] for x in point), multiply)


def auto(point, multiply):
    out = tuple(
        __import__('functools').reduce(int.__xor__,
            (point[j] for j in range(4) if row & (1 << j)), 0)
        for row in AUT)
    return normalized(out, multiply)


def places_of_exact_degree(n, smaller):
    pts, mult = curve_points(n)
    rest = pts - smaller
    places = set()
    while rest:
        p = min(rest)
        orbit = {p}
        v = frob(p, mult)
        while v not in orbit:
            orbit.add(v)
            v = frob(v, mult)
        assert len(orbit) == n
        assert orbit <= rest
        rest.difference_update(orbit)
        places.add(frozenset(orbit))
    return places, mult


def symbolic_checks():
    X, Y, Z, W = S.symbols('X Y Z W')
    variables = (X, Y, Z, W)
    phi = lambda a, b: a**2 * b + a * b**2
    G = phi(X, Y) + phi(Z, W)
    F = ((X+Z)*phi(X, Z) + (Y+Z+W)*phi(X, W)
         + (X+Y+Z+W)*phi(Y, Z) + (Z+W)*phi(Y, W)
         + Y*phi(Z, W))
    transformed = [sum(variables[j] for j in range(4) if AUT[i] & (1 << j))
                   for i in range(4)]
    assert S.Poly(S.expand(G.subs(dict(zip(variables, transformed)), simultaneous=True)-G),
                  *variables, modulus=2).is_zero
    assert S.Poly(S.expand(F.subs(dict(zip(variables, transformed)), simultaneous=True)-F-Z*G),
                  *variables, modulus=2).is_zero
    A = S.Matrix([[((row >> j) & 1) for j in range(4)] for row in AUT])
    assert all(int(z) % 2 == int(i == j)
               for i in range(4) for j, z in enumerate(list((A**5).row(i))))
    cp = S.Poly(A.charpoly().as_expr(), S.Symbol('lambda'), modulus=2)
    assert cp.all_coeffs() == [1,1,1,1,1]
    gradients = ([S.diff(G, x) for x in variables],
                 [S.diff(F, x) for x in variables])
    minors = [(gradients[0][i]*gradients[1][j] - gradients[0][j]*gradients[1][i])
              for i in range(4) for j in range(i+1,4)]
    for i in range(4):
        remaining = tuple(v for k, v in enumerate(variables) if k != i)
        equations = [S.Poly(S.expand(P.subs({variables[i]:1})),
                            *remaining, modulus=2).as_expr()
                     for P in (G,F,*minors)]
        gb = S.groebner(equations, *remaining, modulus=2, order='grevlex')
        assert len(gb.polys) == 1 and gb.polys[0].is_one
    print('SMOOTHNESS_AND_ORDER_FIVE_IDENTITIES_VERIFIED', flush=True)


def main():
    symbolic_checks()
    sets = {}
    for n in range(1, 7):
        sets[n], _ = curve_points(n)
    counts = tuple(len(sets[n]) for n in range(1, 7))
    assert counts == (15, 15, 15, 19, 50, 15), counts
    for n in (2, 3, 4, 5, 6):
        assert sets[1] <= sets[n]
    assert sets[2] == sets[1] and sets[3] == sets[1] and sets[6] == sets[1]
    degree4, m4 = places_of_exact_degree(4, sets[1])
    degree5, m5 = places_of_exact_degree(5, sets[1])
    assert len(degree4) == 1 and len(degree5) == 7
    # A stabilizes every geometric ramification point of degree four.
    assert all(auto(p, m4) == p for p in next(iter(degree4)))
    for n in (1, 4, 5):
        mult = field(n)
        assert all(auto(p, mult) in sets[n] for p in sets[n])
    lookup = {p: i for i, p in enumerate(sorted(degree5, key=lambda Q: min(Q)))}
    permutation = [lookup[frozenset(auto(p, m5) for p in pl)]
                   for pl in sorted(degree5, key=lambda Q: min(Q))]
    assert sum(i == j for i, j in enumerate(permutation)) == 2
    # Three rational five-cycles; on degree-five places: two fixed and one five-cycle.
    m1 = field(1)
    rem = set(sets[1])
    fivecycles = []
    while rem:
        p = min(rem)
        orbit = {p}
        v = auto(p, m1)
        while v not in orbit:
            orbit.add(v)
            v = auto(v, m1)
        assert len(orbit) == 5
        rem -= orbit
        fivecycles.append(orbit)
    assert len(fivecycles) == 3
    power_sums = [counts[n-1] - (2**n+1) for n in range(1,7)]
    coeffs = [1]
    for n in range(1,7):
        val = sum(power_sums[j-1]*coeffs[n-j] for j in range(1,n+1))
        assert val%n == 0
        coeffs.append(val//n)
    assert coeffs == [1, 12, 77, 350, 1261, 3827, 10157]
    print('LOW_DEGREE_CLOSED_PLACE_SPECTRUM_VERIFIED',
          'N_1..6='+repr(counts), 'places_deg2..6=(0,0,1,7,0)',
          'deck_degree5_cycles=(1,1,5)',
          'quotient_rational_fibers=(3_split,2_inert)',
          'Weil_coeffs_0..6='+repr(coeffs), flush=True)

if __name__ == '__main__':
    main()
